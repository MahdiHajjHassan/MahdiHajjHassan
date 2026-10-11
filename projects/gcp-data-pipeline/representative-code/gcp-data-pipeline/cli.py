"""Execute ingestion/training/export as a real local pipeline."""
import argparse
import json
from pathlib import Path
from service import Product,ROOT
parser=argparse.ArgumentParser()
parser.add_argument("--data-dir",type=Path,default=ROOT/".product-data")
sub=parser.add_subparsers(dest="command",required=True)
run=sub.add_parser("run");run.add_argument("--input",type=Path,default=ROOT/"fixtures/observations.csv");run.add_argument("--label",default="CLI observation batch")
sub.add_parser("train")
export=sub.add_parser("export");export.add_argument("--station",default="all");export.add_argument("--out",type=Path,default=ROOT/".product-data/exports")
sub.add_parser("status")
args=parser.parse_args();app=Product(args.data_dir)
if args.command=="run":result=app.action("run",{"csv":args.input.read_text(encoding="utf-8"),"label":args.label})
elif args.command=="train":result=app.action("train",{})
elif args.command=="export":
    data=app.action("export",{"station_id":args.station});args.out.mkdir(parents=True,exist_ok=True)
    path=args.out/data["filename"];path.write_text(data["content"],encoding="utf-8");result={"output":str(path),"model_sha256":app.state()["model"]["sha256"]}
else:
    state=app.state();result={"runs":state["runs"],"warehouse_rows":state["warehouse_rows"],"model":state["model"],"anomalies":[r for r in state["measures"] if r["anomaly"]]}
print(json.dumps(result,ensure_ascii=False,indent=2))
