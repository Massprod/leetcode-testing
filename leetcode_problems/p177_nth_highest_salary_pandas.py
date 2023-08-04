import pandas as pd


# Write a solution to find the nth highest salary from the Employee table.
# If there is no nth highest salary, return null.
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # No info if original is sorted.
    col_name: str = f'getNthHighestSalary({N})'
    # Sort to take Nth row.
    employee.sort_values(by='salary', ascending=False, inplace=True)
    employee.rename(
        columns={
            'salary': col_name
        },
        inplace=True,
    )
    # Drop duplicates, cuz we need Nth largest, and duplicates will take correct_value place.
    employee.drop_duplicates(subset=[col_name], keep='first', inplace=True)
    # Reset indexes, cuz I'm taking with iloc[] -> which is taking index of DF not column == id.
    employee.reset_index(inplace=True)
    # There's no constraints, but suppose we're not taking 0Nth cuz it should be [1, N].
    if 1 <= N <= len(employee.index):
        # Indexes are zero_indexes => we need -1.
        return employee[[col_name]].iloc[N - 1:N]
    else:
        # Resetting [0] index and returning as None.
        employee[col_name][0] = None
        return employee[[col_name]].iloc[:1]


# Failed commits, cuz didn't correctly understand limits of N and how iloc[] taking values.
