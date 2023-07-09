
# SQL schema:
# DROP TABLE IF EXISTS employees;
# Create table If Not Exists Employees (employee_id int, name varchar(20), manager_id int, salary int);
# Truncate table Employees;
# insert into Employees (employee_id, name, manager_id, salary) values ('3', 'Mila', '9', '60301');
# insert into Employees (employee_id, name, manager_id, salary) values ('12', 'Antonella', Null, '31000');
# insert into Employees (employee_id, name, manager_id, salary) values ('13', 'Emery', Null, '67084');
# insert into Employees (employee_id, name, manager_id, salary) values ('1', 'Kalel', '11', '21241');
# insert into Employees (employee_id, name, manager_id, salary) values ('9', 'Mikaela', Null, '50937');
# insert into Employees (employee_id, name, manager_id, salary) values ('11', 'Joziah', '6', '28485');
# ----------------------
# Write an SQL query to report the IDs of the employees whose salary is strictly less than $30000
#   and whose manager left the company.
# When a manager leaves the company, their information is deleted from the Employees table,
#   but the reports still have their manager_id set to the manager that left.
# Return the result table ordered by employee_id.

# SQL query:
# SELECT
# employee_id
# FROM employees
# WHERE
# salary < 30000
# AND
# manager_id NOT IN (SELECT employee_id FROM employees)
# ORDER BY employee_id;
# ----------------------
# Failed commit -> forgot to order, rushed.
