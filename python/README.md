# Python Examples

These examples use the Python standard library so they are easy to run in any environment.

## Run Tests

```bash
python3 -m unittest discover python/tests
```

## Run the ETL Pipeline

```bash
python3 python/src/etl_pipeline.py
```

The scripts demonstrate:

- Reading CSV files
- Cleaning and normalizing raw values
- Validating required fields and numeric ranges
- Aggregating orders by customer and region
- Segmenting customers based on order behavior
- Writing a clean summary file

