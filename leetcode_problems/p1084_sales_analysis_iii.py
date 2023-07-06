
# Table: Product
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | product_id   | int     |
# | product_name | varchar |
# | unit_price   | int     |
# +--------------+---------+
# product_id is the primary key of this table.
# Each row of this table indicates the name and the price of each product.

# Table: Sales
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | seller_id   | int     |
# | product_id  | int     |
# | buyer_id    | int     |
# | sale_date   | date    |
# | quantity    | int     |
# | price       | int     |
# +-------------+---------+
# This table has no primary key, it can have repeated rows.
# product_id is a foreign key to the Product table.
# Each row of this table contains some information about one sale.
# -------------------------
# Write an SQL query that reports the products that were only sold in the first quarter of 2019.
# That is, between 2019-01-01 and 2019-03-31 inclusive.
# Return the result table in any order.


# SQL schema:
# DROP TABLE IF EXISTS product, sales;
# Create table If Not Exists Product (product_id int, product_name varchar(10), unit_price int);
# Create table If Not Exists Sales
#   (seller_id int, product_id int, buyer_id int, sale_date date, quantity int, price int);
# Truncate table Product;
# insert into Product (product_id, product_name, unit_price) values ('1', 'S8', '1000');
# insert into Product (product_id, product_name, unit_price) values ('2', 'G4', '800');
# insert into Product (product_id, product_name, unit_price) values ('3', 'iPhone', '1400');
# Truncate table Sales;
# insert into Sales (seller_id, product_id, buyer_id, sale_date, quantity, price)
# values
# ('1', '1', '1', '2019-01-21', '2', '2000'),
# ('1', '2', '2', '2019-02-17', '1', '800'),
# ('2', '2', '3', '2019-06-02', '1', '800'),
# ('3', '3', '4', '2019-05-13', '2', '2800');

# SQL query:
# SELECT e2.product_id, e2.product_name
# FROM sales AS e1
# JOIN product AS e2
# ON e2.product_id = e1.product_id
# AND e2.product_id NOT IN (
#   SELECT product_id
#   FROM sales
#   WHERE sale_date NOT BETWEEN '2019-01-01' AND '2019-03-31'
# )
# GROUP BY e2.product_id, e2.product_name
