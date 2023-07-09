
# SQL schema:
# DROP TYPE IF EXISTS primary_flag_enum;
# CREATE TYPE primary_flag_enum AS ENUM('Y', 'N');
# DROP TABLE IF EXISTS employee;
# Create table If Not Exists Employee (employee_id int, department_id int, primary_flag primary_flag_enum);
# Truncate table Employee;
# insert into Employee (employee_id, department_id, primary_flag) values ('1', '1', 'N');
# insert into Employee (employee_id, department_id, primary_flag) values ('2', '1', 'Y');
# insert into Employee (employee_id, department_id, primary_flag) values ('2', '2', 'N');
# insert into Employee (employee_id, department_id, primary_flag) values ('3', '3', 'N');
# insert into Employee (employee_id, department_id, primary_flag) values ('4', '2', 'N');
# insert into Employee (employee_id, department_id, primary_flag) values ('4', '3', 'Y');
# insert into Employee (employee_id, department_id, primary_flag) values ('4', '4', 'N');
# -------------------------
# Employees can belong to multiple departments. When the employee joins other departments,
#   they need to decide which department is their primary department.
# Note that when an employee belongs to only one department, their primary column is 'N'.
# Write an SQL query to report all the employees with their primary department.
# For employees who belong to one department, report their only department.
# Return the result table in any order.

# SQL query:
# -- all employees with more than 1 and Y as a flag --
# SELECT
# employee_id,
# department_id
# FROM employee
# WHERE
# primary_flag = 'Y'
# GROUP BY employee_id, department_id
# UNION
# SELECT
# employee_id,
# department_id
# FROM employee
# WHERE employee_id IN (
# 	-- all employees with 1 department --
# 	SELECT
# 	employee_id
# 	FROM employee
# 	GROUP BY employee_id
# 	HAVING COUNT(employee_id) = 1)
# ORDER BY employee_id;
# -------------------------
# Dunno why we can't use just GROUP BY and found cases when primary_flag is Y or count is 1.
# But group_by always ask to include primary flag in it, and it's breaks everything.
# Maybe there's a way to do this, but it's still good solution with 70+% speed.
# But might be overcomplicated. W.e
