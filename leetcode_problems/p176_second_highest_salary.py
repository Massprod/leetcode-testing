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
# ------------------------
# Write an SQL query to report the second highest salary from the Employee table.
# If there is no second highest salary, the query should report null.
# The query result format is in the following example.

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

# query with DENSE_RANK()
data: Result = db.execute(
    text(
        "SELECT min(salary) AS SecondHighestSalary "
        "FROM ("
        "   SELECT salary, dense_rank() over(ORDER BY salary DESC) as r "
        "   FROM employee "
        ") as p "
        "WHERE r = 2;"
    )
)

for _ in data:
    assert _[0] == 200

# There's a lot of way to do this.
# can be done with dense_rank() -> https://learnsql.com/blog/how-to-rank-rows-sql/
# or with FETCH -> https://www.sqlservertutorial.net/sql-server-basics/sql-server-offset-fetch/
# Prefer FETCH is simplier and more readable.
# The trick in a task is to return Null, because we're getting empty result column in both cases.
# To get Null instead of empty column, we need to EXTRA SELECT or take MIN(), MAX() from result.
# Then if there's value it will return it, if there's empty column MIN(), MAX() gives Null and SELECT too.
# But query with FETCH doesn't work with MySQL and this is what Leetcode uses.

# query with FETCH
data = db.execute(
    text(
        "SELECT("
        "   SELECT DISTINCT salary"
        "   FROM employee"
        "   ORDER BY salary DESC"
        "   OFFSET 1"
        "   FETCH NEXT 1 ROW ONLY"
        ") as SecondHighestSalary;"
    )
)

for _ in data:
    assert _[0] == 200

# deleting rows to test Null
db.execute(
    text(
        "DELETE FROM employee "
        "WHERE id IN (1, 2);"
    )
)
db.commit()

# query with FETCH
data = db.execute(
    text(
        "SELECT("
        "   SELECT DISTINCT salary"
        "   FROM employee"
        "   ORDER BY salary DESC"
        "   OFFSET 1"
        "   FETCH NEXT 1 ROW ONLY"
        ") as SecondHighestSalary;"
    )
)

for _ in data:
    assert _[0] is None

# query with DENSE_RANK()
data = db.execute(
    text(
        "SELECT min(salary) as SecondHighestSalary "
        "FROM ("
        "   SELECT "
        "   salary, "
        "   dense_rank() over(ORDER BY salary DESC) as r "
        "   FROM employee"
        ") as p "
        "WHERE r = 2;"
    )
)

for _ in data:
    assert _[0] is None
