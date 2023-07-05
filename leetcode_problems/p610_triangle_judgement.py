from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from tasks_database.db import get_session


# Table: Triangle
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | x           | int  |
# | y           | int  |
# | z           | int  |
# +-------------+------+
# (x, y, z) is the primary key column for this table.
# Each row of this table contains the lengths of three line segments.
# ----------------------
# Write an SQL query to report for every three line segments whether they can form a triangle.
# Return the result table in any order.


# SQL schema:
# DROP TABLE IF EXISTS triangle;
# Create table If Not Exists Triangle (x int, y int, z int);
# Truncate table Triangle;
# insert into Triangle (x, y, z) values ('13', '15', '30');
# insert into Triangle (x, y, z) values ('10', '20', '15');

# To determine whether three line segments can form a triangle, we need to apply the triangle inequality theorem.
# According to the theorem, for any three line segments with lengths a, b, and c,
#   they can form a triangle if and only if the sum of the lengths of any two sides
#   is greater than the length of the third side.

db: Session = next(get_session())
db.execute(
    text(
        "DROP TABLE IF EXISTS triangle;"
        "CREATE TABLE triangle("
        "   x INTEGER,"
        "   y INTEGER,"
        "   z INTEGER"
        ");"
        "INSERT INTO triangle (x, y, z) "
        "VALUES "
        "(13, 15, 30),"
        "(10, 20, 15);"
    )
)
db.commit()

# SQL query:
# SELECT x, y, z,
# 	CASE
# 		WHEN x + y > z
# 			AND
# 			x + z > y
# 			AND
# 			y + z > x
# 			THEN 'Yes'
# 		ELSE 'No'
# 		END AS triangle
# FROM triangle;

data: Result = db.execute(
    text(
        "SELECT x, y, z,"
        "   CASE"
        "       WHEN x + y > z "
        "           AND "
        "           x + z > y "
        "           AND "
        "           y + z > x "
        "           THEN 'Yes' "
        "       ELSE 'No'"
        "       END AS triangle "
        "FROM triangle;"
    )
)

for _ in data:
    print(_)

# Expected output:
# +----+----+----+----------+
# | x  | y  | z  | triangle |
# +----+----+----+----------+
# | 13 | 15 | 30 | No       |
# | 10 | 20 | 15 | Yes      |
# +----+----+----+----------+
