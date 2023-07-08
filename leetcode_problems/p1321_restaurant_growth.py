
# Table: Customer
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | customer_id   | int     |
# | name          | varchar |
# | visited_on    | date    |
# | amount        | int     |
# +---------------+---------+
# (customer_id, visited_on) is the primary key for this table.
# This table contains data about customer transactions in a restaurant.
# visited_on is the date on which the customer with ID (customer_id) has visited the restaurant.
# amount is the total paid by a customer.
# ---------------------------
# You are the restaurant owner, and you want to analyze
#   a possible expansion (there will be at least one customer every day).
# Write an SQL query to compute the moving average of how much the customer paid
#   in a seven days window (i.e., current day + 6 days before).
#   average_amount should be rounded to two decimal places.
# Return result table ordered by visited_on in ascending order.

# SQL schema:
# DROP TABLE IF EXISTS customer;
# Create table If Not Exists Customer (customer_id int, name varchar(20), visited_on date, amount int);
# Truncate table Customer;
# insert into Customer (customer_id, name, visited_on, amount) values ('1', 'Jhon', '2019-01-01', '100');
# insert into Customer (customer_id, name, visited_on, amount) values ('2', 'Daniel', '2019-01-02', '110');
# insert into Customer (customer_id, name, visited_on, amount) values ('3', 'Jade', '2019-01-03', '120');
# insert into Customer (customer_id, name, visited_on, amount) values ('4', 'Khaled', '2019-01-04', '130');
# insert into Customer (customer_id, name, visited_on, amount) values ('5', 'Winston', '2019-01-05', '110');
# insert into Customer (customer_id, name, visited_on, amount) values ('6', 'Elvis', '2019-01-06', '140');
# insert into Customer (customer_id, name, visited_on, amount) values ('7', 'Anna', '2019-01-07', '150');
# insert into Customer (customer_id, name, visited_on, amount) values ('8', 'Maria', '2019-01-08', '80');
# insert into Customer (customer_id, name, visited_on, amount) values ('9', 'Jaze', '2019-01-09', '110');
# insert into Customer (customer_id, name, visited_on, amount) values ('1', 'Jhon', '2019-01-10', '130');
# insert into Customer (customer_id, name, visited_on, amount) values ('3', 'Jade', '2019-01-10', '150');

# PostgreSQL query:
# SELECT
# e1.visited_on,
# -- SUM() of all customers in a WEEK interval --
# (
#  SELECT SUM(amount)
#  FROM customer AS e2
#  WHERE
#  e2.visited_on
#  BETWEEN e1.visited_on - INTERVAL '6 days' AND e1.visited_on
# ) AS amount,
# -- AVG spend in a WEEK interval --
# (
#  SELECT ROUND(SUM(amount)::decimal / 7, 2)
#  FROM customer AS e2
#  WHERE
#  e2.visited_on
#  BETWEEN e1.visited_on - INTERVAL '6 days' AND e1.visited_on
# ) AS average_amount
# FROM customer AS e1
# WHERE e1.visited_on >= (SELECT MIN(visited_on) + INTERVAL '6 days'
# 					      FROM customer)
# GROUP BY e1.visited_on
# ORDER BY e1.visited_on;
# ---------------------------
# Didn't succeed in filtering it all from JOINed table, but it works and fast enough.
# So it's fine with me for now.

# MySQL query:
# SELECT
#  e1.visited_on,
# -- SUM() of all customers in a WEEK interval --
# (
#  SELECT SUM(amount)
#  FROM customer AS e2
#  WHERE
#  e2.visited_on
#  BETWEEN DATE_SUB(e1.visited_on, INTERVAL 6 day) AND e1.visited_on
# ) AS amount,
# -- AVG spend in a WEEK interval --
# (
#  SELECT ROUND(SUM(amount) / 7, 2)
#  FROM customer AS e2
#  WHERE
#  e2.visited_on
#  BETWEEN DATE_SUB(e1.visited_on, INTERVAL 6 day) AND e1.visited_on
# ) AS average_amount
# FROM customer AS e1
# WHERE e1.visited_on >= (SELECT DATE_ADD(MIN(visited_on), INTERVAL 6 day)
# 					      FROM customer)
# GROUP BY e1.visited_on
# ORDER BY e1.visited_on;
# ---------------------------
# For my SQL we need to use DATE_ADD, DATE_SUB, everything else is equal.
