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
# Each row of this table indicates the ID of a department and its name.

# A company's executives are interested in seeing who earns the most money
#   in each of the company's departments.
# A high earner in a department is an employee who has a salary
#   in the top three unique salaries for that department.
# Write an SQL query to find the employees who are high earners in each of the departments.
# Return the result table in any order.
# -------------------

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
        "   name VARCHAR(200),"
        "   salary INTEGER,"
        "   departmentId int,"
        "   CONSTRAINT departmentId"
        "       FOREIGN KEY(departmentId)"
        "       REFERENCES department(id)"
        "       ON DELETE SET NULL "
        ");"
    )
)
db.execute(
    text(
        "INSERT INTO department(name)"
        "VALUES"
        "('IT'),"
        "('Sales');"
    )
)
db.commit()
db.execute(
    text(
        "INSERT INTO employee(name, salary, departmentId)"
        "VALUES"
        "('Joe', 85000, 1),"
        "('Henry', 80000, 2),"
        "('Sam', 60000, 2),"
        "('Max', 90000, 1),"
        "('Janet', 69000, 1),"
        "('Randy', 85000, 1),"
        "('Will', 70000, 1);"
    )
)
db.commit()


# Ok. After p184 searched for normal_solution, and it can be done with rank().
# In this case we just need to group ranks by departments which can be done with PARTITION BY.
# Same can be used on p184, just with dense_rank = 1, instead of my frankenstein_type solution.
# But w.e, good experience on CONCAT anyway.


data: Result = db.execute(
    text(
        "SELECT "
        "Department, "
        "Employee, "
        "Salary "
        "FROM ("
        "   SELECT"
        "   e2.name AS Department,"
        "   e1.name AS Employee,"
        "   e1.salary AS Salary,"
        "   DENSE_RANK() OVER("
        "       PARTITION BY e1.departmentId"
        "       ORDER BY e1.salary DESC) AS dense_rank"
        "   FROM employee AS e1"
        "   JOIN department AS e2 ON e2.id = e1.departmentId"
        ") AS no_name "
        "WHERE dense_rank <= 3;"
    )
)
test_out: set[str] = {'Max', 'Joe', 'Randy', 'Will', 'Henry', 'Sam'}
count: int = 0
for _ in data:
    print(_)
    assert _[1] in test_out
    count += 1
assert count == len(test_out)
