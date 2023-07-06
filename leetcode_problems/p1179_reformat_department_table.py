
# Table: Department
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | revenue     | int     |
# | month       | varchar |
# +-------------+---------+
# (id, month) is the primary key of this table.
# The table has information about the revenue of each department per month.
# The month has values in ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"].
# ------------------------
# Write an SQL query to reformat the table such that there is a department id column
#  and a revenue column for each month.
# Return the result table in any order.

# SQL schema:
# DROP TABLE IF EXISTS department;
# Create table If Not Exists Department (id int, revenue int, month varchar(5));
# Truncate table Department;
# insert into Department (id, revenue, month) values ('1', '8000', 'Jan');
# insert into Department (id, revenue, month) values ('2', '9000', 'Jan');
# insert into Department (id, revenue, month) values ('3', '10000', 'Feb');
# insert into Department (id, revenue, month) values ('1', '7000', 'Feb');
# insert into Department (id, revenue, month) values ('1', '6000', 'Mar');

# SQL query:
# SELECT
#     id,
#     MAX(CASE WHEN month = 'Jan' THEN revenue END) AS "Jan_Revenue",
#     MAX(CASE WHEN month = 'Feb' THEN revenue END) AS "Feb_Revenue",
#     MAX(CASE WHEN month = 'Mar' THEN revenue END) AS "Mar_Revenue",
#     MAX(CASE WHEN month = 'Apr' THEN revenue END) AS "Apr_Revenue",
#     MAX(CASE WHEN month = 'May' THEN revenue END) AS "May_Revenue",
#     MAX(CASE WHEN month = 'Jun' THEN revenue END) AS "Jun_Revenue",
#     MAX(CASE WHEN month = 'Jul' THEN revenue END) AS "Jul_Revenue",
#     MAX(CASE WHEN month = 'Aug' THEN revenue END) AS "Aug_Revenue",
#     MAX(CASE WHEN month = 'Sep' THEN revenue END) AS "Sep_Revenue",
#     MAX(CASE WHEN month = 'Oct' THEN revenue END) AS "Oct_Revenue",
#     MAX(CASE WHEN month = 'Nov' THEN revenue END) AS "Nov_Revenue",
#     MAX(CASE WHEN month = 'Dec' THEN revenue END) AS "Dec_Revenue"
# FROM (
#     SELECT DISTINCT id, month, revenue
#     FROM department
# ) AS department_pivot
# GROUP BY id
# ORDER BY id;

# Using MAX() or any aggregate function to escape duplicates when Month have same ID's and Revenue.
