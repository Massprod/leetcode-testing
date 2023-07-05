
# Table: Sales
# +-------------+-------+
# | Column Name | Type  |
# +-------------+-------+
# | sale_id     | int   |
# | product_id  | int   |
# | year        | int   |
# | quantity    | int   |
# | price       | int   |
# +-------------+-------+
# (sale_id, year) is the primary key of this table.
# product_id is a foreign key to Product table.
# Each row of this table shows a sale on the product product_id in a certain year.
# Note that the price is per unit.

# Table: Product
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | product_id   | int     |
# | product_name | varchar |
# +--------------+---------+
# product_id is the primary key of this table.
# Each row of this table indicates the product name of each product.
# --------------------------
# Write an SQL query that selects the product id, year, quantity,
#   and price for the first year of every product sold.
# Return the resulting table in any order.

# SQL schema:
# DROP TABLE IS EXISTS sales, product;
# Create table If Not Exists Sales (sale_id int, product_id int, year int, quantity int, price int);
# Create table If Not Exists Product (product_id int, product_name varchar(10));
# insert into Sales (sale_id, product_id, year, quantity, price) values ('1', '100', '2008', '10', '5000');
# insert into Sales (sale_id, product_id, year, quantity, price) values ('2', '100', '2009', '12', '5000');
# insert into Sales (sale_id, product_id, year, quantity, price) values ('7', '200', '2011', '15', '9000');
# insert into Product (product_id, product_name) values ('100', 'Nokia');
# insert into Product (product_id, product_name) values ('200', 'Apple');
# insert into Product (product_id, product_name) values ('300', 'Samsung');

# SQL query:
# SELECT product_id, year AS first_year, quantity, price
# FROM sales
# WHERE (product_id, year) IN (
# 	SELECT product_id, MIN(year)
# 	FROM sales
# 	GROUP BY product_id
# );

# Guess only difficult part here to call it Medium is that,
#   we need to know that we can use multiple values(columns) for IN statement.
