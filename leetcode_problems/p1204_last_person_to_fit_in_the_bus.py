
# Table: Queue
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | person_id   | int     |
# | person_name | varchar |
# | weight      | int     |
# | turn        | int     |
# +-------------+---------+
# person_id is the primary key column for this table.
# This table has the information about all people waiting for a bus.
# The person_id and turn columns will contain all numbers from 1 to n,
#   where n is the number of rows in the table.
# turn determines the order of which the people will board the bus,
#   where turn=1 denotes the first person to board and turn=n denotes the last person to board.
# weight is the weight of the person in kilograms.
# --------------------------
# There is a queue of people waiting to board a bus. However,
#   the bus has a weight limit of 1000 kilograms, so there may be some people who cannot board.
# Write an SQL query to find the person_name of the last person that can fit on the bus
#   without exceeding the weight limit.
# The test cases are generated such that the first person does not exceed the weight limit.


# SQL schema:
# DROP TABLE IF EXISTS queue;
# Create table If Not Exists Queue (person_id int, person_name varchar(30), weight int, turn int);
# insert into Queue (person_id, person_name, weight, turn) values ('5', 'Alice', '250', '1');
# insert into Queue (person_id, person_name, weight, turn) values ('4', 'Bob', '175', '5');
# insert into Queue (person_id, person_name, weight, turn) values ('3', 'Alex', '350', '2');
# insert into Queue (person_id, person_name, weight, turn) values ('6', 'John Cena', '400', '3');
# insert into Queue (person_id, person_name, weight, turn) values ('1', 'Winston', '500', '6');
# insert into Queue (person_id, person_name, weight, turn) values ('2', 'Marie', '200', '4');

# Made a mistake by thinking this is what I need to return:
# +------+----+-----------+--------+--------------+
# | Turn | ID | Name      | Weight | Total Weight |
# +------+----+-----------+--------+--------------+
# | 1    | 5  | Alice     | 250    | 250          |
# | 2    | 3  | Alex      | 350    | 600          |
# | 3    | 6  | John Cena | 400    | 1000         | (last person to board)
# | 4    | 2  | Marie     | 200    | 1200         | (cannot board)
# | 5    | 4  | Bob       | 175    | ___          |
# | 6    | 1  | Winston   | 500    | ___          |
# +------+----+-----------+--------+--------------+

# And made this query to get this, it can be used to filter after, but we can shorten it.
# PostgreSQl query:
# SELECT "Name" AS "person_name"
# SELECT
# turn AS "Turn",
# person_id AS "ID",
# person_name AS "Name",
# weight AS "Weight",
# (SELECT SUM(weight)
#   FROM queue AS e2
#   WHERE e2.turn <= e1.turn) AS "Total Weight"
# FROM queue AS e1

# Correct query for this without extra steps:
# SELECT
# person_name
# FROM queue AS e1
# WHERE (SELECT SUM(weight)
# 	     FROM queue AS e2
# 	     WHERE e2.turn <= e1.turn) <= 1000
# ORDER BY turn DESC
# LIMIT 1;
# ^^Returns, correct style for the task:
# +-------------+
# | person_name |
# +-------------+
# | John Cena   |
# +-------------+

# SELECT SUM(weight)
# FROM queue AS e2
# WHERE e2.turn <= e1.turn
# ^^Most important part, which summarizes everything in e2 table until we hit e1.turn(current_row)
#   and assign it to a current_row. We're checking every ROW in e1 step by step and at every step we count this SUM().
