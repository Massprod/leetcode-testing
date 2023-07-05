from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from tasks_database.db import get_session


# Table: RequestAccepted
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | requester_id   | int     |
# | accepter_id    | int     |
# | accept_date    | date    |
# +----------------+---------+
# (requester_id, accepter_id) is the primary key for this table.
# This table contains the ID of the user who sent the request,
#   the ID of the user who received the request,
#   and the date when the request was accepted.
# -----------------------------
# Write an SQL query to find the people who have the most friends and the most friends number.
# The test cases are generated so that only one person has the most friends.
# -----------------------------
# Follow up: In the real world, multiple people could have the same most number of friends.
# Could you find all these people in this case?

# SQL schema:
# DROP TABLE IF EXISTS requestaccepted;
# Create table RequestAccepted (requester_id int not null, accepter_id int null, accept_date date null);
# insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('1', '2', '2016/06/03');
# insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('1', '3', '2016/06/08');
# insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('2', '3', '2016/06/08');
# insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('3', '4', '2016/06/09');
# INSERT INTO requestaccepted (requester_id, accepter_id, accept_date) VALUES ('1', '4', '2016/06/10');

db: Session = next(get_session())
db.execute(
    text(
        "DROP TABLE IF EXISTS requestaccepted;"
        "CREATE TABLE requestaccepted("
        "   requester_id INTEGER NOT NULL,"
        "   accepter_id INTEGER NULL,"
        "   accept_date DATE NULL"
        ");"
    )
)
db.commit()
db.execute(
    text(
        "INSERT INTO requestaccepted(requester_id, accepter_id, accept_date) "
        "VALUES "
        "('1', '2', '2016/06/03'), "
        "('1', '3', '2016/06/08'),"
        "('2', '3', '2016/06/08'),"
        "('3', '4', '2016/06/09'),"
        "('1', '4', '2016/06/10')"
        ";"
    )
)
db.commit()

# How we can calculate everything together?
# Like we know that every possible record in requester_id means that there's friend for this person in accepter_id.
# Grouping COUNT by requester_id will give us all friends for person with that id.
# But this person is a friend for a person in accepter_id as well.
# So we need to summarize groups in 1 column and another?.

# SELECT requester_id AS id, SUM(count)
# FROM (
# SELECT requester_id, COUNT(accepter_id)
# FROM requestaccepted
# GROUP BY requester_id
# UNION ALL
# SELECT accepter_id, COUNT(requester_id)
# FROM requestaccepted
# GROUP BY accepter_id) AS test
# GROUP BY requester_id
# ORDER BY sum DESC
# LIMIT 1;

# Ok a little robust but working.
# If we need to see everyone with same amount friends?
# Every data already here, but we need to filter with HAVING, and only way I see we can get this value
# of maximum friends is to use another SUBQUERY to find it.
# Actually repeating all this and filter on that?

# Ok there's 2 versions:
# First is PostgreSQL:
# SELECT id, num
# FROM (
# 	SELECT requester_id AS id, SUM(count) AS num
# 	FROM (
# 	SELECT requester_id, COUNT(accepter_id) AS count
# 	FROM requestaccepted
# 	GROUP BY requester_id
# 	UNION ALL
# 	SELECT accepter_id, COUNT(requester_id) AS count
# 	FROM requestaccepted
# 	GROUP BY accepter_id) AS test
# 	GROUP BY requester_id
# ) AS all_friends
# GROUP BY id, num
# HAVING num IN (
# 	SELECT SUM(count) AS num
# 	FROM (
# 	SELECT requester_id, COUNT(accepter_id) AS count
# 	FROM requestaccepted
# 	GROUP BY requester_id
# 	UNION ALL
# 	SELECT accepter_id, COUNT(requester_id) AS count
# 	FROM requestaccepted
# 	GROUP BY accepter_id) AS test
# 	GROUP BY requester_id
# 	ORDER BY num DESC
# 	LIMIT 1
# );

# Second is MySQL:
# SELECT id, num
# FROM (
# 	SELECT requester_id AS id, SUM(count) AS num
# 	FROM (
# 	SELECT requester_id, COUNT(accepter_id) AS count
# 	FROM requestaccepted
# 	GROUP BY requester_id
# 	UNION ALL
# 	SELECT accepter_id, COUNT(requester_id) AS count
# 	FROM requestaccepted
# 	GROUP BY accepter_id) AS test
# 	GROUP BY requester_id
# ) AS all_friends
# GROUP BY id, num
# HAVING num IN (
#   SELECT MAX(num)
#   FROM (
# 	SELECT SUM(count) AS num
# 	FROM (
# 	SELECT requester_id, COUNT(accepter_id) AS count
# 	FROM requestaccepted
# 	GROUP BY requester_id
# 	UNION ALL
# 	SELECT accepter_id, COUNT(requester_id) AS count
# 	FROM requestaccepted
# 	GROUP BY accepter_id) AS test
# 	GROUP BY requester_id) AS test2
# );
# In MySQL we can't use LIMIT directly, so I'm taking EXTRA SUBQUERY to find MAX() value of friends.

# My local is PostgreSQL so:
data: Result = db.execute(
    text(
        "SELECT id, num "
        "FROM ("
        "   SELECT requester_id AS id, SUM(count) AS num "
        "   FROM ("
        "       SELECT requester_id, COUNT(accepter_id) AS count "
        "       FROM requestaccepted "
        "       GROUP BY requester_id "
        "       UNION ALL "
        "       SELECT accepter_id, COUNT(requester_id) AS count "
        "       FROM requestaccepted "
        "       GROUP BY accepter_id) AS test"
        "   GROUP BY requester_id) AS all_friends "
        "GROUP BY id, num "
        "HAVING num IN ("
        "   SELECT SUM(count) AS num "
        "   FROM ("
        "       SELECT requester_id, COUNT(accepter_id) AS count "
        "       FROM requestaccepted "
        "       GROUP BY requester_id "
        "       UNION ALL"
        "       SELECT accepter_id, COUNT(requester_id) AS count "
        "       FROM requestaccepted "
        "       GROUP BY accepter_id) AS test"
        "   GROUP BY requester_id "
        "   ORDER BY num DESC "
        "   LIMIT 1"
        ");"
    )
)
for _ in data:
    print(_)

# Expected output:
# +----+-----+
# | id | num |
# +----+-----+
# | 1  | 3   |
# | 3  | 3   |
# +----+-----+

# More pretty option by GPT:
# SELECT requester_id AS id, COUNT(accepter_id) AS num
# FROM (
#   SELECT requester_id, accepter_id
#   FROM RequestAccepted
#   UNION ALL
#   SELECT accepter_id, requester_id
#   FROM RequestAccepted
# ) AS friendships
# GROUP BY requester_id
# HAVING COUNT(accepter_id) = (
#   SELECT COUNT(accepter_id) AS max_friends
#   FROM (
#     SELECT requester_id, accepter_id
#     FROM RequestAccepted
#     UNION ALL
#     SELECT accepter_id, requester_id
#     FROM RequestAccepted
#   ) AS inner_friendships
#   GROUP BY requester_id
#   ORDER BY max_friends DESC
#   LIMIT 1
# )
# ORDER BY num DESC;

# Same approach but, I never used UNION ALL before like this.
# Difference with mine is that I didn't think about JOINING both columns in one and GROUP on it...
# Well, more experience needed.
