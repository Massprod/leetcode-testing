
# SQL schema:
# DROP TABLE IF EXISTS employees, salaries;
# Create table If Not Exists Employees (employee_id int, name varchar(30));
# Create table If Not Exists Salaries (employee_id int, salary int);
# Truncate table Employees;
# insert into Employees (employee_id, name) values ('2', 'Crew');
# insert into Employees (employee_id, name) values ('4', 'Haven');
# insert into Employees (employee_id, name) values ('5', 'Kristian');
# Truncate table Salaries;
# insert into Salaries (employee_id, salary) values ('5', '76071');
# insert into Salaries (employee_id, salary) values ('1', '22517');
# insert into Salaries (employee_id, salary) values ('4', '63539');
# -------------------
# Write an SQL query to report the IDs of all the employees with missing information.
# The information of an employee is missing if:
#   1) The employee's name is missing, or
#   2) The employee's salary is missing.
# Return the result table ordered by employee_id in ascending order.

# PostgreSQL query:
# SELECT
# -- combine 2 columns with missed employees --
# CASE WHEN e1.employee_id IS Null THEN e2.employee_id
# 	   WHEN e2.employee_id IS Null THEN e1.employee_id
# 	   END AS employee_id
# -- all missing employees from both tables --
# FROM employees AS e1
# FULL OUTER JOIN salaries AS e2 ON e2.employee_id = e1.employee_id
# WHERE e1.employee_id IS Null OR e2.employee_id IS Null;
# -------------------
# ^^First made this solution, and it's correct. But MySQL doesn't support FULL OUTER JOIN.
# So we need to filter salaries and employees one by one and UNION after.
# -------------------
# SQL query:
# -- all employees missed from salaries --
# SELECT e1.employee_id
# FROM employees AS e1
# LEFT JOIN salaries AS e2 ON e1.employee_id = e2.employee_id
# WHERE e2.employee_id IS NULL
# UNION
# -- all employees missed from employees_table --
# SELECT e4.employee_id
# FROM employees AS e3
# RIGHT JOIN salaries AS e4 ON e3.employee_id = e4.employee_id
# WHERE e3.employee_id IS NULL
# ORDER BY employee_id;
