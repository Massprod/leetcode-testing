import pandas as pd


# Write a solution to calculate the bonus of each employee.
# The bonus of an employee is 100% of their salary if the ID of the employee is an odd number
#   and the employee's name does not start with the character 'M'.
# The bonus of an employee is 0 otherwise.
# Return the result table ordered by employee_id.
# +-------------+---------+--------+
# | employee_id | name    | salary |
# +-------------+---------+--------+
# | 2           | Meir    | 3000   |
# | 3           | Michael | 3800   |
# | 7           | Addilyn | 7400   |
# | 8           | Juan    | 6100   |
# | 9           | Kannon  | 7700   |
# +-------------+---------+--------+


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # Reverse -> delete everything with 1 of the limits.
    employees.loc[(employees['employee_id'] % 2 == 0) | (employees['name'].str.contains('^M')), 'salary'] = 0
    employees.sort_values(by='employee_id', inplace=True)
    employees.rename(
        columns={
            'salary': 'bonus',
        },
        inplace=True
    )
    return employees[['employee_id', 'bonus']]
