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


# No idea about fancy logic we can implement here, but I know we need to take 2 options.
# First option is every player and their first_login date. <- Already done that before.
# Second option is every player and their first_login date + 1 day.
# If we know this 2 options we can filter on them.

# It will give us every player who have logged in and their FIRST_LOGIN_DATE.
first_option: str = "SELECT player_id, MIN(event_date) " \
                    "FROM activity " \
                    "GROUP BY player_id;"
show: Result = db.execute(text(first_option))
print("First")
for _ in show:
    print(_)
# Same query, but now we're having data on second_day in it.
second_option: str = "SELECT player_id, (MIN(event_date) + INTERVAL '1 day') AS second_day " \
                     "FROM activity " \
                     "GROUP BY player_id;"
show = db.execute(text(second_option))
print("Second")
for _ in show:
    print(_)
# No idea how to make this more pretty, or simplier, but we can just check
# every combo of (player_id, event_date) IN this 2 options, if they're inside it's correct.
# All it's left to combine that to work with MySQL, because we can't use INTERVAL without DATE_ADD(),
# and correctly use ROUND() on this.
count_2_days: str = "SELECT COUNT(DISTINCT e2.player_id) " \
                    "FROM activity AS e1 " \
                    "JOIN activity AS e2 ON e1.player_id = e2.player_id " \
                    "AND (e1.player_id, e1.event_date) IN (" \
                    "   SELECT player_id, MIN(event_date) " \
                    "   FROM activity " \
                    "   GROUP BY player_id" \
                    ")" \
                    "AND (e2.player_id, e2.event_date) IN (" \
                    "   SELECT player_id, (MIN(event_date) + INTERVAL '1 day') AS second_day " \
                    "   FROM activity " \
                    "   GROUP BY player_id" \
                    ");"
show = db.execute(text(count_2_days))
print("2 cons_days")
for _ in show:
    print(_)

# ROUND() was calculating INTEGER division, floor division, and it was always 0.
# Fixed it by changing type of data from COUNT() it was BIGINT, now it's DECIMAL.
postgresql_query: str = "SELECT ROUND(" \
                        "   CAST(" \
                        "       (" \
                        "       SELECT COUNT(DISTINCT e2.player_id) " \
                        "       FROM activity AS e1" \
                        "       JOIN activity AS e2 ON e1.player_id = e2.player_id " \
                        "       AND (e1.player_id, e1.event_date) IN (" \
                        "           SELECT player_id, MIN(event_date) " \
                        "           FROM activity " \
                        "           GROUP BY player_id" \
                        "           )" \
                        "       AND (e2.player_id, e2.event_date) IN (" \
                        "           SELECT player_id, (MIN(event_date) + INTERVAL '1 day') AS second_day " \
                        "           FROM activity " \
                        "           GROUP BY player_id" \
                        "           )" \
                        "       ) AS DECIMAL(10, 2)" \
                        "       )" \
                        "   /" \
                        "   CAST(" \
                        "       (" \
                        "       SELECT COUNT(DISTINCT player_id) " \
                        "       FROM activity " \
                        "       ) AS DECIMAL(10, 2)" \
                        "       )," \
                        "   2) AS fraction;" \

# For MySQL Query, all changes that I need to do is replace ! + INTERVAL '1 day' ! for ->
#     -> DATE_ADD(MIN(event_date), INTERVAL 1 day). Not going to rewrite it for this.

show = db.execute(text(postgresql_query))
print("Fraction")
for _ in show:
    print(_)
