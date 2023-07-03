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
# ----------------------------
# Write an SQL query to report the fraction of players that logged in again
#   on the day after the day they first logged in, rounded to 2 decimal places.
# In other words, you need to count the number of players that logged in for
#   at least two consecutive days starting from their first login date,
#   then divide that number by the total number of players.

db: Session = next(get_session())
db.execute(
    text(
        "DROP TABLE IF EXISTS activity;"
    )
)
db.commit()
db.execute(
    text(
        "CREATE TABLE activity("
        "   player_id SERIAL,"
        "   device_id INTEGER NOT NULL,"
        "   event_date DATE,"
        "   games_played INTEGER NOT NULL,"
        "   CONSTRAINT pk_activity"
        "       PRIMARY KEY (player_id, event_date)"
        ");"
    )
)
db.commit()
db.execute(
    text(
        "INSERT INTO activity("
        "player_id,"
        "device_id,"
        "event_date,"
        "games_played) "
        "VALUES "
        "('1', '2', '2016-03-01', '5'),"
        "('1', '2', '2016-03-02', '6'),"
        "('2', '3', '2017-06-25', '1'),"
        "('3', '1', '2016-03-02', '0'),"
        "('3', '4', '2018-07-03', '5');"
    )
)
db.commit()
