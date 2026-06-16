# SQL-Python
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
