import pandas as pd


# Write a solution to show the unique ID of each user,
#   If a user does not have a unique ID replace just show null.
# Return the result table in any order.
# -----------------
# Employees table:
# +----+----------+
# | id | name     |
# +----+----------+
# | 1  | Alice    |
# | 7  | Bob      |
# | 11 | Meir     |
# | 90 | Winston  |
# | 3  | Jonathan |
# +----+----------+
# EmployeeUNI table:
# +----+-----------+
# | id | unique_id |
# +----+-----------+
# | 3  | 1         |
# | 11 | 2         |
# | 90 | 3         |
# +----+-----------+
# Output:
# +-----------+----------+
# | unique_id | name     |
# +-----------+----------+
# | null      | Alice    |
# | null      | Bob      |
# | 2         | Meir     |
# | 3         | Winston  |
# | 1         | Jonathan |
# +-----------+----------+


def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    # Standard left_join.
    employees = employees.merge(employee_uni, left_on=['id'], right_on=['id'], how='left')
    return employees[['unique_id', 'name']]
