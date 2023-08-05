import pandas as pd


# Write a solution to find all the classes that have at least five students.
# Return the result table in any order.
# ------------------
# Courses table:
# +---------+----------+
# | student | class    |
# +---------+----------+
# | A       | Math     |
# | B       | English  |
# | C       | Math     |
# | D       | Biology  |
# | E       | Math     |
# | F       | Computer |
# | G       | Math     |
# | H       | Math     |
# | I       | Math     |
# +---------+----------+
# Output:
# +---------+
# | class   |
# +---------+
# | Math    |
# +---------+


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # Count every unique combination -> class + student
    courses['count'] = courses.groupby(by=['class'])['student'].transform('count')
    # Filter any class with less than 5 students.
    courses = courses[(courses['count'] >= 5)]
    # Delete duplicates.
    courses.drop_duplicates(subset='class', inplace=True)
    return courses[['class']]
