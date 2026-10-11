PRAGMA foreign_keys=ON;
CREATE TABLE IF NOT EXISTS runs(id TEXT PRIMARY KEY,label TEXT NOT NULL,created_at TEXT NOT NULL,raw_file TEXT NOT NULL,input_rows INTEGER NOT NULL,accepted INTEGER NOT NULL,rejected INTEGER NOT NULL,duplicates INTEGER NOT NULL,status TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS staging(id INTEGER PRIMARY KEY,run_id TEXT NOT NULL REFERENCES runs(id),row_number INTEGER NOT NULL,source_json TEXT NOT NULL,status TEXT NOT NULL,error TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS ods(station_id TEXT NOT NULL,observed_at TEXT NOT NULL,count INTEGER NOT NULL CHECK(count>=0),run_id TEXT NOT NULL REFERENCES runs(id),PRIMARY KEY(station_id,observed_at));
CREATE TABLE IF NOT EXISTS models(id INTEGER PRIMARY KEY,body TEXT NOT NULL);
CREATE VIEW IF NOT EXISTS dwh_hourly AS SELECT station_id,observed_at,SUM(count) AS count,COUNT(*) AS source_rows FROM ods GROUP BY station_id,observed_at;
