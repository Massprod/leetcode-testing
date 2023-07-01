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