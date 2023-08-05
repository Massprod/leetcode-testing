import pandas as pd


# Write a solution to find the first login date for each player.
# Return the result table in any order.
# ------------------
# Activity table:
# +-----------+-----------+------------+--------------+
# | player_id | device_id | event_date | games_played |
# +-----------+-----------+------------+--------------+
# | 1         | 2         | 2016-03-01 | 5            |
# | 1         | 2         | 2016-05-02 | 6            |
# | 2         | 3         | 2017-06-25 | 1            |
# | 3         | 1         | 2016-03-02 | 0            |
# | 3         | 4         | 2018-07-03 | 5            |
# +-----------+-----------+------------+--------------+
# Output:
# +-----------+-------------+
# | player_id | first_login |
# +-----------+-------------+
# | 1         | 2016-03-01  |
# | 2         | 2017-06-25  |
# | 3         | 2016-03-02  |
# +-----------+-------------+


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # GroupBy: player_id with min(event_date).
    activity['first_login'] = activity.groupby(by=['player_id'])['event_date'].transform(min)
    # As always, dropping duplicated rows -> every player_id will have same first_login date.
    activity.drop_duplicates(subset=['player_id', 'first_login'], inplace=True)
    return activity[['player_id', 'first_login']]
