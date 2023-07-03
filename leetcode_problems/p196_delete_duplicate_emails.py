from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from tasks_database.db import get_session

# Table: Person
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | email       | varchar |
# +-------------+---------+
# id is the primary key column for this table.
# Each row of this table contains an email. The emails will not contain uppercase letters.
# -------------------------
# Delete all the duplicate emails, keeping only one unique email with the smallest id.
#   (For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.)
# After running your script, the answer shown is the Person table.
# The driver will first compile and run your piece of code and then show the Person table.
# The final order of the Person table does not matter.

db: Session = next(get_session())
db.execute(
    text(
        "DROP TABLE IF EXISTS person;"
    )
)
db.commit()
db.execute(
    text(
        "CREATE TABLE person("
        "   id SERIAL PRIMARY KEY,"
        "   email VARCHAR(200) NOT NULL"
        ");"
    )
)
db.commit()
db.execute(
    text(
        "INSERT INTO person(email) "
        "VALUES "
        "('john@example.com'),"
        "('bob@example.com'),"
        "('john@example.com');"
    )
)
db.commit()

# Don't work in MySQL, because ->
# -> ! You can't specify target table 'person' for update in FROM clause !
postgresql_query: str = "DELETE FROM person " \
                        "WHERE id IN (" \
                        "   SELECT e2.id" \
                        "   FROM person AS e1" \
                        "   JOIN person AS e2 ON e2.email = e1.email" \
                        "   WHERE e2.id > e1.id" \
                        ");"

# I don't know wtf happened with Leetcode part but, their literal solution copied from Editorial is False.
# W.e leaving is a NOTE, but Task is bugged and I can't commit correctly anyway.
# Both should be working.
mysql_query: str = "DELETE e1 " \
                   "FROM person AS e1, person AS e2 " \
                   "WHERE e1.email = e2.email AND e1.id > e2.id;"
db.execute(text(postgresql_query))
db.commit()
data: Result = db.execute(text("SELECT * FROM person;"))
for _ in data:
    print(_)
