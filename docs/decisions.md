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