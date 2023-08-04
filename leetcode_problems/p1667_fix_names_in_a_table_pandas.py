import pandas as pd


# Write a solution to fix the names so that only the first character
#   is uppercase and the rest are lowercase.
# Return the result table ordered by user_id.
# +---------+-------+
# | user_id | name  |
# +---------+-------+
# | 1       | aLice |
# | 2       | bOB   |
# +---------+-------+


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    # Resetting only 1 column.
    # Always use lambda to apply.
    users['name'] = users['name'].apply(lambda x: str.capitalize(x))
    users.sort_values(by='user_id', inplace=True)
    return users
