
# Table: Project
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | project_id  | int     |
# | employee_id | int     |
# +-------------+---------+
# (project_id, employee_id) is the primary key of this table.
# employee_id is a foreign key to Employee table.
# Each row of this table indicates that the employee with employee_id is working on the project with project_id.

# Table: Employee
# +------------------+---------+
# | Column Name      | Type    |
# +------------------+---------+
# | employee_id      | int     |
# | name             | varchar |
# | experience_years | int     |
# +------------------+---------+
# employee_id is the primary key of this table. It's guaranteed that experience_years is not NULL.
# Each row of this table contains information about one employee.
# ------------------------
# Write an SQL query that reports the average experience years of all the employees for each project,
#  rounded to 2 digits.
# Return the result table in any order.


# SQL schema:
# DROP TABLE IF EXISTS project, employee;
# Create table If Not Exists Project (project_id int, employee_id int);
# Create table If Not Exists Employee (employee_id int, name varchar(10), experience_years int);
# Truncate table Project;
# insert into Project (project_id, employee_id) values ('1', '1');
# insert into Project (project_id, employee_id) values ('1', '2');
# insert into Project (project_id, employee_id) values ('1', '3');
# insert into Project (project_id, employee_id) values ('2', '1');
# insert into Project (project_id, employee_id) values ('2', '4');
# Truncate table Employee;
# insert into Employee (employee_id, name, experience_years) values ('1', 'Khaled', '3');
# insert into Employee (employee_id, name, experience_years) values ('2', 'Ali', '2');
# insert into Employee (employee_id, name, experience_years) values ('3', 'John', '1');
# insert into Employee (employee_id, name, experience_years) values ('4', 'Doe', '2');

# SQL query:
# SELECT project_id, ROUND(AVG(experience_years), 2) AS "average_years"
# FROM employee AS e1
# JOIN project AS e2 ON e2.employee_id = e1.employee_id
# GROUP BY project_Id;

# Only problem with that, I couldn't use 'average_years' raising syntax on AS.
# Not a first time encounter, fixes with double_quotes. But why is it even raising if it's works fine in other cases.
# Double quotes, can't even be used in some cases and we need to use single and in cases like this doubles. Hmm.
