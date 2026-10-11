-- Optional BigQuery counterpart. Replace PROJECT_ID and DATASET before execution.
-- Run after traffic_hourly contains approved historical station/hour counts.
CREATE OR REPLACE MODEL `PROJECT_ID.DATASET.traffic_baseline`
OPTIONS (
  MODEL_TYPE = 'ARIMA_PLUS',
  TIME_SERIES_TIMESTAMP_COL = 'observed_at',
  TIME_SERIES_DATA_COL = 'count',
  TIME_SERIES_ID_COL = 'station_id'
) AS
SELECT observed_at, count, station_id
FROM `PROJECT_ID.DATASET.traffic_hourly`
WHERE DATE(observed_at) < CURRENT_DATE();

SELECT *
FROM ML.DETECT_ANOMALIES(
  MODEL `PROJECT_ID.DATASET.traffic_baseline`,
  STRUCT(0.95 AS anomaly_prob_threshold),
  (SELECT observed_at, count, station_id
   FROM `PROJECT_ID.DATASET.traffic_hourly`
   WHERE DATE(observed_at) = CURRENT_DATE())
);
