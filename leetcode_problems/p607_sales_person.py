from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from tasks_database.db import get_session


# Table: SalesPerson
# +-----------------+---------+
# | Column Name     | Type    |
# +-----------------+---------+
# | sales_id        | int     |
# | name            | varchar |
# | salary          | int     |
# | commission_rate | int     |
# | hire_date       | date    |
# +-----------------+---------+
# sales_id is the primary key column for this table.
# Each row of this table indicates the name and the ID of a salesperson alongside their salary,
#   commission rate, and hire date.

# Table: Company
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | com_id      | int     |
# | name        | varchar |
# | city        | varchar |
# +-------------+---------+
# com_id is the primary key column for this table.
# Each row of this table indicates the name and
#   the ID of a company and the city in which the company is located.

# Table: Orders
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | order_id    | int  |
# | order_date  | date |
# | com_id      | int  |
# | sales_id    | int  |
# | amount      | int  |
# +-------------+------+
# order_id is the primary key column for this table.
# com_id is a foreign key to com_id from the Company table.
# sales_id is a foreign key to sales_id from the SalesPerson table.
# Each row of this table contains information about one order.
# This includes the ID of the company, the ID of the salesperson,
#   the date of the order, and the amount paid.
# ----------------------
# Find the names of all the salespersons who did not have any orders related to the company
#   with the name "RED".
# Return the result table in any order.

# SQL schema:
# DROP TABLE IF EXISTS salesperson, company, orders;
# Create table If Not Exists SalesPerson (sales_id int, name varchar(255), salary int, commission_rate int, hire_date date);
# Create table If Not Exists Company (com_id int, name varchar(255), city varchar(255));
# Create table If Not Exists Orders (order_id int, order_date date, com_id int, sales_id int, amount int);
# insert into SalesPerson (sales_id, name, salary, commission_rate, hire_date)
#   values ('1', 'John', '100000', '6', '4/1/2006');
# insert into SalesPerson (sales_id, name, salary, commission_rate, hire_date)
#   values ('2', 'Amy', '12000', '5', '5/1/2010');
# insert into SalesPerson (sales_id, name, salary, commission_rate, hire_date)
#   values ('3', 'Mark', '65000', '12', '25/12/2008');
# insert into SalesPerson (sales_id, name, salary, commission_rate, hire_date)
#   values ('4', 'Pam', '25000', '25', '1/1/2005');
# insert into SalesPerson (sales_id, name, salary, commission_rate, hire_date)
#   values ('5', 'Alex', '5000', '10', '2/3/2007');
# insert into Company (com_id, name, city) values ('1', 'RED', 'Boston');
# insert into Company (com_id, name, city) values ('2', 'ORANGE', 'New York');
# insert into Company (com_id, name, city) values ('3', 'YELLOW', 'Boston');
# insert into Company (com_id, name, city) values ('4', 'GREEN', 'Austin');
# insert into Orders (order_id, order_date, com_id, sales_id, amount)
#  values ('1', '1/1/2014', '3', '4', '10000');
# insert into Orders (order_id, order_date, com_id, sales_id, amount)
#  values ('2', '2/1/2014', '4', '5', '5000');
# insert into Orders (order_id, order_date, com_id, sales_id, amount)
#  values ('3', '3/1/2014', '1', '1', '50000');
# insert into Orders (order_id, order_date, com_id, sales_id, amount)
#  values ('4', '4/1/2014', '1', '4', '25000');

# Too much to repeat for an easy task, using PgAdmin

# Most basic:
# SELECT name
# FROM salesperson
# WHERE sales_id NOT IN (
# 	SELECT sales_id
# 	FROM orders AS e1
# 	JOIN company AS e2
# 	ON e2.com_id = e1.com_id
# 	AND e2.name LIKE 'RED'
# );
# First what's come on my mind, and it's slow because we're joining every row in a column and filtering.
# While we can just find com_id from company table with name 'RED' and filter on that.

# Faster version:
# SELECT name
# FROM salesperson
# WHERE sales_id NOT IN (
# 	SELECT sales_id
# 	FROM orders
# 	WHERE com_id IN(
# 		SELECT com_id
# 		FROM company
# 		WHERE name LIKE 'RED'
# 	)
# );
