
# Table: Transactions
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | country       | varchar |
# | state         | enum    |
# | amount        | int     |
# | trans_date    | date    |
# +---------------+---------+
# id is the primary key of this table.
# The table has information about incoming transactions.
# The state column is an enum of type ["approved", "declined"].
# ----------------------------
# Write an SQL query to find for each month and country,
#  the number of transactions and their total amount,
#  the number of approved transactions and their total amount.
# Return the result table in any order.

# SQL schema:
# DROP TYPE IF EXISTS state_enum CASCADE;
# CREATE TYPE state_enum AS ENUM('approved', 'declined');
# DROP TABLE IF EXISTS transactions;
# Create table If Not Exists Transactions (id int, country varchar(4), state state_enum, amount int, trans_date date);
# insert into Transactions (id, country, state, amount, trans_date)
# VALUES
# ('121', 'US', 'approved', '1000', '2018-12-18'),
# ('122', 'US', 'declined', '2000', '2018-12-19'),
# ('123', 'US', 'approved', '2000', '2019-01-01'),
# ('124', 'DE', 'approved', '2000', '2019-01-07');

# Expected output:
# +----------+---------+-------------+----------------+--------------------+-----------------------+
# | month    | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
# +----------+---------+-------------+----------------+--------------------+-----------------------+
# | 2018-12  | US      | 2           | 1              | 3000               | 1000                  |
# | 2019-01  | US      | 1           | 1              | 2000               | 2000                  |
# | 2019-01  | DE      | 1           | 1              | 2000               | 2000                  |
# +----------+---------+-------------+----------------+--------------------+-----------------------+


# PostgreSQL query:
# SELECT
# 	EXTRACT(year FROM trans_date) || '-' || LPAD(EXTRACT(month FROM trans_date)::text, 2, '0'::text) AS "month",
# 	country,
# 	COUNT(*) AS "trans_count",
# 	SUM(CASE
# 	    WHEN state = 'approved' THEN 1 ELSE 0 END
# 	   ) AS "approved_count",
# 	SUM(amount),
# 	SUM(CASE
# 	    WHEN state = 'approved' THEN amount ELSE 0 END
# 	   ) AS "approved_total_amount"
# FROM transactions
# GROUP BY month, country;
# ----------------------------
# MySQL query:
# SELECT
# 	CONCAT(
# 		EXTRACT(year FROM trans_date),
# 		'-',
# 		LPAD(EXTRACT(month FROM trans_date), 2, '0')
# 	       ) AS month,
# 	country,
# 	COUNT(*) AS trans_count,
# 	SUM(CASE
# 		WHEN state = 'approved' THEN 1 ELSE 0 END
# 		) AS approved_count,
# 	SUM(amount) AS trans_total_amount,
# 	SUM(CASE
#       WHEN state = 'approved' THEN amount ELSE 0 END
#       ) AS approved_total_amount
# FROM transactions
# GROUP BY month, country;

# LPAD() to fix month return to include 0 before 1 digit months, like we need in a task_output.
# In postgres extra type convert to text, and dunno why,
# but can't use || to concat() in MySQl so extra using CONCAT() for this.
# Most hard of this was to understand how we can GROUP BY this correctly, and most important part is to use SUM()
# to include only SUM() of correct rows not just month_any combos.
