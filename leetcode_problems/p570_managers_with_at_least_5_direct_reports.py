from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from tasks_database.db import get_session


# Table: Employee
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# | department  | varchar |
# | managerId   | int     |
# +-------------+---------+
# id is the primary key column for this table.
# Each row of this table indicates the name of an employee, their department, and the id of their manager.
# If managerId is null, then the employee does not have a manager.
# No employee will be the manager of themselves.
# ------------------------
# Find the managers with at least five direct reports.
# Return the result table in any order.

# I'm actually done with this style of solution, it's too long and ineffective to use it in every case.
# So I will just ust PgAdmin to create tables, and Insert data by Leetcode schemas and after that,
# just paste here correct solution if I don't need to extra search and explain something hard.
# It was needed for me to practice execute() after bootcamp, but now it's too much.

postgresql_query: str = "SELECT name " \
                        "FROM employee " \
                        "WHERE id IN (" \
                        "   SELECT managerId " \
                        "   FROM employee " \
                        "   GROUP BY managerId " \
                        "   HAVING COUNT(managerId) >=5 " \
                        ");"
db: Session = next(get_session())
data: Result = db.execute(text(postgresql_query))
for _ in data:
    print(_)

# Correct output:
# +------+
# | name |
# +------+
# | John |
# +------+
