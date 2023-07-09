
# SQL schema:
# DROP TYPE IF EXISTS action_enum CASCADE;
# CREATE TYPE action_enum AS ENUM('confirmed', 'timeout');
# DROP TABLE IF EXISTS signups, confirmations;
# Create table If Not Exists Signups (user_id int, time_stamp timestamp);
# Create table If Not Exists Confirmations (user_id int, time_stamp timestamp, action action_enum);
# Truncate table Signups;
# insert into Signups (user_id, time_stamp) values ('3', '2020-03-21 10:16:13');
# insert into Signups (user_id, time_stamp) values ('7', '2020-01-04 13:57:59');
# insert into Signups (user_id, time_stamp) values ('2', '2020-07-29 23:09:44');
# insert into Signups (user_id, time_stamp) values ('6', '2020-12-09 10:39:37');
# Truncate table Confirmations;
# insert into Confirmations (user_id, time_stamp, action) values ('3', '2021-01-06 03:30:46', 'timeout');
# insert into Confirmations (user_id, time_stamp, action) values ('3', '2021-07-14 14:00:00', 'timeout');
# insert into Confirmations (user_id, time_stamp, action) values ('7', '2021-06-12 11:57:29', 'confirmed');
# insert into Confirmations (user_id, time_stamp, action) values ('7', '2021-06-13 12:58:28', 'confirmed');
# insert into Confirmations (user_id, time_stamp, action) values ('7', '2021-06-14 13:59:27', 'confirmed');
# insert into Confirmations (user_id, time_stamp, action) values ('2', '2021-01-22 00:00:00', 'confirmed');
# insert into Confirmations (user_id, time_stamp, action) values ('2', '2021-02-28 23:59:59', 'timeout');
# ----------------------------
# The confirmation rate of a user is the number of 'confirmed' messages divided by
#   the total number of requested confirmation messages.
# The confirmation rate of a user that did not request any confirmation messages is 0.
# Round the confirmation rate to two decimal places.
# Write an SQL query to find the confirmation rate of each user.
# Return the result table in any order.

# PostgreSQL query:
# SELECT
# e3.user_id,
# -- filtering nulls --
# CASE WHEN e3.confirmation_rate IS Null THEN 0
# 	   ELSE e3.confirmation_rate
# 	   END AS confirmation_rate
# FROM(
# 	SELECT
# 	e1.user_id,
# 	e2.confirmation_rate
# 	FROM signups AS e1
# 	LEFT JOIN (
# 		SELECT
# 		user_id,
#       -- confirmation rate of a user --
# 		ROUND(
# 			SUM(CASE WHEN action = 'confirmed' THEN 1
# 			    ELSE 0
# 			    END)::decimal
# 			/
# 			COUNT(action)::decimal, 2) AS confirmation_rate
# 		FROM confirmations
# 		GROUP BY user_id
# 	) AS e2 ON e2.user_id = e1.user_id ) AS e3;
# ----------------------------
# For MySQL -> delete type change.
# Works fine, and not slow. So I'm leaving it like this.
# But there's should be a way to skip extra filtering and make 0 inside.
# ----------------------------
# Yeah, there's COALESCE() -> allows us to choose what to set instead of NULL.

# PostgreSQL query, without extra filtering:
# SELECT
# e1.user_id,
# COALESCE(e2.confirmation_rate, 0) AS confirmation_rate
# FROM signups AS e1
# LEFT JOIN (
#     SELECT
#     user_id,
#   -- confirmation rate of a user --
#     ROUND(
#         SUM(CASE WHEN action = 'confirmed' THEN 1
#             ELSE 0
#             END)::decimal
#         /
#         COUNT(action)::decimal, 2) AS confirmation_rate
#     FROM confirmations
#     GROUP BY user_id) AS e2 ON e2.user_id = e1.user_id;
