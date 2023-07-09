
# SQL schema:
# DROP TABLE IF EXISTS activities;
# Create table If Not Exists Activities (sell_date date, product varchar(20));
# Truncate table Activities;
# insert into Activities (sell_date, product) values ('2020-05-30', 'Headphone');
# insert into Activities (sell_date, product) values ('2020-06-01', 'Pencil');
# insert into Activities (sell_date, product) values ('2020-06-02', 'Mask');
# insert into Activities (sell_date, product) values ('2020-05-30', 'Basketball');
# insert into Activities (sell_date, product) values ('2020-06-01', 'Bible');
# insert into Activities (sell_date, product) values ('2020-06-02', 'Mask');
# insert into Activities (sell_date, product) values ('2020-05-30', 'T-Shirt');
# ----------------------
# Find for each date the number of different products sold and their names.
# The sold products names for each date should be sorted lexicographically.
# Return the result table ordered by sell_date.

# PostgreSQL query:
# SELECT
#   e1.sell_date,
#   COUNT(DISTINCT e1.product) AS num_sold,
#   STRING_AGG(DISTINCT e1.product, ',' ORDER BY e1.product) AS products
# FROM activities AS e1
# GROUP BY sell_date
# ORDER BY sell_date;

# MySQL query:
# SELECT
#   e1.sell_date,
#   COUNT(DISTINCT e1.product) AS num_sold,
#   GROUP_CONCAT(DISTINCT e1.product ORDER BY e1.product SEPARATOR ',' ) AS products
# FROM activities AS e1
# GROUP BY sell_date
# ORDER BY sell_date;

# STRING_AGG, GROUP_CONCAT ->
# -> both taking every row in a table and concat it together, can be extra filtered and ordered.
