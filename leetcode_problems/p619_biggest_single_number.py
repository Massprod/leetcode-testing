
# Table: MyNumbers
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | num         | int  |
# +-------------+------+
# There is no primary key for this table. It may contain duplicates.
# Each row of this table contains an integer.
# ----------------------
# A single number is a number that appeared only once in the MyNumbers table.
# Write an SQL query to report the largest single number.
# If there is no single number, report null.


# SQL schema:
# DROP TABLE IS EXISTS mynumbers;
# Create table If Not Exists MyNumbers (num int);
# Truncate table MyNumbers;
# insert into MyNumbers (num) values ('8');
# insert into MyNumbers (num) values ('8');
# insert into MyNumbers (num) values ('3');
# insert into MyNumbers (num) values ('3');
# insert into MyNumbers (num) values ('1');
# insert into MyNumbers (num) values ('4');
# insert into MyNumbers (num) values ('5');
# insert into MyNumbers (num) values ('6');

# SQL query:
# SELECT MAX(num) AS num
# FROM (
#   SELECT num, COUNT(num) AS count
#   FROM mynumbers
#   GROUP BY num
#   ORDER BY COUNT(num)) AS test
# WHERE count = 1;

# Too easy to do solution_style.
