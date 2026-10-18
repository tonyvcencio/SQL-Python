SELECT
    p.category,
    p.product_name,
    SUM(oi.quantity) AS units_sold,
    ROUND(SUM(oi.quantity * oi.unit_price), 2) AS gross_revenue,
    ROUND(AVG(oi.unit_price), 2) AS average_selling_price,
    DENSE_RANK() OVER (
        PARTITION BY p.category
        ORDER BY SUM(oi.quantity * oi.unit_price) DESC
    ) AS category_revenue_rank
FROM products AS p
JOIN order_items AS oi
    ON p.product_id = oi.product_id
JOIN orders AS o
    ON oi.order_id = o.order_id
WHERE o.status = 'completed'
GROUP BY p.category, p.product_name
ORDER BY p.category, category_revenue_rank;

