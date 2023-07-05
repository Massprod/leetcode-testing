
# Table: Salary
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | id          | int      |
# | name        | varchar  |
# | sex         | ENUM     |
# | salary      | int      |
# +-------------+----------+
# id is the primary key for this table.
# The sex column is ENUM value of type ('m', 'f').
# The table contains information about an employee.
# --------------------------
# Write an SQL query to swap all 'f' and 'm' values (i.e., change all 'f' values to 'm' and vice versa)
#   with a single update statement and no intermediate temporary tables.
# Note that you must write a single update statement,
#   do not write any select statement for this problem.

# SQL schema:
# DROP TABLE IF EXISTS salary;
# Create table If Not Exists Salary (id int, name varchar(100), sex char(1), salary int);
# insert into Salary (id, name, sex, salary) values ('1', 'A', 'm', '2500');
# insert into Salary (id, name, sex, salary) values ('2', 'B', 'f', '1500');
# insert into Salary (id, name, sex, salary) values ('3', 'C', 'm', '5500');
# insert into Salary (id, name, sex, salary) values ('4', 'D', 'f', '500');

# SQL query:
# UPDATE salary
# SET sex = CASE
#           WHEN sex = 'm' THEN 'f'
#           WHEN sex = 'f' THEN 'm'
#           END;
