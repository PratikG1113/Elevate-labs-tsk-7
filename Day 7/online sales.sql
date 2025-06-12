-- Create a database (optional if already created)
CREATE DATABASE sales_project;
USE sales_project;

-- Create the sales table
CREATE TABLE sales (
    product VARCHAR(100),
    quantity INT,
    price DECIMAL(10, 2)
);

-- Insert sample data
INSERT INTO sales (product, quantity, price) VALUES
('Laptop', 10, 700.00),
('Mouse', 50, 20.00),
('Keyboard', 30, 35.00),
('Monitor', 15, 150.00),
('Headphones', 20, 50.00);

SELECT * FROM sales;
