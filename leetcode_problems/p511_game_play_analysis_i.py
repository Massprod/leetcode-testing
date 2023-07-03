from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from tasks_database.db import get_session


# Table: Activity
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | player_id    | int     |
# | device_id    | int     |
# | event_date   | date    |
# | games_played | int     |
# +--------------+---------+
# (player_id, event_date) is the primary key of this table.
# This table shows the activity of players of some games.
# Each row is a record of a player who logged in and played a number of games (possibly 0)
#   before logging out on someday using some device.
# ---------------------------
# Find the first login date for each player.
# Return the result table in any order.


db: Session = next(get_session())
db.execute(
    text(
        "DROP TABLE IF EXISTS activity;"
    )
)
db.execute(
    text(
        "Create table If Not Exists Activity (player_id int, device_id int, event_date date, games_played int);"
        "Truncate table Activity;"
        "insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-01', '5');"
        "insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-05-02', '6');"
        "insert into Activity (player_id, device_id, event_date, games_played) values ('2', '3', '2017-06-25', '1');"
        "insert into Activity (player_id, device_id, event_date, games_played) values ('3', '1', '2016-03-02', '0');"
        "insert into Activity (player_id, device_id, event_date, games_played) values ('3', '4', '2018-07-03', '5');"
    )
)
db.commit()

# Just simple GROUP BY to store all player_ids and their corresponding MIN() values(event_date).

query: str = "SELECT " \
             "player_id," \
             "first_login " \
             "FROM (" \
             "  SELECT player_id, MIN(event_date) AS first_login " \
             "  FROM activity " \
             "  GROUP BY player_id" \
             ") AS test " \
             "ORDER BY player_id;"
data: Result = db.execute(text(query))
for _ in data:
    print(_)

# Correct output:
# +-----------+-------------+
# | player_id | first_login |
# +-----------+-------------+
# | 1         | 2016-03-01  |
# | 2         | 2017-06-25  |
# | 3         | 2016-03-02  |
# +-----------+-------------+
