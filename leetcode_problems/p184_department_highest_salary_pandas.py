import pandas as pd


# Write a solution to find employees who have the highest salary in each of the departments.
# Return the result table in any order.
# ------------------
# Employee table:
# +----+-------+--------+--------------+
# | id | name  | salary | departmentId |
# +----+-------+--------+--------------+
# | 1  | Joe   | 70000  | 1            |
# | 2  | Jim   | 90000  | 1            |
# | 3  | Henry | 80000  | 2            |
# | 4  | Sam   | 60000  | 2            |
# | 5  | Max   | 90000  | 1            |
# +----+-------+--------+--------------+
# Department table:
# +----+-------+
# | id | name  |
# +----+-------+
# | 1  | IT    |
# | 2  | Sales |
# +----+-------+


def department_highest_salary(employee: pd.DataFrame,  department: pd.DataFrame) -> pd.DataFrame:
    # LeftJoin department with employee table by id == departmentId.
    department = department.merge(employee, left_on='id', right_on='departmentId', how='left')
    # GroupBy every departmentId with its maximum_salary and transform() original DF
    # to keep correct indexing ->
    max_sal = department.groupby(['departmentId'])['salary'].transform(max)
    # -> cuz we're saving correct indexing of original DF we can now just check
    # where's salaries are equal to maximum values.
    # Correct indexing => every row with maximum_salary is having same departmentId as before,
    # so we're always having correct pair of (max_salary + departmentId).
    # And if salary == max_salary, we're having a match for this row, and department as well.
    department = department[department['salary'] == max_sal]
    # Rename for correct output.
    department.rename(
        columns={
            'name_x': 'Department',
            'name_y': 'Employee',
            'salary': 'Salary',
        },
        inplace=True,
    )
    return department[['Department', 'Employee', 'Salary']]


# Ok. If Join is somewhat similar to SQL and I had no problem with doing this.
# GroupBy is a little bit harder, and took some documentation time. But still a good experience.
# Actually it's only hard, because I'm just not familiar with pandas. First day.
