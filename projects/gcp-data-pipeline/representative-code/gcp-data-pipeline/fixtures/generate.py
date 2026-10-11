"""Reproducible fictional hourly counts; no API or real traffic feed."""
import csv
from datetime import datetime,timedelta,timezone
import math
from pathlib import Path
import random
STATIONS={"central":("Central interchange",235),"riverside":("Riverside junction",185),"airport":("Airport corridor",290),"north":("North ring road",220),"harbour":("Harbour approach",165),"university":("University avenue",145)}
def expected(station,hour):
    return STATIONS[station][1]+65*math.sin((hour-5)*math.pi/12)+35*math.cos(hour*math.pi/12)
def rows(start,days,spike=False):
    rng=random.Random(41)
    for day in range(days):
        for hour in range(24):
            at=(start+timedelta(days=day,hours=hour)).isoformat()
            for station in STATIONS:
                value=round(expected(station,hour)+rng.randint(-6,6))
                if spike and station=="central" and hour==14:value+=320
                if spike and station=="airport" and hour==8:value+=140
                yield {"station_id":station,"observed_at":at,"count":value}
def write(name,data):
    with (Path(__file__).parent/name).open("w",newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=["station_id","observed_at","count"]);writer.writeheader();writer.writerows(data)
if __name__=="__main__":
    write("baseline.csv",rows(datetime(2026,10,4,tzinfo=timezone.utc),7))
    write("observations.csv",rows(datetime(2026,10,11,tzinfo=timezone.utc),1,True))
    write("quality.csv",[{"station_id":"central","observed_at":"not-a-date","count":-9},{"station_id":"unknown","observed_at":"2026-10-12T00:00:00+00:00","count":100}])
