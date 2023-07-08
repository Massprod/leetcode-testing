
# Table: Products
# +------------------+---------+
# | Column Name      | Type    |
# +------------------+---------+
# | product_id       | int     |
# | product_name     | varchar |
# | product_category | varchar |
# +------------------+---------+
# product_id is the primary key for this table.
# This table contains data about the company's products.

# Table: Orders
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | order_date    | date    |
# | unit          | int     |
# +---------------+---------+
# There is no primary key for this table. It may have duplicate rows.
# product_id is a foreign key to the Products table.
# unit is the number of products ordered in order_date.
# -----------------------------
# Write an SQL query to get the names of products that have at least 100 units
#   ordered in February 2020 and their amount.
# Return result table in any order.

# SQL schema:
# DROP TABLE IF EXISTS products, orders;
# Create table If Not Exists Products (product_id int, product_name varchar(40), product_category varchar(40));
# Create table If Not Exists Orders (product_id int, order_date date, unit int);
# Truncate table Products;
# insert into Products (product_id, product_name, product_category) values ('1', 'Leetcode Solutions', 'Book');
# insert into Products (product_id, product_name, product_category) values ('2', 'Jewels of Stringology', 'Book');
# insert into Products (product_id, product_name, product_category) values ('3', 'HP', 'Laptop');
# insert into Products (product_id, product_name, product_category) values ('4', 'Lenovo', 'Laptop');
# insert into Products (product_id, product_name, product_category) values ('5', 'Leetcode Kit', 'T-shirt');
# Truncate table Orders;
# insert into Orders (product_id, order_date, unit) values ('1', '2020-02-05', '60');
# insert into Orders (product_id, order_date, unit) values ('1', '2020-02-10', '70');
# insert into Orders (product_id, order_date, unit) values ('2', '2020-01-18', '30');
# insert into Orders (product_id, order_date, unit) values ('2', '2020-02-11', '80');
# insert into Orders (product_id, order_date, unit) values ('3', '2020-02-17', '2');
# insert into Orders (product_id, order_date, unit) values ('3', '2020-02-24', '3');
# insert into Orders (product_id, order_date, unit) values ('4', '2020-03-01', '20');
# insert into Orders (product_id, order_date, unit) values ('4', '2020-03-04', '30');
# insert into Orders (product_id, order_date, unit) values ('4', '2020-03-04', '60');
# insert into Orders (product_id, order_date, unit) values ('5', '2020-02-25', '50');
# insert into Orders (product_id, order_date, unit) values ('5', '2020-02-27', '50');
# insert into Orders (product_id, order_date, unit) values ('5', '2020-03-01', '50');

# SQL query:
# SELECT product_name, unit
# FROM(
# 	SELECT
# 	e1.product_name,
# 	(SELECT SUM(unit)
# 	 FROM orders AS e2
# 	 WHERE
# 	 EXTRACT(year FROM e2.order_date) = 2020
# 	 AND
# 	 EXTRACT(month FROM e2.order_date) = 2
# 	 AND
# 	 e1.product_id = e2.product_id
#
# 	) AS unit
# 	FROM products AS e1
# ) AS e3
# WHERE unit >= 100;

# ^^Don't like extra select, rebuild with GROUP and JOIN.
# SELECT
# product_name,
# SUM(unit) AS unit
# FROM (
# 	SELECT product_name, unit, order_date
# 	FROM products AS e1
# 	JOIN orders AS e2 ON e1.product_id = e2.product_id
# 	WHERE
# 	EXTRACT(year FROM e2.order_date) = 2020
#   AND
# 	EXTRACT(month FROM e2.order_date) = 2
# ) AS test
# GROUP BY product_name
# HAVING SUM(unit) >= 100

# Both working correctly.
# Expected output:
# +--------------------+---------+
# | product_name       | unit    |
# +--------------------+---------+
# | Leetcode Solutions | 130     |
# | Leetcode Kit       | 100     |
# +--------------------+---------+
