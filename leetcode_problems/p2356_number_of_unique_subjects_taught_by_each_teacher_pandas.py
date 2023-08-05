import pandas as pd


# Write a solution to calculate the number of unique subjects each teacher teaches in the university.
# Return the result table in any order.
# -----------------
# Teacher table:
# +------------+------------+---------+
# | teacher_id | subject_id | dept_id |
# +------------+------------+---------+
# | 1          | 2          | 3       |
# | 1          | 2          | 4       |
# | 1          | 3          | 3       |
# | 2          | 1          | 1       |
# | 2          | 2          | 1       |
# | 2          | 3          | 1       |
# | 2          | 4          | 1       |
# +------------+------------+---------+
# Output:
# +------------+-----+
# | teacher_id | cnt |
# +------------+-----+
# | 1          | 2   |
# | 2          | 4   |
# +------------+-----+


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    # Drop all duplicates, we don't need them ->
    teacher.drop_duplicates(subset=['teacher_id', 'subject_id'], inplace=True)
    # -> count every unique combination of teacher_id + subject_id ->
    teacher['cnt'] = teacher.groupby(by='teacher_id')['subject_id'].transform('count')
    # -> every teacher_id on the same row as cnt, we only need One Id.
    teacher.drop_duplicates(subset=['teacher_id', 'cnt'], inplace=True)
    return teacher[['teacher_id', 'cnt']]
