
# SQL schema:
# DROP TABLE IF EXISTS followers;
# Create table If Not Exists Followers(user_id int, follower_id int);
# Truncate table Followers;
# insert into Followers (user_id, follower_id) values ('0', '1');
# insert into Followers (user_id, follower_id) values ('1', '0');
# insert into Followers (user_id, follower_id) values ('2', '0');
# insert into Followers (user_id, follower_id) values ('2', '1');
# ----------------------
# Write an SQL query that will, for each user, return the number of followers.
# Return the result table ordered by user_id in ascending order.

# SQL query:
# SELECT
# user_id,
# COUNT(DISTINCT follower_id) AS followers_count
# FROM followers
# GROUP BY user_id
# ORDER BY user_id;

# Expected output:
# +---------+----------------+
# | user_id | followers_count|
# +---------+----------------+
# | 0       | 1              |
# | 1       | 1              |
# | 2       | 2              |
# +---------+----------------+
