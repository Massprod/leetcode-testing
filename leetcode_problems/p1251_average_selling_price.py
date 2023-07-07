
# Table: Prices
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | start_date    | date    |
# | end_date      | date    |
# | price         | int     |
# +---------------+---------+
# (product_id, start_date, end_date) is the primary key for this table.
# Each row of this table indicates the price of the product_id in the period from start_date to end_date.
# For each product_id there will be no two overlapping periods.
# That means there will be no two intersecting periods for the same product_id.

# Table: UnitsSold
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | purchase_date | date    |
# | units         | int     |
# +---------------+---------+
# There is no primary key for this table, it may contain duplicates.
# Each row of this table indicates the date, units, and product_id of each product sold.
# ---------------------------
# Write an SQL query to find the average selling price for each product.
#   average_price should be rounded to 2 decimal places.
# Return the result table in any order.

# SQL schema:
# DROP TABLE IF EXISTS prices, unitssold;
# Create table If Not Exists Prices (product_id int, start_date date, end_date date, price int);
# Create table If Not Exists UnitsSold (product_id int, purchase_date date, units int);
# insert into Prices (product_id, start_date, end_date, price) values ('1', '2019-02-17', '2019-02-28', '5');
# insert into Prices (product_id, start_date, end_date, price) values ('1', '2019-03-01', '2019-03-22', '20');
# insert into Prices (product_id, start_date, end_date, price) values ('2', '2019-02-01', '2019-02-20', '15');
# insert into Prices (product_id, start_date, end_date, price) values ('2', '2019-02-21', '2019-03-31', '30');
# insert into UnitsSold (product_id, purchase_date, units) values ('1', '2019-02-25', '100');
# insert into UnitsSold (product_id, purchase_date, units) values ('1', '2019-03-01', '15');
# insert into UnitsSold (product_id, purchase_date, units) values ('2', '2019-02-10', '200');
# insert into UnitsSold (product_id, purchase_date, units) values ('2', '2019-03-22', '30');

# PostgreSQL query:
# SELECT
# product_id,
# ROUND(
#  SUM((SELECT price
#  	    FROM prices AS e2
#       WHERE e1.product_id = e2.product_id
#       AND e1.purchase_date BETWEEN e2.start_date AND e2.end_date
# 	   ) * units
# 	  )::decimal
#    /
#    SUM(units)::decimal, 2) AS average_price
# FROM unitssold AS e1
# GROUP BY product_id;

# SQL query:
# SELECT
# product_id,
# ROUND(
#  SUM((SELECT price
#  	  FROM prices AS e2
#       WHERE e1.product_id = e2.product_id
#       AND e1.purchase_date BETWEEN e2.start_date AND e2.end_date
# 	 ) * units
# 	)
#  /
#  SUM(units), 2) AS average_price
# FROM unitssold AS e1
# GROUP BY product_id;

# As always we need to force type_change and MySQL handles it by itself.
# Everything else is classic.
