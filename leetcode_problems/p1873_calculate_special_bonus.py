
# SQL schema:
# DROP TABLE IF EXISTS employees;
# Create table If Not Exists Employees (employee_id int, name varchar(30), salary int);
# Truncate table Employees;
# insert into Employees (employee_id, name, salary) values ('2', 'Meir', '3000');
# insert into Employees (employee_id, name, salary) values ('3', 'Michael', '3800');
# insert into Employees (employee_id, name, salary) values ('7', 'Addilyn', '7400');
# insert into Employees (employee_id, name, salary) values ('8', 'Juan', '6100');
# insert into Employees (employee_id, name, salary) values ('9', 'Kannon', '7700');
# ------------------------
# Calculate the bonus of each employee.
# The bonus of an employee is 100% of their salary if the ID of the employee is an odd number
#   and the employee name does not start with the character 'M'. The bonus of an employee is 0 otherwise.
# Return the result table ordered by employee_id.

# SQL query:
# SELECT
# employee_id,
# CASE WHEN employee_id % 2 = 1
#           -- no info about casesens, consider both --
# 	        AND name NOT LIKE 'M%'
# 	        AND name NOT LIKE 'm%' THEN salary
# 	   ELSE 0
# 	   END AS bonus
# FROM employees
# ORDER BY employee_id;
