
# SQL schema:
# DROP TABLE IF EXISTS users, register;
# Create table If Not Exists Users (user_id int, user_name varchar(20));
# Create table If Not Exists Register (contest_id int, user_id int);
# Truncate table Users;
# insert into Users (user_id, user_name) values ('6', 'Alice');
# insert into Users (user_id, user_name) values ('2', 'Bob');
# insert into Users (user_id, user_name) values ('7', 'Alex');
# Truncate table Register;
# insert into Register (contest_id, user_id) values ('215', '6');
# insert into Register (contest_id, user_id) values ('209', '2');
# insert into Register (contest_id, user_id) values ('208', '2');
# insert into Register (contest_id, user_id) values ('210', '6');
# insert into Register (contest_id, user_id) values ('208', '6');
# insert into Register (contest_id, user_id) values ('209', '7');
# insert into Register (contest_id, user_id) values ('209', '6');
# insert into Register (contest_id, user_id) values ('215', '7');
# insert into Register (contest_id, user_id) values ('208', '7');
# insert into Register (contest_id, user_id) values ('210', '2');
# insert into Register (contest_id, user_id) values ('207', '2');
# insert into Register (contest_id, user_id) values ('210', '7');
# -----------------------
# Write an SQL query to find the percentage of the users registered in each contest rounded to two decimals.
# Return the result table ordered by percentage in descending order.
# In case of a tie, order it by contest_id in ascending order.

# PostgreSQL query:
# SELECT
# contest_id,
# ROUND(SUM(CASE WHEN user_id IN (SELECT user_id FROM users) THEN 1
# 		 	   ELSE 0
# 		 	   END)::decimal
# 	 /
# 	 (SELECT COUNT(user_id)
# 	  FROM users
# 	 )::decimal
# 	 * 100, 2) AS percentage
# FROM register
# GROUP BY contest_id
# ORDER BY percentage DESC, contest_id ASC;
