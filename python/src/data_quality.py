from __future__ import annotations

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from typing import Iterable


REQUIRED_CUSTOMER_FIELDS = ("customer_id", "customer_name", "signup_date", "region")
REQUIRED_ORDER_FIELDS = ("order_id", "customer_id", "order_date", "order_total", "status")


def missing_required_fields(row: dict[str, str], required_fields: Iterable[str]) -> list[str]:
    return [field for field in required_fields if not row.get(field, "").strip()]


def parse_money(value: str) -> Decimal:
    try:
        amount = Decimal(value.strip())
    except (AttributeError, InvalidOperation) as exc:
        raise ValueError(f"Invalid money value: {value!r}") from exc

    if amount < Decimal("0"):
        raise ValueError(f"Money value cannot be negative: {value!r}")

    return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def normalize_status(value: str) -> str:
    normalized = value.strip().lower()
    allowed_statuses = {"completed", "returned", "cancelled"}
    if normalized not in allowed_statuses:
        raise ValueError(f"Unexpected status: {value!r}")
    return normalized


def find_duplicate_values(rows: Iterable[dict[str, str]], field: str) -> set[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()

    for row in rows:
        value = row[field]
        if value in seen:
            duplicates.add(value)
        seen.add(value)

    return duplicates
