from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from tasks_database.db import get_session


# Table: Users
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | user_id        | int     |
# | join_date      | date    |
# | favorite_brand | varchar |
# +----------------+---------+
# user_id is the primary key of this table.
# This table has the info of the users of an online shopping website where users can sell and buy items.

# Table: Orders
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | order_id      | int     |
# | order_date    | date    |
# | item_id       | int     |
# | buyer_id      | int     |
# | seller_id     | int     |
# +---------------+---------+
# order_id is the primary key of this table.
# item_id is a foreign key to the Items table.
# buyer_id and seller_id are foreign keys to the Users table.

# Table: Items
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | item_id       | int     |
# | item_brand    | varchar |
# +---------------+---------+
# item_id is the primary key of this table.
# --------------------------
# Write an SQL query to find for each user, the join date and the number of orders they made as a buyer in 2019.
# Return the result table in any order.


# SQl schema:
# DROP TABLE IF EXISTS users, orders, items;
# Create table If Not Exists Users (user_id int, join_date date, favorite_brand varchar(10));
# Create table If Not Exists Orders (order_id int, order_date date, item_id int, buyer_id int, seller_id int);
# Create table If Not Exists Items (item_id int, item_brand varchar(10));
# insert into Users (user_id, join_date, favorite_brand) values ('1', '2018-01-01', 'Lenovo');
# insert into Users (user_id, join_date, favorite_brand) values ('2', '2018-02-09', 'Samsung');
# insert into Users (user_id, join_date, favorite_brand) values ('3', '2018-01-19', 'LG');
# insert into Users (user_id, join_date, favorite_brand) values ('4', '2018-05-21', 'HP');
# insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('1', '2019-08-01', '4', '1', '2');
# insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('2', '2018-08-02', '2', '1', '3');
# insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('3', '2019-08-03', '3', '2', '3');
# insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('4', '2018-08-04', '1', '4', '2');
# insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('5', '2018-08-04', '1', '3', '4');
# insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('6', '2019-08-05', '2', '2', '4');
# insert into Items (item_id, item_brand) values ('1', 'Samsung');
# insert into Items (item_id, item_brand) values ('2', 'Lenovo');
# insert into Items (item_id, item_brand) values ('3', 'LG');
# insert into Items (item_id, item_brand) values ('4', 'HP');


db: Session = next(get_session())
db.execute(
    text(
        "DROP TABLE IF EXISTS users, orders, items;"
        "CREATE TABLE users("
        "   user_id INTEGER,"
        "   join_date DATE,"
        "   favorite_brand VARCHAR(10)"
        ");"
        "CREATE TABLE orders("
        "   order_id INTEGER,"
        "   order_date DATE,"
        "   item_id INTEGER,"
        "   buyer_id INTEGER,"
        "   seller_id INTEGER"
        ");"
        "CREATE TABLE items("
        "   item_id INTEGER,"
        "   item_brand VARCHAR(10)"
        ");"
        "INSERT INTO users(user_id, join_date, favorite_brand) "
        "VALUES "
        "('1', '2018-01-01', 'Lenovo'), "
        "('2', '2018-02-09', 'Samsung'), "
        "('3', '2018-01-19', 'LG'), "
        "('4', '2018-05-21', 'HP');"
        "INSERT INTO orders(order_id, order_date, item_id, buyer_id, seller_id) "
        "VALUES "
        "('1', '2019-08-01', '4', '1', '2'), "
        "('2', '2018-08-02', '2', '1', '3'), "
        "('3', '2019-08-03', '3', '2', '3'), "
        "('4', '2018-08-04', '1', '4', '2'), "
        "('5', '2018-08-04', '1', '3', '4'), "
        "('6', '2019-08-05', '2', '2', '4');"
        "INSERT INTO items(item_id, item_brand) "
        "VALUES "
        "('1', 'Samsung'), "
        "('2', 'Lenovo'), "
        "('3', 'LG'), "
        "('4', 'HP');"
    )
)

# SQL schema:
# SELECT
# DISTINCT e1.user_id AS "buyer_id",
# e1.join_date,
# CASE
# 	WHEN e1.user_id NOT IN (
# 		SELECT buyer_id
# 		FROM (
# 			SELECT
# 			DISTINCT buyer_id,
# 			COUNT(buyer_id) AS count
# 			FROM (
# 				SELECT buyer_id
# 				FROM orders
# 				WHERE EXTRACT(year FROM order_date) = 2019
# 			) AS test
# 			GROUP BY buyer_id) AS test4
# 	)
# 	THEN 0
# 	ELSE test2.count
# 	END AS "orders_in_2019"
# FROM users AS e1
# LEFT JOIN (
# 	SELECT
# 	DISTINCT buyer_id,
# 	COUNT(buyer_id) AS count
# 	FROM (
# 		SELECT *
# 		FROM orders
# 		WHERE EXTRACT(year FROM order_date) = 2019
# 	) AS test
# 	GROUP BY buyer_id
# ) AS test2
# ON e1.user_id = test2.buyer_id
# ORDER BY e1.user_id;

# Finally a normal task, not 1liner.
# Failed first_commit, because I was returning only USERS who bought something in 2019.
# When we needed to return EVERYONE and just set 0 for USERS who didn't buy anything in 2019.

# Not succeeded in making GROUP BY with HAVING correct year, because we need to use order_date inside GROUP BY.
# And if we do this, it's ruining select and giving incorrect data.
# Instead, I filter everything we need first and then use it to choose correct data for every user.
# !
# SELECT
# DISTINCT buyer_id,
# COUNT(buyer_id) AS count
# FROM (
#   SELECT buyer_id
#   FROM orders
#   WHERE EXTRACT(year FROM order_date) = 2019
# ) AS test
# !
# ^^Every buyer_id AND their count of orders made in correct 2019year.
# Now we can take correct IDs from it and filter user_id on it:
# !
# 	WHEN e1.user_id NOT IN (
# 		SELECT buyer_id
# 		FROM (
# 			SELECT
# 			DISTINCT buyer_id,
# 			COUNT(buyer_id) AS count
# 			FROM (
# 				SELECT buyer_id
# 				FROM orders
# 				WHERE EXTRACT(year FROM order_date) = 2019
# 			) AS test
# 			GROUP BY buyer_id) AS test4
# 	)
# !
# Everything else is simple. Standard LEFT JOIN to include every USER and add COUNT data as column for them.

data: Result = db.execute(
    text(
        "SELECT "
        'DISTINCT e1.user_id AS "buyer_id", '
        'e1.join_date, '
        'CASE '
        '   WHEN e1.user_id NOT IN ('
        '       SELECT buyer_id '
        '       FROM ('
        '           SELECT '
        '           DISTINCT buyer_Id, '
        '           COUNT(buyer_id) AS count '
        '           FROM ('
        '               SELECT buyer_id '
        '               FROM orders '
        '               WHERE EXTRACT(year FROM order_date) = 2019 '
        '           ) AS test '
        '        GROUP BY buyer_id) AS test4 '
        '   )'
        '   THEN 0 '
        '   ELSE test2.count '
        '   END AS "orders_in_2019" '
        'FROM users AS e1 '
        'LEFT JOIN ( '
        '   SELECT '
        '   DISTINCT buyer_id, '
        '   COUNT(buyer_id) AS count '
        '   FROM ('
        '       SELECT * '
        '       FROM orders '
        '       WHERE EXTRACT(year FROM order_date) = 2019 '
        '   ) AS test '
        '   GROUP BY buyer_id '
        ') AS test2 '
        'ON e1.user_id = test2.buyer_id '
        'ORDER BY e1.user_id;'
    )
)

for _ in data:
    print(_)

# Expected output:
# +-----------+------------+----------------+
# | buyer_id  | join_date  | orders_in_2019 |
# +-----------+------------+----------------+
# | 1         | 2018-01-01 | 1              |
# | 2         | 2018-02-09 | 2              |
# | 3         | 2018-01-19 | 0              |
# | 4         | 2018-05-21 | 0              |
# +-----------+------------+----------------+
