
# SQL schema:
# DROP TABLE IF EXISTS employees;
# Create table If Not Exists Employees(emp_id int, event_day date, in_time int, out_time int);
# Truncate table Employees;
# insert into Employees (emp_id, event_day, in_time, out_time) values ('1', '2020-11-28', '4', '32');
# insert into Employees (emp_id, event_day, in_time, out_time) values ('1', '2020-11-28', '55', '200');
# insert into Employees (emp_id, event_day, in_time, out_time) values ('1', '2020-12-3', '1', '42');
# insert into Employees (emp_id, event_day, in_time, out_time) values ('2', '2020-11-28', '3', '33');
# insert into Employees (emp_id, event_day, in_time, out_time) values ('2', '2020-12-9', '47', '74');
# ------------------------
# Calculate the total time in minutes spent by each employee on each day at the office.
# Note that within one day, an employee can enter and leave more than once.
# The time spent in the office for a single entry is out_time - in_time.
# Return the result table in any order.

# SQL query:
# SELECT
# event_day AS day,
# emp_id,
# SUM(out_time) - SUM(in_time) AS total_time
# FROM employees
# GROUP BY day, emp_id
# ORDER BY day;
