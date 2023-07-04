from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from tasks_database.db import get_session

# Table: Customer
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# | referee_id  | int     |
# +-------------+---------+
# id is the primary key column for this table.
# Each row of this table indicates the id of a customer, their name,
#   and the id of the customer who referred them.
# -------------------------
# Write an SQL query to report the names of the customer that are not referred by the customer with id = 2.
# Return the result table in any order.


sql_schema: str = "DROP TABLE IF EXISTS customer;"\
                  "Create table Customer (id int, name varchar(25), referee_id int);" \
                  "Truncate table Customer;" \
                  "insert into Customer (id, name, referee_id) values (1, 'Will', Null);" \
                  "insert into Customer (id, name, referee_id) values (2, 'Jane', Null);" \
                  "insert into Customer (id, name, referee_id) values (3, 'Alex', 2);" \
                  "insert into Customer (id, name, referee_id) values (4, 'Bill', Null);" \
                  "insert into Customer (id, name, referee_id) values (5, 'Zack', 1);" \
                  "insert into Customer (id, name, referee_id) values (6, 'Mark', 2);"

db: Session = next(get_session())
db.execute(text(sql_schema))
db.commit()

postgresql_query: str = "SELECT name " \
                        "FROM customer " \
                        "WHERE referee_id != 2 OR referee_id IS Null;"
data: Result = db.execute(text(postgresql_query))
for _ in data:
    print(_)

# Expected output:
# +------+
# | name |
# +------+
# | Will |
# | Jane |
# | Bill |
# | Zack |
# +------+
