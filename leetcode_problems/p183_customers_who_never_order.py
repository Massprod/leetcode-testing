from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from tasks_database.db import get_session


# Table: Customers
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# +-------------+---------+
# id is the primary key column for this table.
# Each row of this table indicates the ID and name of a customer.

# Table: Orders
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | customerId  | int  |
# +-------------+------+
# id is the primary key column for this table.
# customerId is a foreign key of the ID from the Customers table.
# Each row of this table indicates the ID of an order and the ID of the customer who ordered it.
# ---------------------
# Write an SQL query to report all customers who never order anything.
# Return the result table in any order.

db: Session = next(get_session())
db.execute(
    text(
        "DROP TABLE IF EXISTS customers, orders;"
    )
)
db.commit()
db.execute(
    text(
        "CREATE TABLE customers("
        "   id SERIAL PRIMARY KEY,"
        "   name VARCHAR(50)"
        ");"
    )
)
db.commit()
db.execute(
    text(
        "CREATE TABLE orders("
        "   id SERIAL PRIMARY KEY,"
        "   customerId INTEGER,"
        "   CONSTRAINT customerId"
        "       FOREIGN KEY (customerId)"
        "       REFERENCES customers(id)"
        ");"
    )
)
db.commit()
db.execute(
    text(
        "INSERT INTO customers(name) "
        "VALUES"
        "('Joe'),"
        "('Henry'),"
        "('Sam'),"
        "('Max');"
    )
)
db.execute(
    text(
        "INSERT INTO orders(customerId) "
        "VALUES"
        "(3),"
        "(1);"
    )
)
db.commit()


# Select everything from customers and JOIN with orders by customerId,
# use this to filter everything from customers?
# What about duplicates? Names is not UNIQUE column and there's no other indication.
# Failed on duplicates, because we can have same Name customers but diff IDs.
# Think about duplicates and ignore them for no reason, obviously there's case with same CustomerNames,
# and it's better to filter on unique ID.


data: Result = db.execute(
    text(
        "SELECT name AS Customers "
        "FROM customers "
        "WHERE id NOT IN ("
        "   SELECT e2.customerId"
        "   FROM customers AS e1"
        "   JOIN orders AS e2 ON e1.id = e2.customerId"
        ");"
    )
)
test_output: set[str] = {"Henry", "Max"}
count: int = 0
for _ in data:
    assert _[0] in test_output
    count += 1
assert count == len(test_output)
