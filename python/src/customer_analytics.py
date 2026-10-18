from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from decimal import Decimal
from typing import Iterable


@dataclass(frozen=True)
class Customer:
    customer_id: str
    customer_name: str
    signup_date: str
    region: str


@dataclass(frozen=True)
class Order:
    order_id: str
    customer_id: str
    order_date: str
    order_total: Decimal
    status: str


def completed_orders(orders: Iterable[Order]) -> list[Order]:
    return [order for order in orders if order.status.lower() == "completed"]


def revenue_by_customer(orders: Iterable[Order]) -> dict[str, Decimal]:
    revenue: dict[str, Decimal] = defaultdict(Decimal)
    for order in completed_orders(orders):
        revenue[order.customer_id] += order.order_total
    return dict(revenue)


def revenue_by_region(customers: Iterable[Customer], orders: Iterable[Order]) -> dict[str, Decimal]:
    customer_regions = {customer.customer_id: customer.region for customer in customers}
    revenue: dict[str, Decimal] = defaultdict(Decimal)

    for order in completed_orders(orders):
        region = customer_regions.get(order.customer_id, "Unknown")
        revenue[region] += order.order_total

    return dict(sorted(revenue.items(), key=lambda item: item[0]))


def rank_customers_by_revenue(customers: Iterable[Customer], orders: Iterable[Order]) -> list[dict[str, str]]:
    customer_lookup = {customer.customer_id: customer for customer in customers}
    revenue = revenue_by_customer(orders)

    ranked_rows = []
    for customer_id, total in sorted(revenue.items(), key=lambda item: item[1], reverse=True):
        customer = customer_lookup[customer_id]
        ranked_rows.append(
            {
                "customer_id": customer_id,
                "customer_name": customer.customer_name,
                "region": customer.region,
                "revenue": f"{total:.2f}",
            }
        )

    return ranked_rows


def segment_customer(order_count: int, revenue: Decimal) -> str:
    if order_count >= 3 and revenue >= Decimal("500"):
        return "champion"
    if order_count >= 2 or revenue >= Decimal("250"):
        return "loyal"
    if revenue > Decimal("0"):
        return "new"
    return "inactive"


def customer_segments(customers: Iterable[Customer], orders: Iterable[Order]) -> dict[str, str]:
    totals = revenue_by_customer(orders)
    counts: dict[str, int] = defaultdict(int)

    for order in completed_orders(orders):
        counts[order.customer_id] += 1

    return {
        customer.customer_id: segment_customer(counts[customer.customer_id], totals.get(customer.customer_id, Decimal("0")))
        for customer in customers
    }

