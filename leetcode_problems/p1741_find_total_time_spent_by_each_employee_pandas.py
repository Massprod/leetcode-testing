import pandas as pd


# Write a solution to calculate the total time in minutes spent
#   by each employee on each day at the office.
# Note that within one day, an employee can enter and leave more than once.
# The time spent in the office for a single entry is out_time - in_time.
# Return the result table in any order.
# --------------------
# Employees table:
# +--------+------------+---------+----------+
# | emp_id | event_day  | in_time | out_time |
# +--------+------------+---------+----------+
# | 1      | 2020-11-28 | 4       | 32       |
# | 1      | 2020-11-28 | 55      | 200      |
# | 1      | 2020-12-03 | 1       | 42       |
# | 2      | 2020-11-28 | 3       | 33       |
# | 2      | 2020-12-09 | 47      | 74       |
# +--------+------------+---------+----------+
# Output:
# +------------+--------+------------+
# | day        | emp_id | total_time |
# +------------+--------+------------+
# | 2020-11-28 | 1      | 173        |
# | 2020-11-28 | 2      | 30         |
# | 2020-12-03 | 1      | 41         |
# | 2020-12-09 | 2      | 27         |
# +------------+--------+------------+


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    # Subtract in_time from out_time and save as new column.
    employees['total_time'] = employees.apply(lambda x: x['out_time'] - x['in_time'], axis=1)
    # GroupBy by emp_id and event-day and summarize group total_time.
    employees['total_time'] = employees.groupby(by=['emp_id', 'event_day'])['total_time'].transform(sum)
    # Delete overlapping days, cuz we're assigning total_time to every pair of emp_id + event_day.
    employees.drop_duplicates(subset=['emp_id', 'event_day'], inplace=True)
    employees.rename(
        columns={
            'event_day': 'day',
        },
        inplace=True,
    )
    return employees[['day', 'emp_id', 'total_time']]
