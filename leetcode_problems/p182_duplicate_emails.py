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
        "   email VARCHAR(200) UNIQUE"
        ");"
    )
)
db.commit()
db.execute(
    text(
        "INSERT INTO person(email) "
        "VALUES "
        "('a@b.com'),"
        "('c@d.com'),"
        "('a@b.com');"
    )
)
db.commit()
