from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from tasks_database.db import get_session


# Table: Logs
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | num         | varchar |
# +-------------+---------+
# id is the primary key for this table.
# id is an autoincrement column.
# ------------------
# Write an SQL query to find all numbers that appear at least three times consecutively.
# Return the result table in any order.

db: Session = next(get_session())
db.execute(
    text(
        "DROP TABLE IF EXISTS logs;"
    )
)
db.execute(
    text(
        "CREATE TABLE logs("
        "   id SERIAL PRIMARY KEY,"
        "   num VARCHAR(50)"
        ");"
    )
)
db.commit()
db.execute(
    text(
        "INSERT INTO logs(num)"
        "VALUES"
        "(1),"
        "(1),"
        "(1),"
        "(2),"
        "(1),"
        "(2),"
        "(2);"
    )
)
db.commit()

# Most basic way I know:
#  is multiple JOIN on column we need to filter.
# Should we return Null if there's no consecutive values or just empty result?
# Suppose we need to return Null(None) than we need to extra take SELECT from query.
# Literally all tasks before that was asking to always return Null(None), if there's empty column.
# But now it's incorrect. Ok.
# ------------------
# Mistakes:
#   1) Missed part with values need to be distinct, because there's duplicates.
#      ^^Don't actually a fault, because why shouldn't we have info about duplicates?
#        Like suppose we know that there's 3 + 3 + 3 on indexes 1, 2, 3
#        but if there's another 3 + 3 + 3 on some indexes 9, 10, 11?
#        Without duplicates, we will have no idea about them, but then we probably should know their indexes,
#        so it's another problem. In case of this task it's better to just use DISTINCT.
#   2) Make Query return None instead of empty column.


data: Result = db.execute(
    text(
        "SELECT e1.num AS ConsecutiveNums "
        "FROM logs AS e1 "
        "JOIN logs AS e2 ON e1.id = e2.id - 1 AND e1.num = e2.num "
        "JOIN logs AS e3 ON e2.id = e3.id - 1 AND e2.num = e3.num;"
    )
)
for _ in data:
    print(_)
