# Architecture Decisions

## AD-001: Medallion Architecture

Date: 2026-06-12

Decision:
Use Medallion Architecture.

Flow:
Raw JSON -> Bronze -> Silver -> Gold

Reason:
- Preserve source data
- Enable reprocessing
- Support scalable analytics
- Align with modern lakehouse patterns

Status:
Approved

## AD-002: Generic Ingestion Framework

Date: 2026-06-12

Decision:
Use a common ingestion framework with source-specific adapters.

Reason:
- Reduce duplicate code
- Easier maintenance
- Scalable onboarding of new sources

Status:
Approved

## AD-003: Historical Snapshot Strategy

Date: 2026-06-12

Decision:
Capture product snapshots twice daily initially.

Reason:
- Free
- Simple
- Supports historical analytics
- Can evolve later

Status:
Approved

## AD-004: Fault Isolation

Decision:
Failure of one source should not stop ingestion from other sources.

Reason:
- Improve reliability
- Avoid complete pipeline failures
- Ensure partial data availability

Consequences:
- Additional monitoring required
- Source-specific status tracking needed

Status:
Approved


## AD-005: Master Product Catalog

Decision:
Create a canonical product catalog and map platform-specific products to master products.

Reason:
- Unified analytics
- Consistent reporting
- Cross-platform comparisons

Consequences:
- Product matching logic required
- MDM maintenance required

Status:
Approved

## AD-006: Historical Price Snapshot Fact Table

Decision:
Store every observed price as a historical snapshot record.

Reason:
- Trend analysis
- Discount tracking
- Price history
- Inflation analytics

Consequences:
- Larger storage requirements
- Snapshot scheduling required

Status:
Approved

## AD-007: Raw Data Preservation Strategy

Decision:
Persist every source response as Raw JSON before processing.

Reason:
- Reprocessing support
- Auditability
- Debugging
- Historical consistency
- Schema evolution support
- Multiple downstream consumers

Status:
Approved


## AD-008: Raw Storage Partition Strategy
Date: 2026-07-01

Decision:
Partition raw storage by source and ingestion date.

Structure:

raw/
└── source=<source>/
    └── ingestion_date=<yyyy-mm-dd>/
        └── snapshot_<timestamp>.json

Example:

raw/
└── source=bigbasket/
    └── ingestion_date=2026-07-01/
        ├── snapshot_20260701_080000.json
        └── snapshot_20260701_200000.json

Reason:
- Supports easy reprocessing.
- Simplifies debugging and auditing.
- Preserves historical consistency.
- Scales well as the number of sources grows.
- Aligns with industry-standard data lake partitioning practices.

Status:
Approved

## AD-009: Master Product Catalog Strategy
Decision:
Create a Master Product Catalog to standardize products across platforms.

Reason:
- Enables price comparison across sources.
- Supports historical analytics.
- Handles source-specific naming differences.
- Provides a canonical product definition.
- Allows unavailable products to be represented as NULL.

Status:
Approved



## AD-010: Product Matching Strategy
Decision:
Use a hybrid product matching strategy.

Flow:

1. Exact Match
2. Composite Key Match
3. Fuzzy Match
4. Confidence Threshold Validation

Thresholds:

95%+  → Auto Match
80-95% → Review
<80% → No Match

Reason:
- Reduces incorrect matches.
- Improves comparison accuracy.
- Handles source naming differences.
- Scales well for new sources.

Status:
Approved


## AD-011: Product Granularity Strategy
Decision:
Products with different package sizes or units shall be treated as different Master Products.

Examples:

Aashirvaad Atta 5kg ≠ Aashirvaad Atta 10kg

Reason:
- Ensures accurate price comparison.
- Prevents misleading recommendations.
- Aligns with customer buying behavior.
- Supports precise analytics.

Status:
Approved


## AD-012: Historical Price Storage Strategy
Decision:
Store every product snapshot as a new record.

Do not update previous records.

Reason:
- Supports historical analytics.
- Enables price trend analysis.
- Allows price drop alerts.
- Preserves audit history.
- Improves customer insights.

Future:
Introduce retention and archival policies if storage becomes a concern.

Status:
Approved


## AD-013: Historical Fact Table Strategy
Decision:
Store frequently changing attributes in a separate historical fact table.

Static attributes:
Master Product Dimension

Dynamic attributes:
Price
Discount
Delivery Time
Stock Availability

Reason:
- Supports historical analysis.
- Avoids updating dimension records.
- Aligns with dimensional modeling best practices.
- Improves query performance.

Status:
Approved


## AD-014: Stock Tracking Strategy
Decision:
Store stock availability as quantity rather than a Boolean flag.

Example:

stock_quantity = 20

Reason:
- Supports better customer experience.
- Enables stock trend analysis.
- Allows future cart simulation.
- Provides richer analytics.

Status:
Approved


## AD-015: Current State Table Strategy
Decision:

Maintain two tables.

1. Historical Snapshot Fact Table.
2. Current Product Price Table.

Historical Table:
Stores all snapshots.

Current Table:
Stores latest state for UI queries.

Reason:

- Fast UI response.
- Efficient querying.
- Supports historical analytics.
- Industry best practice.

Status:
Approved

## AD-016: Source Failure Handling Strategy
Decision:

Failure of one source should not fail the entire pipeline.

Pipeline should continue processing remaining sources.

Failed sources shall be marked as unavailable.

Reason:

- Improves reliability.
- Better customer experience.
- Higher system availability.
- Prevents single point of failure.

Status:
Approved


## AD-017: Pipeline Alerting Strategy
Decision:

Pipeline failures shall trigger email notifications.

Single source failures:
Send warning notifications.

Multiple source failures:
Send critical notifications.

Reason:

- Faster issue resolution.
- Improved reliability.
- Reduced downtime.
- Aligns with production support practices.

Future:
Integrate Teams/Slack notifications.

Status:
Approved


## AD-018: Schema Evolution Strategy
Decision:

The pipeline shall not automatically evolve schemas by default.

Process:

1. Preserve Raw JSON.
2. Log schema mismatch errors.
3. Continue processing remaining sources.
4. Notify support team.
5. Fix mappings and replay raw data.

Future:
Limited configuration-driven schema evolution may be introduced.

Reason:

- Ensures data quality.
- Prevents incorrect mappings.
- Supports reliable reprocessing.
- Aligns with production support practices.

Status:
Approved

## AD-019: Retry Strategy
Decision:

Use Exponential Backoff Retry Strategy.

Retries:

1st Retry → 1 minute
2nd Retry → 5 minutes
3rd Retry → 15 minutes

Maximum Retries: 3

After retries are exhausted:

- Mark source as failed.
- Notify support team.
- Continue processing remaining sources.

Reason:

- Reduces unnecessary load.
- Improves reliability.
- Prevents source system flooding.
- Aligns with enterprise best practices.

Status:
Approved

## AD-020: Deduplication Strategy
Decision:

Duplicates shall be preserved in Bronze Layer.

Deduplication shall be performed in Silver Layer.

Reason:

- Preserves source fidelity.
- Supports auditing and debugging.
- Aligns with Medallion Architecture principles.
- Ensures UI receives clean data.

Status:
Approved

## AD-021: Data Standardization Strategy
Decision:

Data standardization shall occur in the Silver Layer.

Examples:

₹299
299 INR
Rs. 299

→ 299.0

Reason:

- Bronze preserves source fidelity.
- Silver creates trusted, standardized datasets.
- Gold remains business-focused.

Status:
Approved


## AD-022: Invalid Data Handling Strategy
Decision:

Introduce a Quarantine Table for invalid records.

Business-driven NULL values are allowed.

Technical/data-quality failures are redirected to quarantine.

Reason:

- Improves data quality.
- Prevents incorrect UI information.
- Supports troubleshooting.
- Preserves failed records for analysis.

Status:
Approved


## AD-023: Logging Strategy
Decision:

Use Python Logging Framework.

Maintain:

1. Central Pipeline Log.
2. Source-specific Logs.

Reason:

- Easier debugging.
- Better production support.
- Faster issue resolution.
- Source isolation.

Status:
Approved


## AD-024: Configuration Management Strategy
Decision:

Externalize all configurable parameters using YAML files.

Examples:

URLs
Retry Count
Timeouts
Paths
Schedule Frequencies

Reason:

- Eliminates hardcoding.
- Improves maintainability.
- Supports multiple environments.
- Industry best practice.

Status:
Approved

## AD-025: Orchestration Strategy
Decision:

Use Apache Airflow as the orchestration framework.

Reason:

- Scheduling.
- Retry Management.
- Monitoring.
- Dependency Handling.
- Industry-standard orchestration tool.

Status:
Approved