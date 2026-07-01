
# Retail Intelligence Lakehouse - Project Context

## Vision

Build a scalable price comparison platform that compares grocery prices across BigBasket, Instamart, Amazon, etc.

Purpose:
- Learn Modern Data Engineering.
- Showcase skills for product companies.
- Implement industry-standard architecture.

## Architecture

Medallion Architecture

Raw JSON -> Bronze -> Silver -> Gold

## Key Decisions

- Preserve Raw JSON.
- Use Delta Lake.
- Use PySpark.
- Use Airflow.
- Use Master Product Catalog (MDM).
- Maintain Historical Fact Table.
- Maintain Current State Table.
- Deduplicate in Silver Layer.
- Standardize in Silver Layer.

## Tech Stack

Python
PySpark
Delta Lake
Airflow
Docker
Git
Databricks

## Development Principles

- No hardcoding.
- Configuration driven.
- Failure of one source should not stop entire pipeline.
- Learn every concept deeply.