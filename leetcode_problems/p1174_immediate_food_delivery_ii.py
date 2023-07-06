# Table: Delivery
# +-----------------------------+---------+
# | Column Name                 | Type    |
# +-----------------------------+---------+
# | delivery_id                 | int     |
# | customer_id                 | int     |
# | order_date                  | date    |
# | customer_pref_delivery_date | date    |
# +-----------------------------+---------+
# delivery_id is the primary key of this table.
# The table holds information about food delivery to customers that make orders
#  at some date and specify a preferred delivery date (on the same order date or after it).
# ----------------------------
# If the customer's preferred delivery date is the same as the order date,
#  then the order is called immediate; otherwise, it is called scheduled.
# The first order of a customer is the order with the earliest order date that the customer made.
# It is guaranteed that a customer has precisely one first order.
# Write an SQL query to find the percentage of immediate orders in the first orders of all customers,
#  rounded to 2 decimal places.

# SQL schema:
# DROP TABLE IF EXISTS delivery;
# Create table Delivery(delivery_id int, customer_id int, order_date date, customer_pref_delivery_date date);
# Truncate table Delivery;
# insert into Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date)
# values ('1', '1', '2019-08-01', '2019-08-02'),
# values ('2', '2', '2019-08-02', '2019-08-02').
# ('3', '1', '2019-08-11', '2019-08-12'),
# ('4', '3', '2019-08-24', '2019-08-24'),
# ('5', '3', '2019-08-21', '2019-08-22'),
# ('6', '2', '2019-08-11', '2019-08-13'),
# ('7', '4', '2019-08-09', '2019-08-09');

# SQL query:
# SELECT ROUND((immediate / (immediate + scheduled)) * 100, 2) AS immediate_percentage
# FROM (
# 	SELECT CAST(COUNT(*) AS DECIMAL) AS immediate
# 	FROM (
# 	    SELECT
# 		customer_id,
# 		MIN(order_date) AS first_order,
# 		MIN(customer_pref_delivery_date) AS first_delivery
# 		FROM delivery
# 		GROUP BY customer_id
# 	) AS all_customers
# 	WHERE first_order = first_delivery) AS immediate,
# 	(
# 	SELECT CAST(COUNT(*) AS DECIMAL) AS scheduled
# 	FROM (
# 	    SELECT
# 		customer_id,
# 		MIN(order_date) AS first_order,
# 		MIN(customer_pref_delivery_date) AS first_delivery
# 		FROM delivery
# 		GROUP BY customer_id
# 	) AS all_customers
# 	WHERE first_order != first_delivery
# 	) AS scheduled;

# One_liners returns :(
# Just taking every option with first_order = first_delivery
# FROM grouped customers with data about their first_delivery and first_order.
# In the second we COUNT() everyone and first counts only immediate deliveries.
# Only problem there is to not forget use CAST() because in PostgreSQL you cant use NUMERIC to round.
# It gives INT division.
