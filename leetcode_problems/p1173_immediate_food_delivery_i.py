# Table: Delivery
# +-----------------------------+---------+
# | Column Name                 | Type    |
# +-----------------------------+---------+
# | delivery_id                 | int     |
# | customer_id                 | int     |
# | order_date                  | date    |
# | customer_pref_delivery_date | date    |
# +-----------------------------+---------+
# delivery_id is the primary key (column with unique values) of this table.
# The table holds information about food delivery to customers that make orders
#   at some date and specify a preferred delivery date (on the same order date or after it).
# -------------------------------
# If the customer's preferred delivery date is the same as the order date,
#   then the order is called immediate; otherwise, it is called scheduled.
# Write a solution to find the percentage of immediate orders in the table,
#   rounded to 2 decimal places.
# -------------------------------

# SQL schema:
# DROP TABLE IF EXISTS delivery;
# CREATE TABLE Delivery (delivery_id int, customer_id int, order_date date, customer_pref_delivery_date date);
# insert into Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date)
# values ('1', '1', '2019-08-01', '2019-08-02'),
# ('2', '5', '2019-08-02', '2019-08-02'),
# ('3', '1', '2019-08-11', '2019-08-11'),
# ('4', '3', '2019-08-24', '2019-08-26'),
# ('5', '4', '2019-08-21', '2019-08-22'),
# ('6', '2', '2019-08-11', '2019-08-13');

# SQL query:
# SELECT ROUND((immediate / all_) * 100, 2) AS immediate_percentage
# FROM (
#     SELECT CAST(COUNT(*) AS decimal) AS immediate
#     FROM (
#         SELECT customer_id
#         FROM delivery
#         WHERE order_date = customer_pref_delivery_date
#     ) as e1
# ) as e2,
# (
#     SELECT CAST(COUNT(*) AS DECIMAL) AS all_
#     FROM (
#         SELECT customer_id
#         FROM delivery
#     ) as e3
# ) as e4;

# Cast for PostgreSQL, but it's actually good to take correct types even in MySQL.
