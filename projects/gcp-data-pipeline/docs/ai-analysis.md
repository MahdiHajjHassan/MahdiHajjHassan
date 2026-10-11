# GCP Data Pipeline | Anomaly Scoring and AI Interpretation

> [!CAUTION]
> **Public cloud architecture.** I built a GCP ingestion-to-analytics pipeline; this traffic scenario is an independent design, with no Thales implementation or data and no employer endorsement. Service choices, example values and diagrams explain the architecture. This repository contains documentation, not deployed infrastructure or evaluated model results.

The analytical flow separates measured values, model scores, and generated commentary. Each answers a different question.

## Analysis stages

1. **Measure:** BigQuery produces hourly trip-volume and average-duration series by zone.
2. **Score:** a BigQuery ML time-series model compares observations with historical patterns using `ML.DETECT_ANOMALIES`.
3. **Explain:** Gemini receives selected metrics, comparison context, and anomaly scores, then returns a structured interpretation tied to the batch and zone.
4. **Present:** Looker displays the measurement history, scores, and commentary together.

## An analyst's investigation

| Item | Value |
| --- | --- |
| Zone | Harbor North |
| Hour | 17:00 to 18:00 |
| Average duration | 22 minutes |
| Historical comparison | 14 minutes |
| Question to investigate | Why is the duration above the comparison value? |

The historical series and model threshold determine whether the difference qualifies as an anomaly. An interpretation can point the analyst toward the relevant series and data freshness; it does not establish the cause of the change.

## Dashboard structure

| Area | Contents |
| --- | --- |
| Freshness | Latest accepted interval, batch state, and stale/unavailable indicators. |
| Traffic overview | Volume and duration series, with zone filters. |
| Anomaly review | Scored observations with underlying measurements and model context. |
| AI commentary | Labelled generated text with its batch and availability status. |

## Evaluation concerns

Output-format validation and factual support are separate checks. Evaluation covers empty history, invalid values, stale data, model errors, and explanations that are unsupported by the measurements.

- [BigQuery ML anomaly detection](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-detect-anomalies)
- [BigQuery AI functions](https://docs.cloud.google.com/bigquery/docs/generative-ai-overview)
- [Looker with BigQuery](https://docs.cloud.google.com/bigquery/docs/looker)

[Project overview](../README.md) · [Batch processing](reference-design.md)
