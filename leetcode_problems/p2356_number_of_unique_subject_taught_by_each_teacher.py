
# SQL schema:
# DROP TABLE IF EXISTS teacher;
# Create table If Not Exists Teacher (teacher_id int, subject_id int, dept_id int);
# Truncate table Teacher;
# insert into Teacher (teacher_id, subject_id, dept_id) values ('1', '2', '3');
# insert into Teacher (teacher_id, subject_id, dept_id) values ('1', '2', '4');
# insert into Teacher (teacher_id, subject_id, dept_id) values ('1', '3', '3');
# insert into Teacher (teacher_id, subject_id, dept_id) values ('2', '1', '1');
# insert into Teacher (teacher_id, subject_id, dept_id) values ('2', '2', '1');
# insert into Teacher (teacher_id, subject_id, dept_id) values ('2', '3', '1');
# insert into Teacher (teacher_id, subject_id, dept_id) values ('2', '4', '1');
# ----------------------------
# Calculate the number of unique subjects each teacher teaches in the university.
# Return the result table in any order.

# SQL query:
# SELECT
# teacher_id,
# COUNT(DISTINCT subject_id) AS cnt
# FROM teacher
# GROUP BY teacher_id;
