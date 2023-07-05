
# Table: ActorDirector
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | actor_id    | int     |
# | director_id | int     |
# | timestamp   | int     |
# +-------------+---------+
# timestamp is the primary key column for this table.
# ---------------------------

# Find all the pairs (actor_id, director_id) where the actor has cooperated
#   with the director at least three times.
# Return the result table in any order.

# SQL schema:
# DROP TABLE IS EXISTS actordirector;
# Create table If Not Exists ActorDirector (actor_id int, director_id int, timestamp int);
# Truncate table ActorDirector;
# insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '1', '0');
# insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '1', '1');
# insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '1', '2');
# insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '2', '3');
# insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '2', '4');
# insert into ActorDirector (actor_id, director_id, timestamp) values ('2', '1', '5');
# insert into ActorDirector (actor_id, director_id, timestamp) values ('2', '1', '6');

# SQL query:
# SELECT actor_id, director_id
# FROM actordirector
# GROUP BY actor_id, director_id
# HAVING COUNT(*) >= 3;
