# Elevate-labs-task-7

# Task 7: Sales Summary using MySQL and Python

## 📌 Objective  
This task demonstrates how to connect Python with a MySQL database, run SQL queries to summarize sales data, and visualize the results using matplotlib.

## 🧰 Tools Used  
- MySQL Workbench  
- Python 3.x  
- mysql-connector-python  
- pandas  
- matplotlib  

## 📁 Dataset & Database  
A MySQL database named `sales_project` is used with one table called `sales`. The table contains basic product sales information.  

**Table Schema:**  
CREATE TABLE sales (  
    product VARCHAR(100),  
    quantity INT,  
    price DECIMAL(10, 2)  
);  

**Sample Data:**  
INSERT INTO sales (product, quantity, price) VALUES  
('Laptop', 10, 700.00),  
('Mouse', 50, 20.00),  
('Keyboard', 30, 35.00),  
('Monitor', 15, 150.00),  
('Headphones', 20, 50.00);  

## 🐍 Python Script Overview  
The Python script performs the following steps:  
1. Connects to the MySQL database using `mysql.connector`.  
2. Executes a SQL query to calculate total quanti
