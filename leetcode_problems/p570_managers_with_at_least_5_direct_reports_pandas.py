import pandas as pd


# Write a solution to find managers with at least five direct reports.
# Return the result table in any order.
# ----------------------
# Employee table:
# +-----+-------+------------+-----------+
# | id  | name  | department | managerId |
# +-----+-------+------------+-----------+
# | 101 | John  | A          | None      |
# | 102 | Dan   | A          | 101       |
# | 103 | James | A          | 101       |
# | 104 | Amy   | A          | 101       |
# | 105 | Anne  | A          | 101       |
# | 106 | Ron   | B          | 101       |
# +-----+-------+------------+-----------+
# Output:
# +------+
# | name |
# +------+
# | John |
# +------+


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # Count occurrences of every unique managerId ->
    count: pd.DataFrame = employee.groupby(by=['managerId']).nunique()
    # -> LEFT JOIN count with employee to delete everything except managerId == id.
    employee = count.merge(employee, left_on='managerId', right_on='id', how='left')
    # Filter to leave only >= 5 reports.
    employee = employee[employee['id_x'] >= 5]
    employee = employee[['id_y', 'name_y']]
    # We can have managers with >= 5 reports, but they're not present.
    # Changed to LEFT JOIN, so it's extra dropna()
    employee.dropna(inplace=True)
    employee.rename(
        columns={
            'name_y': 'name',
        },
        inplace=True,
    )
    return employee[['name']]
