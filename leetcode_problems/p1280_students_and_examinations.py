
# Table: Students
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | student_id    | int     |
# | student_name  | varchar |
# +---------------+---------+
# student_id is the primary key for this table.
# Each row of this table contains the ID and the name of one student in the school.

# Table: Subjects
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | subject_name | varchar |
# +--------------+---------+
# subject_name is the primary key for this table.
# Each row of this table contains the name of one subject in the school.

# Table: Examinations
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | student_id   | int     |
# | subject_name | varchar |
# +--------------+---------+
# There is no primary key for this table. It may contain duplicates.
# Each student from the Students table takes every course from the Subjects table.
# Each row of this table indicates that a student with ID student_id attended the exam of subject_name.
# -------------------------
# Find the number of times each student attended each exam.
# Return the result table ordered by student_id and subject_name.


# SQL schema:
# DROP TABLE IF EXISTS students, subjects, examinations;
# Create table If Not Exists Students (student_id int, student_name varchar(20));
# Create table If Not Exists Subjects (subject_name varchar(20));
# Create table If Not Exists Examinations (student_id int, subject_name varchar(20));
# Truncate table Students;
# insert into Students (student_id, student_name) values ('1', 'Alice');
# insert into Students (student_id, student_name) values ('2', 'Bob');
# insert into Students (student_id, student_name) values ('13', 'John');
# insert into Students (student_id, student_name) values ('6', 'Alex');
# Truncate table Subjects;
# insert into Subjects (subject_name) values ('Math');
# insert into Subjects (subject_name) values ('Physics');
# insert into Subjects (subject_name) values ('Programming');
# Truncate table Examinations;
# insert into Examinations (student_id, subject_name) values ('1', 'Math');
# insert into Examinations (student_id, subject_name) values ('1', 'Physics');
# insert into Examinations (student_id, subject_name) values ('1', 'Programming');
# insert into Examinations (student_id, subject_name) values ('2', 'Programming');
# insert into Examinations (student_id, subject_name) values ('1', 'Physics');
# insert into Examinations (student_id, subject_name) values ('1', 'Math');
# insert into Examinations (student_id, subject_name) values ('13', 'Math');
# insert into Examinations (student_id, subject_name) values ('13', 'Programming');
# insert into Examinations (student_id, subject_name) values ('13', 'Physics');
# insert into Examinations (student_id, subject_name) values ('2', 'Math');
# insert into Examinations (student_id, subject_name) values ('1', 'Math');

# SQL query:
# SELECT
# e3.student_id,
# e3.student_name,
# e4.subject_name,
# CASE
# 	-- combo of student_id and subject_name present in examinations --
#   WHEN (e3.student_id, e4.subject_name) IN (SELECT * FROM examinations)
# 	THEN (SELECT COUNT(*) FROM examinations AS e5
#         WHERE (e3.student_id, e4.subject_name) = (e5.student_id, e5.subject_name)
#         )
# 	-- not present --
# 	ELSE 0
# 	END AS attended_exams
# FROM Students AS e3
# CROSS JOIN Subjects AS e4
# GROUP BY e3.student_id, e3.student_name, e4.subject_name
# ORDER BY student_id;
# -------------------------
# It's fun how this is EASY task, because if you don't know about cross JOIN there's a BIG PROBLEM.
# Because there's no way to check if sm1 attended exam without CROSS JOIN students and subjects.

# Expected output:
# +------------+--------------+--------------+----------------+
# | student_id | student_name | subject_name | attended_exams |
# +------------+--------------+--------------+----------------+
# | 1          | Alice        | Math         | 3              |
# | 1          | Alice        | Physics      | 2              |
# | 1          | Alice        | Programming  | 1              |
# | 2          | Bob          | Math         | 1              |
# | 2          | Bob          | Physics      | 0              |
# | 2          | Bob          | Programming  | 1              |
# | 6          | Alex         | Math         | 0              |
# | 6          | Alex         | Physics      | 0              |
# | 6          | Alex         | Programming  | 0              |
# | 13         | John         | Math         | 1              |
# | 13         | John         | Physics      | 1              |
# | 13         | John         | Programming  | 1              |
# +------------+--------------+--------------+----------------+
