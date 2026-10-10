# GCP Data Pipeline: anomaly analysis and interpretation

> [!CAUTION]
> **Independent portfolio demo — no Thales implementation or data.**
> This showcase uses fictional data and generic reference designs to explain engineering ideas from my professional experience. It does not reproduce, document, or disclose Thales's actual systems, architecture, configuration, or critical data. It is not an official Thales project or endorsement.

## Proposed analysis stages

1. **Compute observations.** BigQuery produces hourly trip-volume and average-duration series for fictional zones.
2. **Score unusual values.** A proposed BigQuery ML time-series model compares observations against a fitted historical pattern. `ML.DETECT_ANOMALIES` is an available mechanism; no model is trained or evaluated in this documentation.
3. **Generate an explanation.** BigQuery AI with Gemini receives selected measures, comparison context, and anomaly scores. It returns a structured interpretation tied to the batch and zone.
4. **Expose evidence and interpretation.** Looker presents metric history and scores separately from the generated text.

References: [BigQuery ML anomaly detection](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-detect-anomalies), [BigQuery AI functions](https://docs.cloud.google.com/bigquery/docs/generative-ai-overview), and [Looker with BigQuery](https://docs.cloud.google.com/bigquery/docs/looker).

## Fictional illustration

**Invented values and manually written commentary — not a pipeline run, model output, or evaluation result.**

| Field | Illustrative value |
| --- | --- |
| Zone | Harbor North, a fictional zone |
| Observed hour | 17:00–18:00 in the example's declared timezone |
| Average duration | 22 minutes |
| Historical comparison | 14 minutes |
| Potential finding | Duration is above the fictional comparison value. |
| Example commentary | “Travel duration rose in Harbor North. Review the hourly series and data freshness before investigating possible causes.” |

The comparison does not establish an anomaly threshold or causal explanation. The model would need an adequate historical series and evaluation. Do not invent congestion causes, accuracy, saved time, or operational outcomes.

## Dashboard concept

**Concept layout — no Looker report has been built or connected by this draft.**

| Dashboard area | Intended content |
| --- | --- |
| Freshness and batch state | Latest accepted interval, current batch status, and unavailable/stale indicators. |
| Traffic overview | Hourly volume and duration series with zone filters. |
| Anomaly review | Scored observations with the underlying values and model context. |
| AI interpretation | Labelled generated commentary with batch provenance and availability state. |

Generated text stays advisory. A valid output schema is checked separately from whether its interpretation is supported by the measures. Empty history, invalid numeric inputs, stale data, model errors, and unsupported claims need explicit evaluation before any runnable demonstration is described as successful.

[Project overview](../README.md) · [Reference architecture](reference-design.md)
