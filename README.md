# SQL-Python: SQL and Python Data Portfolio

This repository showcases practical examples of SQL querying and Python data manipulation. The examples are intentionally small enough to run locally, but they mirror common analytics tasks: cleaning messy records, joining business entities, creating summary metrics, ranking results, segmenting customers, and validating data quality.

## Repository Structure

```text
.
├── sql/
│   ├── schema/
│   │   └── ecommerce_seed.sql
│   ├── queries/
│   │   ├── 01_monthly_revenue.sql
│   │   ├── 02_customer_lifetime_value.sql
│   │   ├── 03_product_performance.sql
│   │   ├── 04_repeat_purchase_behavior.sql
│   │   ├── 05_data_quality_checks.sql
│   │   └── 06_cohort_retention.sql
│   └── README.md
├── python/
│   ├── src/
│   │   ├── customer_analytics.py
│   │   ├── data_quality.py
│   │   └── etl_pipeline.py
│   ├── tests/
│   │   └── test_portfolio_examples.py
│   ├── README.md
│   └── requirements.txt
└── data/
    ├── orders.csv
    └── customers.csv
```

## Skills Demonstrated

SQL examples demonstrate:

- Table creation and realistic seed data
- Joins across customers, orders, order items, and products
- Aggregations, calculated metrics, and date grouping
- Common table expressions
- Window functions for ranking and retention analysis
- Data quality checks using SQL

Python examples demonstrate:

- CSV ingestion with the standard library
- Typed records with `dataclasses`
- Data cleaning and validation
- Grouping, aggregation, and ranking
- Customer segmentation logic
- A small extract-transform-load pipeline
- Unit tests for analytical logic

## Quick Start

Run the Python tests:

```bash
python3 -m unittest discover python/tests
```

Run the SQL examples with SQLite:

```bash
sqlite3 portfolio.db < sql/schema/ecommerce_seed.sql
sqlite3 portfolio.db < sql/queries/01_monthly_revenue.sql
```

Replace the query filename with any file in `sql/queries`.

## Validation & Results

The repository was validated locally on macOS using Python 3 and SQLite.

| Validation | Result |
|---|---|
| Python unit tests | 8 tests passed |
| Python ETL pipeline | Executed successfully |
| Generated customer summary | 4 customer records |
| SQLite analytical queries | All 6 executed successfully |
| SQL data-quality checks | 4 checks returned zero issues |
| Revenue reconciliation | SQL and Python totals matched at $1,085.88 |

### ETL Revenue by Region

| Region | Revenue |
|---|---:|
| Midwest | $129.50 |
| Northeast | $278.99 |
| South | $157.98 |
| West | $519.41 |
| **Total** | **$1,085.88** |

The Python ETL output reconciles with the SQL monthly revenue and customer lifetime value results. These checks confirm successful execution and consistency across the sample dataset; they do not constitute an exhaustive review of all business logic.