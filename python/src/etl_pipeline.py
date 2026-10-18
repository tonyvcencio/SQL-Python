from __future__ import annotations

import csv
from decimal import Decimal
from pathlib import Path
from sys import path

if __package__ is None:
    path.append(str(Path(__file__).resolve().parent))

from customer_analytics import Customer, Order, customer_segments, rank_customers_by_revenue, revenue_by_region
from data_quality import (
    REQUIRED_CUSTOMER_FIELDS,
    REQUIRED_ORDER_FIELDS,
    find_duplicate_values,
    missing_required_fields,
    normalize_status,
    parse_money,
)


ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data"
OUTPUT_DIR = ROOT / "outputs"


def read_customers(csv_path: Path) -> list[Customer]:
    customers = []
    raw_rows = []
    with csv_path.open(newline="") as handle:
        for row in csv.DictReader(handle):
            raw_rows.append(row)
            missing = missing_required_fields(row, REQUIRED_CUSTOMER_FIELDS)
            if missing:
                raise ValueError(f"Customer row is missing required fields: {missing}")
            customers.append(
                Customer(
                    customer_id=row["customer_id"].strip(),
                    customer_name=row["customer_name"].strip(),
                    signup_date=row["signup_date"].strip(),
                    region=row["region"].strip(),
                )
            )
    duplicates = find_duplicate_values(raw_rows, "customer_id")
    if duplicates:
        raise ValueError(f"Duplicate customer IDs found: {sorted(duplicates)}")
    return customers


def read_orders(csv_path: Path) -> list[Order]:
    orders = []
    raw_rows = []
    with csv_path.open(newline="") as handle:
        for row in csv.DictReader(handle):
            raw_rows.append(row)
            missing = missing_required_fields(row, REQUIRED_ORDER_FIELDS)
            if missing:
                raise ValueError(f"Order row is missing required fields: {missing}")
            orders.append(
                Order(
                    order_id=row["order_id"].strip(),
                    customer_id=row["customer_id"].strip(),
                    order_date=row["order_date"].strip(),
                    order_total=parse_money(row["order_total"]),
                    status=normalize_status(row["status"]),
                )
            )
    duplicates = find_duplicate_values(raw_rows, "order_id")
    if duplicates:
        raise ValueError(f"Duplicate order IDs found: {sorted(duplicates)}")
    return orders


def write_customer_summary(customers: list[Customer], orders: list[Order], output_path: Path) -> None:
    segments = customer_segments(customers, orders)
    ranked_rows = rank_customers_by_revenue(customers, orders)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="") as handle:
        fieldnames = ["customer_id", "customer_name", "region", "revenue", "segment"]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in ranked_rows:
            writer.writerow({**row, "segment": segments[row["customer_id"]]})


def build_portfolio_outputs() -> dict[str, Decimal]:
    customers = read_customers(DATA_DIR / "customers.csv")
    orders = read_orders(DATA_DIR / "orders.csv")
    write_customer_summary(customers, orders, OUTPUT_DIR / "customer_summary.csv")
    return revenue_by_region(customers, orders)


if __name__ == "__main__":
    region_totals = build_portfolio_outputs()
    for region, total in region_totals.items():
        print(f"{region}: ${total:.2f}")
