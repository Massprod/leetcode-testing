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
# | salary      | int     |
# | managerId   | int     |
# +-------------+---------+
# id is the primary key column for this table.
# Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.
# -------------------------
# Write an SQL query to find the employees who earn more than their managers.
# Return the result table in any order.

db: Session = next(get_session())
db.execute(
    text(
        "DROP TABLE IF EXISTS employee;"
    )
)
db.commit()
db.execute(
    text(
        "CREATE TABLE employee("
        "   id SERIAL PRIMARY KEY,"
        "   name VARCHAR(50) NOT NULL,"
        "   salary INTEGER NOT NULL,"
        "   managerId INTEGER"
        ");"
    )
)
db.commit()
db.execute(
    text(
        "INSERT INTO employee(name, salary, managerId) "
        "VALUES "
        "('Joe', 70000, 3),"
        "('Henry', 80000, 4),"
        "('Sam', 60000, Null),"
        "('Max', 90000, Null),"
        "('Kim', 80000, 3),"
        "('Tra', 100000, 4);"
    )
)
db.commit()

# Most basic JOIN with WHERE clause.

test_data: set[str] = {"Joe", "Kim", "Tra"}
data: Result = db.execute(
    text(
        "SELECT e1.name AS employee "
        "FROM employee AS e1 "
        "JOIN employee AS e2 ON e1.managerId = e2.id "
        "WHERE e1.salary > e2.salary;"
    )
)
count: int = 0
for _ in data:
    assert _[0] in test_data
    count += 1
assert len(test_data) == count
