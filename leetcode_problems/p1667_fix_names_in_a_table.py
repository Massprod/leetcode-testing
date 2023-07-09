
# SQL schema:
# DROP TABLE IF EXISTS users;
# Create table If Not Exists Users (user_id int, name varchar(40));
# Truncate table Users;
# insert into Users (user_id, name) values ('1', 'aLice');
# insert into Users (user_id, name) values ('2', 'bOB');
# INSERT INTO users(user_id, name) VALUES ('3', 'kIkNBMasd');
# -------------------
# Fix the names so that only the first character is uppercase and the rest are lowercase.
# Return the result table ordered by user_id.

# PostgreSQL query:
# SELECT
# user_id,
# (UPPER(SUBSTRING(name, 1, 1)) || LOWER(SUBSTRING(name, 2))) AS name
# FROM users
# ORDER BY user_id;

# MySQL query:
# SELECT
# user_id,
# CONCAT(UPPER(SUBSTRING(name, 1, 1)), LOWER(SUBSTRING(name, 2))) AS name
# FROM users
# ORDER BY user_id;

# Failed commit, forgot to order.
