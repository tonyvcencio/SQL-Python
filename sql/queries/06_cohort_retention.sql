WITH first_purchase AS (
    SELECT
        customer_id,
        MIN(order_date) AS first_order_date
    FROM orders
    WHERE status = 'completed'
    GROUP BY customer_id
),
purchase_months AS (
    SELECT DISTINCT
        o.customer_id,
        strftime('%Y-%m', fp.first_order_date) AS cohort_month,
        strftime('%Y-%m', o.order_date) AS activity_month,
        (
            (CAST(strftime('%Y', o.order_date) AS INTEGER) - CAST(strftime('%Y', fp.first_order_date) AS INTEGER)) * 12
            + (CAST(strftime('%m', o.order_date) AS INTEGER) - CAST(strftime('%m', fp.first_order_date) AS INTEGER))
        ) AS months_since_first_purchase
    FROM orders AS o
    JOIN first_purchase AS fp
        ON o.customer_id = fp.customer_id
    WHERE o.status = 'completed'
)
SELECT
    cohort_month,
    months_since_first_purchase,
    COUNT(DISTINCT customer_id) AS retained_customers
FROM purchase_months
GROUP BY cohort_month, months_since_first_purchase
ORDER BY cohort_month, months_since_first_purchase;

