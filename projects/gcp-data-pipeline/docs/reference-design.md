# GCP Data Pipeline reference architecture

> [!CAUTION]
> **Independent portfolio demo: no Thales implementation or data.**
> This showcase uses fictional data and generic reference designs to explain engineering ideas from my professional experience. It does not reproduce, document, or disclose Thales's actual systems, architecture, configuration, or critical data. It is not an official Thales project or endorsement.

All components below describe a fictional reference design. No infrastructure, original configuration, production API, or executed batch is included.

## Hourly batch contract

Use fabricated traffic observations with an hour bucket, fictional zone, trip count, and average duration. A reference batch manifest records a batch ID, observation interval, schema version, and processing state. Neither individual taxi journeys nor driver/customer identifiers are needed for the reference.

## Analytical layers

| Layer | Reference contents | Promotion condition |
| --- | --- | --- |
| Staging | Batch metadata and received observation fields. | Valid schema, bounded input, recognized fictional zones. |
| ODS | Standard timestamps/units and reconciled observations keyed by zone and hour. | Explicit duplicate/revision rules and valid numeric values. |
| Warehouse | Hourly facts, zone dimensions, and historical analytical measures. | Accepted batch and consistent metric definitions. |

BigQuery represents the three logical datasets. Cloud Storage can retain independent fictional raw snapshots for replay. Workflows coordinates the jobs; custom extraction belongs in the reference Cloud Run component.

## Completion and failure paths

```mermaid
flowchart TB
  Start["Scheduled batch"] --> Fetch["Fetch and stage"]
  Fetch --> Quality{"Valid input?"}
  Quality -- "No" --> Failed["Failed batch: record reason"]
  Quality -- "Yes" --> Promote["ODS and warehouse promotion"]
  Promote --> Score["Anomaly scoring"]
  Score --> AI["Generate interpretation"]
  AI --> Valid{"Valid AI result?"}
  Valid -- "Yes" --> Ready["Publish labelled insights"]
  Valid -- "No" --> Missing["Mark interpretation unavailable"]
  Ready --> View["Dashboard shows freshness and state"]
  Missing --> View
  Failed --> Stale["Previous accepted data stays labelled stale"]
```

The reference design specifies batch identity to avoid duplicate promotion, bounded retry policies, an explicit latest-success marker, and separately recorded AI errors. Model retraining is a separate controlled job, not silently retried inside every hourly ingestion step.

## Reference services

[Cloud Scheduler can invoke Workflows on a schedule](https://docs.cloud.google.com/workflows/docs/schedule-workflow). [Workflows can coordinate HTTP services and BigQuery jobs](https://docs.cloud.google.com/workflows/docs/overview). The reference permissions and runtime-secret design uses IAM and Secret Manager; logs avoid credentials or raw source records.

This is a design explanation, not a runnable pipeline or evidence that the original professional system used these choices.

[Project overview](../README.md) · [AI analysis](ai-analysis.md)
