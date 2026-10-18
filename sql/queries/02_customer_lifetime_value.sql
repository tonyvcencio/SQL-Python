WITH customer_orders AS (
    SELECT
        c.customer_id,
        c.customer_name,
        c.region,
        o.order_id,
        SUM(oi.quantity * oi.unit_price) AS order_revenue
    FROM customers AS c
    JOIN orders AS o
        ON c.customer_id = o.customer_id
    JOIN order_items AS oi
        ON o.order_id = oi.order_id
    WHERE o.status = 'completed'
    GROUP BY c.customer_id, c.customer_name, c.region, o.order_id
)
SELECT
    customer_id,
    customer_name,
    region,
    COUNT(order_id) AS completed_orders,
    ROUND(SUM(order_revenue), 2) AS lifetime_value,
    RANK() OVER (ORDER BY SUM(order_revenue) DESC) AS value_rank
FROM customer_orders
GROUP BY customer_id, customer_name, region
ORDER BY lifetime_value DESC;

