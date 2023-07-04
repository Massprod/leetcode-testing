from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from tasks_database.db import get_session


# Table: Courses
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | student     | varchar |
# | class       | varchar |
# +-------------+---------+
# (student, class) is the primary key column for this table.
# Each row of this table indicates the name of a student and the class in which they are enrolled.
# -------------------------
# Find all the classes that have at least five students.
# Return the result table in any order.

# SQL schema:
# DROP TABLE IF EXISTS courses;
# Create table Courses (student varchar(255), class varchar(255));
# insert into Courses (student, class) values ('A', 'Math');
# insert into Courses (student, class) values ('B', 'English');
# insert into Courses (student, class) values ('C', 'Math');
# insert into Courses (student, class) values ('D', 'Biology');
# insert into Courses (student, class) values ('E', 'Math');
# insert into Courses (student, class) values ('F', 'Computer');
# insert into Courses (student, class) values ('G', 'Math');
# insert into Courses (student, class) values ('H', 'Math');
# insert into Courses (student, class) values ('I', 'Math');

db: Session = next(get_session())
db.execute(
    text(
        "DROP TABLE IF EXISTS courses;"
        "CREATE TABLE courses ("
        "student VARCHAR(255),"
        "class VARCHAR(255)"
        ");"
        "INSERT INTO courses (student, class) "
        "VALUES "
        "('A', 'Math'),"
        "('B', 'English'),"
        "('C', 'Math'),"
        "('D', 'Biology'),"
        "('E', 'Math'),"
        "('F', 'Computer'),"
        "('G', 'Math'),"
        "('H', 'Math'),"
        "('I', 'Math');"
    )
)
db.commit()

# Query:
# SELECT class
# FROM courses
# GROUP BY class
# HAVING COUNT(student) >= 5;

postgresql_query: str = "SELECT class " \
                        "FROM courses " \
                        "GROUP BY class " \
                        "HAVING COUNT(student) >= 5;"
data: Result = db.execute(text(postgresql_query))
for _ in data:
    print(_)

# Expected output:
# +---------+
# | class   |
# +---------+
# | Math    |
# +---------+
