WITH completed_orders AS (
    SELECT
        customer_id,
        order_id,
        order_date,
        LAG(order_date) OVER (
            PARTITION BY customer_id
            ORDER BY order_date
        ) AS previous_order_date
    FROM orders
    WHERE status = 'completed'
)
SELECT
    customer_id,
    order_id,
    order_date,
    previous_order_date,
    CAST(julianday(order_date) - julianday(previous_order_date) AS INTEGER) AS days_since_previous_order,
    CASE
        WHEN previous_order_date IS NULL THEN 'first purchase'
        WHEN julianday(order_date) - julianday(previous_order_date) <= 45 THEN 'fast repeat'
        ELSE 'slow repeat'
    END AS purchase_pattern
FROM completed_orders
ORDER BY customer_id, order_date;

