# GCP Data Pipeline: anomaly analysis and interpretation

> [!CAUTION]
> **Professional experience, protected information.**
> This public showcase uses independent reference designs and fictional examples, with no Thales implementation or data. It discloses no employer code, systems, configuration, or critical information and carries no official endorsement. Diagrams explain the design; they are illustrations, not application screenshots or execution results. The traffic scenario and service composition are independent design choices. This repository supplies documentation rather than deployed infrastructure, model outputs, or evaluation results.

## Reference analysis stages

1. **Compute observations.** BigQuery produces hourly trip-volume and average-duration series for each zone.
2. **Score unusual values.** A reference BigQuery ML time-series model compares observations against a fitted historical pattern. `ML.DETECT_ANOMALIES` provides the anomaly-detection mechanism.
3. **Generate an explanation.** BigQuery AI with Gemini receives selected measures, comparison context, and anomaly scores. It returns a structured interpretation tied to the batch and zone.
4. **Expose evidence and interpretation.** Looker presents metric history and scores separately from the generated text.

References: [BigQuery ML anomaly detection](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-detect-anomalies), [BigQuery AI functions](https://docs.cloud.google.com/bigquery/docs/generative-ai-overview), and [Looker with BigQuery](https://docs.cloud.google.com/bigquery/docs/looker).

## Reading an hourly observation

| Field | Illustrative value |
| --- | --- |
| Zone | Harbor North |
| Observed hour | 17:00 to 18:00 in the example's declared timezone |
| Average duration | 22 minutes |
| Historical comparison | 14 minutes |
| Potential finding | Duration is above the comparison value. |
| Example commentary | “Travel duration rose in Harbor North. Review the hourly series and data freshness before investigating possible causes.” |

The historical series and evaluated threshold determine whether the difference qualifies as an anomaly. The observation gives analysts a starting point for investigation.

## Dashboard design

| Dashboard area | Intended content |
| --- | --- |
| Freshness and batch state | Latest accepted interval, current batch status, and unavailable/stale indicators. |
| Traffic overview | Hourly volume and duration series with zone filters. |
| Anomaly review | Scored observations with the underlying values and model context. |
| AI interpretation | Labelled generated commentary with batch provenance and availability state. |

Generated text stays advisory. A valid output schema is checked separately from whether its interpretation is supported by the measures. Empty history, invalid numeric inputs, stale data, model errors, and unsupported claims need explicit evaluation as part of model and interpretation evaluation.

[Project overview](../README.md) · [Reference architecture](reference-design.md)
