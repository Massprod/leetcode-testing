from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from tasks_database.db import get_session

# Table: Weather
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | recordDate    | date    |
# | temperature   | int     |
# +---------------+---------+
# id is the primary key for this table.
# This table contains information about the temperature on a certain day.
# ----------------------------
# Write an SQL query to find all dates' Id with higher temperatures compared to its previous dates (yesterday).
# Return the result table in any order.

db: Session = next(get_session())
db.execute(
    text(
        "DROP TABLE IF EXISTS weather;"
    )
)
db.commit()
db.execute(
    text(
        "CREATE TABLE weather("
        "   id SERIAL PRIMARY KEY,"
        "   recordDate DATE NOT NULL,"
        "   temperature INTEGER NOT NULL"
        ");"
    )
)
db.commit()
db.execute(
    text(
        "INSERT INTO weather(recordDate, temperature) "
        "VALUES "
        "('2015-01-01', 10),"
        "('2015-01-02', 25),"
        "('2015-01-03', 20),"
        "('2015-01-04', 30);"
    )
)
db.commit()

# Failed 2 times, because I was using PostgreSQL syntax and didn't know we need to use DATE_ADD() in MySQL.
mysql_query: str = "SELECT e2.id " \
                   "FROM weather AS e1 " \
                   "JOIN weather AS e2 ON e1.recordDate = DATE_ADD(e2.recordDate, INTERVAL -1 day) " \
                   "WHERE e2.temperature > e1.temperature;"

# There's no DATE_ADD() in postgresql, but we can simply add or extract INTERVAL 'week', 'month' w.e we want.
postgresql_query: str = "SELECT e2.id " \
                        "FROM weather AS e1 " \
                        "JOIN weather AS e2 ON e1.recordDate = e2.recordDate - INTERVAL '1 day' " \
                        "WHERE e2.temperature > e1.temperature;"
data: Result = db.execute(text(postgresql_query))
for _ in data:
    print(_)
