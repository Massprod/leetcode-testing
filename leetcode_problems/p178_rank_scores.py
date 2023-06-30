from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from tasks_database.db import get_session


# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | score       | decimal |
# +-------------+---------+
# id is the primary key for this table.
# Each row of this table contains the score of a game.
# Score is a floating point value with two decimal places.

# Write an SQL query to rank the scores.
# The ranking should be calculated according to the following rules:
#   - The scores should be ranked from the highest to the lowest.
#   - If there is a tie between two scores, both should have the same ranking.
#   - After a tie, the next ranking number should be the next consecutive integer value.
#      In other words, there should be no holes between ranks.
# Return the result table ordered by score in descending order.

db: Session = next(get_session())
db.execute(
    text(
        "DROP TABLE IF EXISTS scores;"
    )
)
db.execute(
    text(
        "CREATE TABLE scores("
        "   id SERIAL PRIMARY KEY,"
        "   score FLOAT(2)"
        ");"
    )
)
db.commit()
db.execute(
    text(
        "INSERT INTO scores(score)"
        "values"
        "(3.50),"
        "(3.65),"
        "(4.00),"
        "(3.85),"
        "(4.00),"
        "(3.65);"
    )
)
db.commit()

data: Result = db.execute(
    text(
        "SELECT "
        "score,"
        "dense_rank() over(ORDER BY score DESC) as 'rank'"  # using 'rank' because in MySQL it conflicts                                 
        "FROM scores;"                                      # with rank() by itself, in PostgreSQL doesn't.
    )
)

for _ in data:
    print(_)

# Expected:
# +-------+------+
# | score | rank |
# +-------+------+
# | 4.00  | 1    |
# | 4.00  | 1    |
# | 3.85  | 2    |
# | 3.65  | 3    |
# | 3.65  | 3    |
# | 3.50  | 4    |
# +-------+------+
