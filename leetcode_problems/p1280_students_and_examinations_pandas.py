import pandas as pd


# Write a solution to find the number of times each student attended each exam.
# Return the result table ordered by student_id and subject_name.
# ---------------
# Output:
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


def students_and_examinations(students: pd.DataFrame,
                              subjects: pd.DataFrame,
                              examinations: pd.DataFrame) -> pd.DataFrame:
    # GroupBy all unique pairs of (student_id + subject_name) ->
    examinations = examinations.groupby(by=['student_id', 'subject_name'])
    # -> create new column 'attended_exams' and populate with count of all unique pairs.
    examinations = examinations.agg(attended_exams=('student_id', 'count'))
    # Reset indexing after aggregate.
    examinations = examinations.reset_index()
    # CROSS JOIN students and subjects ->
    students = students.merge(subjects, how='cross')
    # -> LEFT JOIN to get counts into a students table.
    students = students.merge(
        examinations,
        left_on=['student_id', 'subject_name'],
        right_on=['student_id', 'subject_name'],
        how='left'
    )
    # Fill Nulls with 0, we're only having Nulls on not attended_exams.
    students.fillna(0, inplace=True)
    # ! Return the result table ordered by student_id and subject_name !
    students.sort_values(by=['student_id', 'subject_name'], inplace=True)
    return students[['student_id', 'student_name', 'subject_name', 'attended_exams']]
