WITH order_totals AS (
    SELECT
        o.order_id,
        strftime('%Y-%m', o.order_date) AS order_month,
        SUM(oi.quantity * oi.unit_price) AS order_revenue
    FROM orders AS o
    JOIN order_items AS oi
        ON o.order_id = oi.order_id
    WHERE o.status = 'completed'
    GROUP BY o.order_id, strftime('%Y-%m', o.order_date)
)
SELECT
    order_month,
    COUNT(order_id) AS completed_orders,
    ROUND(SUM(order_revenue), 2) AS revenue,
    ROUND(AVG(order_revenue), 2) AS average_order_value
FROM order_totals
GROUP BY order_month
ORDER BY order_month;

