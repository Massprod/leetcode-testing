from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from tasks_database.db import get_session


# Table: Seat
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | student     | varchar |
# +-------------+---------+
# id is the primary key column for this table.
# Each row of this table indicates the name and the ID of a student.
# id is a continuous increment.
# ---------------------------
# Write an SQL query to swap the seat id of every two consecutive students.
# If the number of students is odd, the id of the last student is not swapped.
# Return the result table ordered by id in ascending order.

# SQL schema:
# DROP TABLE IS EXISTS seat;
# Create table If Not Exists Seat (id int, student varchar(255));
# insert into Seat (id, student) values ('1', 'Abbot');
# insert into Seat (id, student) values ('2', 'Doris');
# insert into Seat (id, student) values ('3', 'Emerson');
# insert into Seat (id, student) values ('4', 'Green');
# insert into Seat (id, student) values ('5', 'Jeames');

db: Session = next(get_session())
db.execute(
    text(
        "DROP TABLE IF EXISTS seat; "
        "CREATE TABLE seat("
        "   id INTEGER,"
        "   student VARCHAR(255)"
        ");"
        "INSERT INTO seat (id, student) "
        "VALUES "
        "('1', 'Abbot'),"
        "('2', 'Doris'),"
        "('3', 'Emerson'),"
        "('4', 'Green'),"
        "('5', 'Jeames');"
    )
)
db.commit()

# SQL query:
# SELECT e1.id,
#     CASE
#       WHEN e1.id % 2 = 1 AND e1.id < (SELECT MAX(id) FROM seat) -- id is odd
# 		THEN (
# 			SELECT student
# 			FROM seat
# 			WHERE id = e1.id + 1
# 		)
# 		WHEN e1.id % 2 = 0 AND e1.id < (SELECT MAX(id) FROM seat) -- id is even
# 		THEN (
# 			SELECT student
# 			FROM seat
# 			WHERE id = e1.id - 1
# 		)
# 		WHEN e1.id % 2 = 0 AND e1.id = (SELECT MAX(id) FROM seat) -- last id is not odd
# 		THEN (
# 			SELECT student
# 			FROM seat
# 			WHERE id = e1.id - 1
# 		)
#       -- if last id is odd we don't bother to swap it
# 		ELSE (
# 			SELECT student
# 			FROM seat
# 			WHERE id = e1.id
# 		)
#     END AS student
# FROM seat AS e1;

data: Result = db.execute(
    text(
        "SELECT e1.id, "
        "   CASE "
        "       WHEN e1.id % 2 = 1 AND e1.id < (SELECT MAX(id) FROM seat) "
        "       THEN ("
        "           SELECT student "
        "           FROM seat "
        "           WHERE id = e1.id + 1"
        "       )"
        "       WHEN e1.id % 2 = 0 AND e1.id < (SELECT MAX(id) FROM seat) "
        "       THEN ("
        "           SELECT student "
        "           FROM seat "
        "           WHERE id = e1.id - 1"
        "       )"
        "       WHEN e1.id % 2 = 0 AND e1.id = (SELECT MAX(id) FROM SEAT) "
        "       THEN ("
        "           SELECT student "
        "           FROM seat "
        "           WHERE id = e1.id - 1"
        "       )"
        "       ELSE ("
        "           SELECT student "
        "           FROM seat "
        "           WHERE id = e1.id "
        "       )"
        "   END AS student "
        "FROM seat AS e1;"
    )
)

for _ in data:
    print(_)

# Expected output:
# +----+---------+
# | id | student |
# +----+---------+
# | 1  | Doris   |
# | 2  | Abbot   |
# | 3  | Green   |
# | 4  | Emerson |
# | 5  | Jeames  |
# +----+---------+
