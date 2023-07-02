from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from tasks_database.db import get_session


# Table: Employee
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | id           | int     |
# | name         | varchar |
# | salary       | int     |
# | departmentId | int     |
# +--------------+---------+
# id is the primary key column for this table.
# departmentId is a foreign key of the ID from the Department table.
# Each row of this table indicates the ID, name, and salary of an employee.
# It also contains the ID of their department.

# Table: Department
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# +-------------+---------+
# id is the primary key column for this table.
# It is guaranteed that department name is not NULL.
# Each row of this table indicates the ID of a department and its name.
# -------------------------
# Write an SQL query to find employees who have the highest salary in each of the departments.
# Return the result table in any order.

db: Session = next(get_session())
db.execute(
    text(
        "DROP TABLE IF EXISTS employee, department;"
    )
)
db.commit()
db.execute(
    text(
        "CREATE TABLE department("
        "   id SERIAL PRIMARY KEY,"
        "   name VARCHAR(100) NOT NULL"
        ");"
    )
)
db.commit()
db.execute(
    text(
        "CREATE TABLE employee("
        "   id SERIAL PRIMARY KEY,"
        "   name VARCHAR(100),"
        "   salary INTEGER,"
        "   departmentId INTEGER,"
        "   CONSTRAINT departmentId"
        "       FOREIGN KEY(departmentId)"
        "       REFERENCES department(id)"
        "       ON DELETE SET NULL"
        ");"
    )
)
db.commit()
db.execute(
    text(
        "INSERT INTO department(name)"
        "VALUES"
        "('IT'),"
        "('HR');"
    )
)
db.execute(
    text(
        "INSERT INTO employee(name, salary, departmentId)"
        "VALUES"
        "('Joe', 60000, 1),"
        "('Sam', 50000, 1),"
        "('Max', 50000, 2);"
    )
)
db.commit()


# I know how to take MAX() from some department, but what about every department?
# Guess we can group them, but on what?
# Take max() from salaries and group on departmentId, and filter on this?
# Should be correct.
# -------------------------
# Failed. Didn't considered that we can have same max(salary) in different departments,
# and because we're just checking IN we're going to have lower than max(salary) in other department.
# Ok. We can't use SUMM of them to filter -> e1.salary + e1.departmentId.
# -------------------------
# Failed to come up with more pretty/correct solution.
# But it's working, and with my 2 days experience on SQL. It's fine for now.
# Same approach as before we're making a SUMM, but as a STRING with max_salary and id of a department.
# It's always going to be unique, so I don't see how it can be Incorrect.
# But what if our salary is 1000000000000000000, in theory it possible that salary can have more digits
# than we set limit to our string while using CONVERT(). But if we're using CONCAT this shouldn't be a problem.
# Leaving it with CONCAT() and this approach, maybe Google when I need it to be more pretty, but not now.


data: Result = db.execute(
    text(
        "SELECT "
        "e2.name AS Department,"
        "e1.name AS Employee,"
        "e1.salary AS salary "
        "FROM employee AS e1 "
        "JOIN department AS e2 ON e2.id = e1.departmentId "
        "WHERE CONCAT(e1.salary, ' ', departmentId) IN ("
        "   SELECT CONCAT(MAX(salary), ' ', departmentId) AS gro "
        "   FROM employee "
        "   GROUP BY departmentId "
        ")"
        ";"
    )
)

for _ in data:
    print(_)
