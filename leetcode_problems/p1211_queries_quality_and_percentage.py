
# Table: Queries
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | query_name  | varchar |
# | result      | varchar |
# | position    | int     |
# | rating      | int     |
# +-------------+---------+
# There is no primary key for this table, it may have duplicate rows.
# This table contains information collected from some queries on a database.
# The position column has a value from 1 to 500.
# The rating column has a value from 1 to 5. Query with rating less than 3 is a poor query.
# --------------------------
# We define query quality as:
#   The average of the ratio between query rating and its position.
# We also define poor query percentage as:
#   The percentage of all queries with rating less than 3.
# Write an SQL query to find each query_name, the quality and poor_query_percentage.
# Both quality and poor_query_percentage should be rounded to 2 decimal places.
# Return the result table in any order.

# Expected output:
# +------------+---------+-----------------------+
# | query_name | quality | poor_query_percentage |
# +------------+---------+-----------------------+
# | Dog        | 2.50    | 33.33                 |
# | Cat        | 0.66    | 33.33                 |
# +------------+---------+-----------------------+

# SQL schema:
# DROP TABLE IF EXISTS queries;
# Create table If Not Exists Queries (query_name varchar(30), result varchar(50), position int, rating int);
# Truncate table Queries;
# insert into Queries (query_name, result, position, rating) values ('Dog', 'Golden Retriever', '1', '5');
# insert into Queries (query_name, result, position, rating) values ('Dog', 'German Shepherd', '2', '5');
# insert into Queries (query_name, result, position, rating) values ('Dog', 'Mule', '200', '1');
# insert into Queries (query_name, result, position, rating) values ('Cat', 'Shirazi', '5', '2');
# insert into Queries (query_name, result, position, rating) values ('Cat', 'Siamese', '3', '3');
# insert into Queries (query_name, result, position, rating) values ('Cat', 'Sphynx', '7', '4');

# PostgreSQL query:
# SELECT
# query_name,
# ROUND(AVG(rating::decimal/position::decimal), 2) AS "quality",
# ROUND((SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END)::decimal
# 	  /
# 	  COUNT(*)::decimal) * 100, 2) AS "poor_query_percentage"
# FROM queries
# GROUP BY query_name;

# MySQl query:
# SELECT
# query_name,
# ROUND(AVG(rating/position), 2) AS "quality",
# ROUND((SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END)
# 	  /
# 	  COUNT(*)) * 100, 2) AS "poor_query_percentage"
# FROM queries
# GROUP BY query_name;

# Only difference is to force type conversion in Postgresql, otherwise it will be INT division and incorrect result.
