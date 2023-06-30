from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from tasks_database.db import get_session

# Table: Employee
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | salary      | int  |
# +-------------+------+
# id is the primary key column for this table.
# Each row of this table contains information about the salary of an employee.
# --------------------------
# Write an SQL query to report the nth highest salary from the Employee table.
# If there is no nth highest salary, the query should report null.


db: Session = next(get_session())
db.execute(
    text(
        "DROP TABLE IF EXISTS employee;"
    )
)
db.execute(
    text(
        "CREATE TABLE employee("
        "   id SERIAL PRIMARY KEY,"
        "   salary INTEGER"
        ");"
    )
)
db.commit()

db.execute(
    text(
        "INSERT INTO employee(salary)"
        "VALUES"
        "(100),"
        "(200),"
        "(300);"
    )
)
db.commit()

# Ok. First encounter with SQL functions.
# First of all we need to set values we will use in RETURN()
# Because SQL doesn't allow any arithmetics in RETURN()
# And we can use OFFSET with MYSQL, just not in PostgreSQL way, at least like I tried before.
# LIMIT *OFFSET_ROWS*, *LIMIT_ROWS* <- like this.

# Correct query for MySQL and Leetcode.
mysql_query: str = \
    "CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT " \
    "BEGIN " \
    " DECLARE F INT;" \
    " SET F = N - 1;" \
    "  RETURN (" \
    "      SELECT DISTINCT salary" \
    "      FROM employee" \
    "      ORDER BY salary DESC" \
    "      LIMIT F, 1" \
    ");" \
    "END"

# Correct query for PostgreSQL.
postgresql_query: str = \
    "CREATE FUNCTION getNthHighestSalary (N INT) " \
    "RETURNS INT " \
    "LANGUAGE plpgsql " \
    "AS " \
    "$$" \
    "DECLARE F INT := N - 1;" \
    "BEGIN" \
    "   RETURN (" \
    "       SELECT DISTINCT salary " \
    "       FROM employee" \
    "       ORDER BY salary DESC" \
    "       LIMIT 1" \
    "       OFFSET F" \
    "   );" \
    "END;" \
    "$$;"

# Only problem with that was, that I'm currently using PostgreSql as my local_db_practice,
# and leetcode is MySQL. So it's better to made MySQL and practice with that.
# But in the meantime why not practice both and see differences?

db.execute(
    text(
        "DROP FUNCTION IF EXISTS getnthhighestsalary;"
    )
)
db.commit()
db.execute(text(postgresql_query))
db.commit()
data: Result = db.execute(
    text(
        "SELECT getNthHighestSalary(3);"
    )
)

for _ in data:
    assert _[0] == 100

data = db.execute(
    text(
        "SELECT getnthhighestsalary(10);"
    )
)

for _ in data:
    assert _[0] is None
