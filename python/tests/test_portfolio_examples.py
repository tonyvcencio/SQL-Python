from __future__ import annotations

import sys
import unittest
from decimal import Decimal
from pathlib import Path


SRC_DIR = Path(__file__).resolve().parents[1] / "src"
sys.path.append(str(SRC_DIR))

from customer_analytics import Customer, Order, customer_segments, revenue_by_customer, revenue_by_region
from data_quality import find_duplicate_values, missing_required_fields, normalize_status, parse_money


class CustomerAnalyticsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.customers = [
            Customer("C001", "Avery Smith", "2025-01-15", "West"),
            Customer("C002", "Jordan Lee", "2025-02-03", "South"),
            Customer("C003", "Taylor Brown", "2025-02-18", "West"),
        ]
        self.orders = [
            Order("1001", "C001", "2025-03-05", Decimal("142.50"), "completed"),
            Order("1002", "C002", "2025-03-09", Decimal("84.99"), "completed"),
            Order("1003", "C001", "2025-04-01", Decimal("210.00"), "completed"),
            Order("1004", "C003", "2025-04-11", Decimal("45.75"), "returned"),
            Order("1008", "C001", "2025-06-14", Decimal("176.80"), "completed"),
        ]

    def test_revenue_by_customer_excludes_returns(self) -> None:
        revenue = revenue_by_customer(self.orders)
        self.assertEqual(revenue["C001"], Decimal("529.30"))
        self.assertEqual(revenue["C002"], Decimal("84.99"))
        self.assertNotIn("C003", revenue)

    def test_revenue_by_region_groups_customer_orders(self) -> None:
        revenue = revenue_by_region(self.customers, self.orders)
        self.assertEqual(revenue["West"], Decimal("529.30"))
        self.assertEqual(revenue["South"], Decimal("84.99"))

    def test_customer_segments(self) -> None:
        segments = customer_segments(self.customers, self.orders)
        self.assertEqual(segments["C001"], "champion")
        self.assertEqual(segments["C002"], "new")
        self.assertEqual(segments["C003"], "inactive")


class DataQualityTests(unittest.TestCase):
    def test_missing_required_fields(self) -> None:
        row = {"customer_id": "C001", "customer_name": "", "region": "West"}
        self.assertEqual(missing_required_fields(row, ["customer_id", "customer_name", "signup_date"]), ["customer_name", "signup_date"])

    def test_parse_money_rejects_negative_values(self) -> None:
        with self.assertRaises(ValueError):
            parse_money("-1.00")

    def test_parse_money_quantizes_valid_values(self) -> None:
        self.assertEqual(parse_money("12.345"), Decimal("12.35"))

    def test_normalize_status_rejects_unexpected_values(self) -> None:
        with self.assertRaises(ValueError):
            normalize_status("pending")

    def test_find_duplicate_values(self) -> None:
        rows = [{"order_id": "1001"}, {"order_id": "1002"}, {"order_id": "1001"}]
        self.assertEqual(find_duplicate_values(rows, "order_id"), {"1001"})


if __name__ == "__main__":
    unittest.main()
