from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from tasks_database.db import get_session


# Table: Stadium
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | visit_date    | date    |
# | people        | int     |
# +---------------+---------+
# visit_date is the primary key for this table.
# Each row of this table contains the visit date and visit id
#   to the stadium with the number of people during the visit.
# No two rows will have the same visit_date, and as the id increases, the dates increase as well.
# ----------------------------
# Write an SQL query to display the records with three or more rows with consecutive id's,
#   and the number of people is greater than or equal to 100 for each.
# Return the result table ordered by visit_date in ascending order.

# SQL schema:
# DROP TABLE IF EXISTS stadium;
# Create table If Not Exists Stadium (id int, visit_date DATE NULL, people int);
# insert into Stadium (id, visit_date, people) values ('1', '2017-01-01', '10');
# insert into Stadium (id, visit_date, people) values ('2', '2017-01-02', '109');
# insert into Stadium (id, visit_date, people) values ('3', '2017-01-03', '150');
# insert into Stadium (id, visit_date, people) values ('4', '2017-01-04', '99');
# insert into Stadium (id, visit_date, people) values ('5', '2017-01-05', '145');
# insert into Stadium (id, visit_date, people) values ('6', '2017-01-06', '1455');
# insert into Stadium (id, visit_date, people) values ('7', '2017-01-07', '199');
# insert into Stadium (id, visit_date, people) values ('8', '2017-01-09', '188');


# Query:
# SELECT DISTINCT e1.id, e1.visit_date, e1.people
# FROM stadium AS e1, stadium AS e2, stadium AS e3
# WHERE
# e1.people >= 100
# AND
# e2.people >= 100
# AND
# e3.people >= 100
# AND
# (
# (e1.id - e2.id = 1 AND e1.id - e3.id = 2 AND e2.id - e3.id = 1)
# OR
# (e2.id - e1.id = 1 AND e2.id - e3.id = 2 AND e1.id - e3.id = 1)
# OR
# (e3.id - e1.id = 1 AND e3.id - e2.id = 2 AND e1.id - e2.id = 1)
# OR
# (e3.id - e2.id = 1 AND e3.id - e1.id = 2 AND e2.id - e1.id = 1)
# )
# ORDER BY e1.visit_date;

# Used GPT to help me with this one, and I couldn't come up with solution by myself.
# Because I didn't even know we can use multiple OR statements like a list of options in AND.
# Actually simple task if I knew how to use this AND correctly and after that we can just use a list of
# all options with consecutive IDs.
# Options like -> 1, 2, 3 | 3, 2, 1 | 3, 1, 2 | 2, 1, 3

db: Session = next(get_session())
db.execute(
    text(
        "DROP TABLE IF EXISTS stadium; "
        "CREATE TABLE stadium ("
        "   id INTEGER,"
        "   visit_date DATE,"
        "   people INTEGER"
        ");"
        "INSERT INTO stadium(id, visit_date, people)"
        "VALUES"
        "('1', '2017-01-01', '10'),"
        "('2', '2017-01-02', '109'),"
        "('3', '2017-01-03', '150'),"
        "('4', '2017-01-04', '99'),"
        "('5', '2017-01-05', '145'),"
        "('6', '2017-01-06', '1455'),"
        "('7', '2017-01-07', '199'),"
        "('8', '2017-01-09', '188');"
    )
)
db.commit()

data: Result = db.execute(
    text(
        "SELECT DISTINCT e1.id, e1.visit_date, e1.people "
        "FROM "
        "stadium AS e1,"
        "stadium AS e2,"
        "stadium AS e3 "
        "WHERE "
        "e1.people >= 100 "
        "AND "
        "e2.people >= 100 "
        "AND "
        "e3.people >= 100 "
        "AND "
        "("
        "(e1.id - e2.id = 1 AND e1.id - e3.id = 2 AND e2.id - e3.id = 1 )"
        "OR "
        "(e2.id - e1.id = 1 AND e2.id - e3.id = 2 AND e1.id - e3.id = 1)"
        "OR "
        "(e3.id - e1.id = 1 AND e3.id - e2.id = 2 AND e1.id - e2.id = 1)"
        "OR "
        "(e3.id - e2.id = 1 AND e3.id - e1.id = 2 AND e2.id - e1.id = 1)"
        ")"
        "ORDER BY e1.visit_date;"
    )
)
for _ in data:
    print(_)

# Expected output:
# +------+------------+-----------+
# | id   | visit_date | people    |
# +------+------------+-----------+
# | 5    | 2017-01-05 | 145       |
# | 6    | 2017-01-06 | 1455      |
# | 7    | 2017-01-07 | 199       |
# | 8    | 2017-01-09 | 188       |
# +------+------------+-----------+
