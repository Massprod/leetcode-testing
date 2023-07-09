
# SQL schema:
# DROP TABLE IF EXISTS employees;
# Create table If Not Exists Employees(employee_id int, name varchar(20), reports_to int, age int);
# Truncate table Employees;
# insert into Employees (employee_id, name, reports_to, age) values ('9', 'Hercy', Null, '43');
# insert into Employees (employee_id, name, reports_to, age) values ('6', 'Alice', '9', '41');
# insert into Employees (employee_id, name, reports_to, age) values ('4', 'Bob', '9', '36');
# insert into Employees (employee_id, name, reports_to, age) values ('2', 'Winston', Null, '37');
# -------------------
# For this problem, we will consider a manager an employee who has at least 1 other employee reporting to them.
# Write an SQL query to report the ids and the names of all managers,
#   the number of employees who report directly to them,
#   and the average age of the reports rounded to the nearest integer.
# Return the result table ordered by employee_id.

# PostgreSQL queries:
# SELECT *
# FROM (
# 	SELECT
# 	e1.employee_id,
# 	e1.name,
# 	(SELECT COUNT(e2.reports_to)
# 	 FROM employees AS e2
# 	 WHERE e2.reports_to = e1.employee_id) AS reports_count,
# 	(SELECT ROUND(SUM(e3.age)::decimal / COUNT(e3.employee_id)::decimal, 0)
# 	 FROM employees AS e3
# 	 WHERE e3.reports_to = e1.employee_id) AS average_age
# 	FROM employees AS e1
# 	GROUP BY e1.employee_id, e1.name) AS e4
# WHERE e4.average_age IS NOT Null
# ORDER BY e4.employee_id;
# ----------------------
# Practiced creating columns and rows by extra SELECT.
# But it can be done with simple JOIN:
# SELECT
# e1.employee_id,
# e1.name,
# COUNT(e2.reports_to) AS reports_count,
# ROUND(SUM(e2.age)::decimal/COUNT(e2.age)::decimal, 0) AS average_age
# FROM employees AS e1
# JOIN employees AS e2 ON e2.reports_to = e1.employee_id
# GROUP BY e1.employee_id, e1.name
# ORDER BY e1.employee_id;
