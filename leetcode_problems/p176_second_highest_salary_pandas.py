import pandas as pd


# Write a solution to find the second highest salary from the Employee table.
# If there is no second highest salary, return null (return None in Pandas).


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Remove duplicates.
    employee = employee.drop_duplicates(subset='salary')
    # Sort, cuz we're not given data on column.
    employee.sort_values(by='salary', inplace=True, ascending=False)
    # Rename for correct output.
    employee.rename(
        inplace=True,
        columns={
            'salary': 'SecondHighestSalary',
        }
    )
    # If there's less than 2 values, we can't record SECOND.
    if len(employee.index) >= 2:
        return employee[['SecondHighestSalary']].iloc[1:2]
    employee['SecondHighestSalary'][0] = None
    return employee[['SecondHighestSalary']].iloc[:1]


# Failed commit, again forgot to set SUBSET in drop_duplicates()...
# It's not DISTINCT and always need's to be set with correct column to delete from.
# Actually DISTINCT is the same, but we're selecting column by default and there it's need to be done explicitly.
