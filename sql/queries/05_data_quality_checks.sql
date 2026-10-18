SELECT
    'orders_without_customers' AS check_name,
    COUNT(*) AS issue_count
FROM orders AS o
LEFT JOIN customers AS c
    ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL

UNION ALL

SELECT
    'order_items_without_orders' AS check_name,
    COUNT(*) AS issue_count
FROM order_items AS oi
LEFT JOIN orders AS o
    ON oi.order_id = o.order_id
WHERE o.order_id IS NULL

UNION ALL

SELECT
    'non_positive_quantities' AS check_name,
    COUNT(*) AS issue_count
FROM order_items
WHERE quantity <= 0

UNION ALL

SELECT
    'missing_customer_regions' AS check_name,
    COUNT(*) AS issue_count
FROM customers
WHERE region IS NULL OR TRIM(region) = '';

