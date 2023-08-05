
# Table: Store
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | bill_id     | int  |
# | customer_id | int  |
# | amount      | int  |
# +-------------+------+
# bill_id is the primary key (column with unique values) for this table.
# Each row contains information about the amount of one bill and the customer associated with it.
# -------------------
# Write a solution to report the number of customers
#   who had at least one bill with an amount strictly greater than 500.

# SQL schema:
# DROP TABLE IF EXISTS store;
# Create table If Not Exists Store (bill_id int, customer_id int, amount int);
# insert into Store (bill_id, customer_id, amount) values ('6', '1', '549');
# insert into Store (bill_id, customer_id, amount) values ('8', '1', '834');
# insert into Store (bill_id, customer_id, amount) values ('4', '2', '394');
# insert into Store (bill_id, customer_id, amount) values ('11', '3', '657');
# insert into Store (bill_id, customer_id, amount) values ('13', '3', '257');

# SQL query:
# SELECT count(DISTINCT customer_id) AS rich_count
# FROM store
# WHERE amount > 500
