
# Table: Employee
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | empId       | int     |
# | name        | varchar |
# | supervisor  | int     |
# | salary      | int     |
# +-------------+---------+
# empId is the primary key column for this table.
# Each row of this table indicates the name and the ID of an employee in addition to their salary
#   and the id of their manager.
#
# Table: Bonus
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | empId       | int  |
# | bonus       | int  |
# +-------------+------+
# empId is the primary key column for this table.
# empId is a foreign key to empId from the Employee table.
# Each row of this table contains the id of an employee and their respective bonus.
# -----------------------
# Write an SQL query to report the name and bonus amount of each employee with a bonus less than 1000.
# Return the result table in any order.

postgresql_query: str = "SELECT e1.name, e2.bonus " \
                        "FROM employee AS e1 " \
                        "LEFT JOIN bonus AS e2 ON e1.empId = e2.empId " \
                        "WHERE e2.bonus < 1000 OR e2.bonus IS NULL;"

# Testing this in PgAdmin, no reason to execute it here, because now I'm not creating tables and inserting there.
# Because tables have same names and most of the time overrides each other.
