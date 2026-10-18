DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id TEXT PRIMARY KEY,
    customer_name TEXT NOT NULL,
    signup_date DATE NOT NULL,
    region TEXT NOT NULL
);

CREATE TABLE products (
    product_id TEXT PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    unit_price NUMERIC NOT NULL
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id TEXT NOT NULL,
    order_date DATE NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price NUMERIC NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO customers (customer_id, customer_name, signup_date, region) VALUES
('C001', 'Avery Smith', '2025-01-15', 'West'),
('C002', 'Jordan Lee', '2025-02-03', 'South'),
('C003', 'Taylor Brown', '2025-02-18', 'West'),
('C004', 'Morgan Davis', '2025-03-01', 'Northeast'),
('C005', 'Riley Wilson', '2025-03-22', 'Midwest'),
('C006', 'Casey Johnson', '2025-04-05', 'South');

INSERT INTO products (product_id, product_name, category, unit_price) VALUES
('P001', 'Analytics Notebook', 'Office', 24.99),
('P002', 'Wireless Keyboard', 'Electronics', 79.99),
('P003', 'USB-C Dock', 'Electronics', 129.50),
('P004', 'Standing Desk Mat', 'Office', 54.00),
('P005', 'Noise Cancelling Headset', 'Electronics', 199.00);

INSERT INTO orders (order_id, customer_id, order_date, status) VALUES
(1001, 'C001', '2025-03-05', 'completed'),
(1002, 'C002', '2025-03-09', 'completed'),
(1003, 'C001', '2025-04-01', 'completed'),
(1004, 'C003', '2025-04-11', 'returned'),
(1005, 'C004', '2025-05-02', 'completed'),
(1006, 'C005', '2025-05-19', 'completed'),
(1007, 'C002', '2025-06-03', 'completed'),
(1008, 'C001', '2025-06-14', 'completed'),
(1009, 'C006', '2025-06-20', 'cancelled');

INSERT INTO order_items (order_item_id, order_id, product_id, quantity, unit_price) VALUES
(1, 1001, 'P001', 2, 24.99),
(2, 1001, 'P002', 1, 79.99),
(3, 1002, 'P004', 1, 54.00),
(4, 1002, 'P001', 1, 24.99),
(5, 1003, 'P003', 1, 129.50),
(6, 1003, 'P001', 3, 24.99),
(7, 1004, 'P004', 1, 54.00),
(8, 1005, 'P005', 1, 199.00),
(9, 1005, 'P002', 1, 79.99),
(10, 1006, 'P003', 1, 129.50),
(11, 1007, 'P001', 1, 24.99),
(12, 1007, 'P004', 1, 54.00),
(13, 1008, 'P002', 2, 79.99),
(14, 1008, 'P001', 1, 24.99);

