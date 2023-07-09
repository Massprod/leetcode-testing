
# SQL schema:
# DROP TABLE IF EXISTS employees, employeeUNI;
# Create table If Not Exists Employees (id int, name varchar(20));
# Create table If Not Exists EmployeeUNI (id int, unique_id int);
# Truncate table Employees;
# insert into Employees (id, name) values ('1', 'Alice');
# insert into Employees (id, name) values ('7', 'Bob');
# insert into Employees (id, name) values ('11', 'Meir');
# insert into Employees (id, name) values ('90', 'Winston');
# insert into Employees (id, name) values ('3', 'Jonathan');
# Truncate table EmployeeUNI;
# insert into EmployeeUNI (id, unique_id) values ('3', '1');
# insert into EmployeeUNI (id, unique_id) values ('11', '2');
# insert into EmployeeUNI (id, unique_id) values ('90', '3');
# ----------------------
# Show the unique ID of each user, If a user does not have a unique ID replace just show null.
# Return the result table in any order.

# SQL query:
# SELECT e1.unique_id, e2.name
# FROM employeeuni AS e1
# RIGHT JOIN employees AS e2 ON e2.id = e1.id;
