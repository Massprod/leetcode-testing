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
        "('2015-01-03', 25),"
        "('2015-01-03', 20),"
        "('2015-01-04', 30);"
    )
)
db.commit()

