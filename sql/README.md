# SQL Examples

These SQL examples use SQLite syntax so they can run locally without a database server. The dataset models a small ecommerce business with customers, products, orders, and order items.

## Setup

```bash
sqlite3 portfolio.db < sql/schema/ecommerce_seed.sql
```

## Run a Query

```bash
sqlite3 portfolio.db < sql/queries/01_monthly_revenue.sql
```

## Query Topics

- `01_monthly_revenue.sql`: Monthly revenue and order trends
- `02_customer_lifetime_value.sql`: Customer value and ranking
- `03_product_performance.sql`: Product revenue, units sold, and average order value
- `04_repeat_purchase_behavior.sql`: Repeat purchase timing
- `05_data_quality_checks.sql`: Null, duplicate, and referential integrity checks
- `06_cohort_retention.sql`: Signup cohort retention by purchase month

