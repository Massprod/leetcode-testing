
# Table: Customer
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | customer_id | int     |
# | product_key | int     |
# +-------------+---------+
# There is no primary key for this table. It may contain duplicates. customer_id is not NULL.
# product_key is a foreign key to Product table.

# Table: Product
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | product_key | int     |
# +-------------+---------+
# product_key is the primary key column for this table.

# SQL schema:
# DROP TABLE IF EXISTS customer, product;
# Create table If Not Exists Customer (customer_id int, product_key int);
# Create table Product (product_key int);
# insert into Customer (customer_id, product_key) values ('1', '5');
# insert into Customer (customer_id, product_key) values ('2', '6');
# insert into Customer (customer_id, product_key) values ('3', '5');
# insert into Customer (customer_id, product_key) values ('3', '6');
# insert into Customer (customer_id, product_key) values ('1', '6');
# insert into Product (product_key) values ('5');
# insert into Product (product_key) values ('6');

# SQL query:
# WITH all_products AS (
# 	SELECT COUNT(*)
# 	FROM product
# )
# SELECT customer_id
# FROM (
# SELECT customer_id
# FROM customer
# GROUP BY customer_id
# HAVING COUNT(DISTINCT product_key) = (SELECT * FROM  all_products)) AS test;

# Failed commit -> didn't see that products can be bought multiple times.
