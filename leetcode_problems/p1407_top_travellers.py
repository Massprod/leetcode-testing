
# DROP TABLE IF EXISTS users, rides;
# Create Table If Not Exists Users (id int, name varchar(30));
# Create Table If Not Exists Rides (id int, user_id int, distance int);
# Truncate table Users;
# insert into Users (id, name) values ('1', 'Alice');
# insert into Users (id, name) values ('2', 'Bob');
# insert into Users (id, name) values ('3', 'Alex');
# insert into Users (id, name) values ('4', 'Donald');
# insert into Users (id, name) values ('7', 'Lee');
# insert into Users (id, name) values ('13', 'Jonathan');
# insert into Users (id, name) values ('19', 'Elvis');
# Truncate table Rides;
# insert into Rides (id, user_id, distance) values ('1', '1', '120');
# insert into Rides (id, user_id, distance) values ('2', '2', '317');
# insert into Rides (id, user_id, distance) values ('3', '3', '222');
# insert into Rides (id, user_id, distance) values ('4', '7', '100');
# insert into Rides (id, user_id, distance) values ('5', '13', '312');
# insert into Rides (id, user_id, distance) values ('6', '19', '50');
# insert into Rides (id, user_id, distance) values ('7', '7', '120');
# insert into Rides (id, user_id, distance) values ('8', '19', '400');
# insert into Rides (id, user_id, distance) values ('9', '7', '230');
# ---------------------
# Write an SQL query to report the distance traveled by each user.
# Return the result table ordered by travelled_distance in descending order,
#   if two or more users traveled the same distance, order them by their name in ascending order.

# SQL query:
# SELECT
# e2.name,
# CASE WHEN SUM(e1.distance) IS Null THEN 0
# 	   ELSE sum(e1.distance)
# 	   END AS travelled_distance
# FROM rides AS e1
# RIGHT JOIN users aS e2 ON e1.user_id = e2.id
# GROUP BY e2.name, e1.user_id
# ORDER BY
# -- first_order --
# travelled_distance DESC,
# -- if first_order is equal --
# name ASC;
# ---------------
# Only hard part about this, is that we need to know how to order by multiple columns.
