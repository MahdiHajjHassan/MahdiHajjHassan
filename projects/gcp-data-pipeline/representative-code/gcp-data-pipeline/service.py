"""Raw files -> staging quality -> ODS -> DWH -> fitted model -> anomaly evidence."""
from contextlib import closing,contextmanager
import csv
from datetime import datetime,timedelta,timezone
import hashlib
import io
import json
from pathlib import Path
import sqlite3
import uuid
from model import fit,predict
from fixtures.generate import STATIONS,rows

ROOT=Path(__file__).resolve().parent
def now():return datetime.now(timezone.utc).isoformat(timespec="seconds")
def csv_text(values):
    buffer=io.StringIO(newline="")
    values=list(values)
    fields=list(values[0]) if values else ["station_id","observed_at","count","predicted","z_score","anomaly"]
    writer=csv.DictWriter(buffer,fieldnames=fields);writer.writeheader();writer.writerows(values)
    return buffer.getvalue()

class Product:
    def __init__(self,data_dir):
        self.data_dir=Path(data_dir);self.data_dir.mkdir(parents=True,exist_ok=True)
        self.path=self.data_dir/"traffic.sqlite3"
        (self.data_dir/"raw").mkdir(exist_ok=True);(self.data_dir/"models").mkdir(exist_ok=True)
        with self.db() as db:
            db.executescript((ROOT/"warehouse.sql").read_text())
            empty=not db.execute("SELECT 1 FROM runs").fetchone()
        if empty:
            self.run(self.fixture("baseline.csv"),"Historical baseline")
            self.train()
            self.run(self.fixture("observations.csv"),"Hourly traffic / 11 October")
    @contextmanager
    def db(self):
        with closing(sqlite3.connect(self.path)) as db:
            db.row_factory=sqlite3.Row;db.execute("PRAGMA foreign_keys=ON")
            with db:yield db
    @staticmethod
    def fixture(name):
        if name not in ("baseline.csv","observations.csv","quality.csv"):raise ValueError("Unknown fixture.")
        return (ROOT/"fixtures"/name).read_text(encoding="utf-8")
    @staticmethod
    def normalize(row):
        station=row.get("station_id")
        if station not in STATIONS:raise ValueError("Unknown station.")
        try:at=datetime.fromisoformat(row.get("observed_at","").replace("Z","+00:00"))
        except (ValueError,TypeError):raise ValueError("Timestamp must be ISO 8601.")
        if at.tzinfo is None:raise ValueError("Timestamp must include its timezone.")
        if at.minute or at.second or at.microsecond:raise ValueError("Each observation must align with an hour.")
        try:count=int(row.get("count"))
        except (ValueError,TypeError):raise ValueError("Count must be a whole number.")
        if str(count)!=str(row.get("count")) or not 0<=count<=100000:raise ValueError("Count must be a whole number from 0 to 100000.")
        return station,at.astimezone(timezone.utc).isoformat(),count
    def run(self,content,label):
        if not isinstance(content,str) or len(content)>1_000_000:raise ValueError("Provide CSV input below 1 MiB.")
        if not isinstance(label,str) or not 1<=len(label.strip())<=100:raise ValueError("Give this batch a label.")
        reader=csv.DictReader(io.StringIO(content))
        if not reader.fieldnames or set(reader.fieldnames)!={"station_id","observed_at","count"}:raise ValueError("CSV columns must be station_id, observed_at and count.")
        data=list(reader)
        if not data or len(data)>10000:raise ValueError("Provide 1 to 10000 observations.")
        run_id="RUN-"+uuid.uuid4().hex[:8].upper()
        raw_file="raw/"+run_id+".csv";(self.data_dir/raw_file).write_text(content,encoding="utf-8")
        accepted=rejected=duplicates=0
        with self.db() as db:
            db.execute("INSERT INTO runs VALUES (?,?,?,?,0,0,0,0,'running')",(run_id,label.strip(),now(),raw_file))
            for n,row in enumerate(data,2):
                status="accepted";error=""
                try:
                    station,at,count=self.normalize(row)
                    if db.execute("SELECT 1 FROM ods WHERE station_id=? AND observed_at=?",(station,at)).fetchone():
                        duplicates+=1;status="duplicate";error="Station/hour already exists in ODS."
                    else:
                        db.execute("INSERT INTO ods VALUES (?,?,?,?)",(station,at,count,run_id));accepted+=1
                except ValueError as e:
                    rejected+=1;status="rejected";error=str(e)
                db.execute("INSERT INTO staging(run_id,row_number,source_json,status,error) VALUES (?,?,?,?,?)",(run_id,n,json.dumps(row),status,error))
            status="quality warning" if rejected else "completed"
            db.execute("UPDATE runs SET input_rows=?,accepted=?,rejected=?,duplicates=?,status=? WHERE id=?",(len(data),accepted,rejected,duplicates,status,run_id))
        result={"id":run_id,"raw_file":raw_file,"input_rows":len(data),"accepted":accepted,"rejected":rejected,"duplicates":duplicates,"status":status,"message":f"Processed {len(data)} observations; {accepted} entered the warehouse."}
        (self.data_dir/"raw"/(run_id+"-summary.json")).write_text(json.dumps(result,indent=2),encoding="utf-8")
        return result
    def train(self):
        with self.db() as db:
            latest=db.execute("SELECT MAX(substr(observed_at,1,10)) FROM ods").fetchone()[0]
            days=db.execute("SELECT COUNT(DISTINCT substr(observed_at,1,10)) FROM ods").fetchone()[0]
            training=[dict(r) for r in db.execute("SELECT * FROM ods WHERE substr(observed_at,1,10)<? ORDER BY observed_at",(latest,))] if days>7 else [dict(r) for r in db.execute("SELECT * FROM ods ORDER BY observed_at")]
            if len(training)<48:raise ValueError("At least 48 historical observations are needed.")
            models={}
            for station in STATIONS:
                samples=[{"hour":datetime.fromisoformat(r["observed_at"]).hour,"count":r["count"]} for r in training if r["station_id"]==station]
                if len(samples)<24:raise ValueError("Every station needs a full daily training profile.")
                models[station]=fit(samples)
            model={"name":"Daily harmonic regression","trained_at":now(),"training_rows":len(training),"training_start":training[0]["observed_at"],"training_end":training[-1]["observed_at"],"threshold":3.0,"stations":models,"features":["intercept","sin(hour / 24 * 2π)","cos(hour / 24 * 2π)"]}
            digest=hashlib.sha256(json.dumps(model,sort_keys=True).encode()).hexdigest();model["sha256"]=digest
            db.execute("INSERT INTO models(body) VALUES (?)",(json.dumps(model),))
        (self.data_dir/"models"/(digest[:12]+".json")).write_text(json.dumps(model,indent=2),encoding="utf-8")
        return {"model":model,"message":"Trained and stored a daily model from historical observations."}
    def state(self):
        with self.db() as db:
            model_row=db.execute("SELECT body FROM models ORDER BY id DESC LIMIT 1").fetchone()
            model=json.loads(model_row[0]) if model_row else None
            latest=db.execute("SELECT MAX(substr(observed_at,1,10)) FROM dwh_hourly").fetchone()[0]
            measures=[]
            for row in db.execute("SELECT * FROM dwh_hourly WHERE substr(observed_at,1,10)=? ORDER BY observed_at,station_id",(latest,)):
                v=dict(row);m=model["stations"].get(v["station_id"]) if model else None
                estimate=predict(m,datetime.fromisoformat(v["observed_at"]).hour) if m else v["count"]
                z=(v["count"]-estimate)/m["scale"] if m else 0
                v.update(predicted=round(estimate,2),z_score=round(z,2),anomaly=abs(z)>=3,station_name=STATIONS[v["station_id"]][0]);measures.append(v)
            runs=[dict(r) for r in db.execute("SELECT * FROM runs ORDER BY rowid DESC LIMIT 20")]
            quarantine=[dict(r) for r in db.execute("SELECT s.*,r.label FROM staging s JOIN runs r ON r.id=s.run_id WHERE s.status='rejected' ORDER BY s.id DESC LIMIT 30")]
            warehouse_rows=db.execute("SELECT COUNT(*) FROM ods").fetchone()[0]
            staging_rows=db.execute("SELECT COUNT(*) FROM staging").fetchone()[0]
        return {"stations":[{"id":k,"name":v[0]} for k,v in STATIONS.items()],"model":model,"measures":measures,"runs":runs,"quarantine":quarantine,"warehouse_rows":warehouse_rows,"staging_rows":staging_rows,"selected_day":latest,"sample_csv":self.fixture("observations.csv")}
    def action(self,name,payload):
        if name=="run":return self.run(payload.get("csv"),payload.get("label","Uploaded traffic batch"))
        if name=="train":return self.train()
        if name=="scenario":
            selected=payload.get("scenario","spike")
            if selected not in ("normal","spike","quality"):raise ValueError("Choose normal, spike or quality.")
            if selected=="quality":return self.run(self.fixture("quality.csv"),"Quality gate / invalid observations")
            day=datetime.fromisoformat(self.state()["selected_day"]).replace(tzinfo=timezone.utc)+timedelta(days=1)
            return self.run(csv_text(rows(day,1,selected=="spike")),selected.capitalize()+" traffic batch")
        if name=="run_detail":
            with self.db() as db:
                run=db.execute("SELECT * FROM runs WHERE id=?",(payload.get("id"),)).fetchone()
                if not run:raise ValueError("Run not found.")
                return {"run":dict(run),"staging":[dict(r) for r in db.execute("SELECT * FROM staging WHERE run_id=? LIMIT 100",(run["id"],))]}
        if name=="export":
            selected=payload.get("station_id","all")
            if selected not in ("all",*STATIONS):raise ValueError("Choose a known station.")
            state=self.state()
            values=[v for v in state["measures"] if selected=="all" or v["station_id"]==selected]
            return {"filename":f"traffic-{state['selected_day']}-{selected}.csv","mime":"text/csv","content":csv_text(values)}
        if name=="model_export":
            return {"filename":"traffic-model.json","content":self.state()["model"],"mime":"application/json"}
        raise ValueError("Unknown pipeline action.")
