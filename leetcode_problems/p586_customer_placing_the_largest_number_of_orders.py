from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from tasks_database.db import get_session

# Table: Orders
# +-----------------+----------+
# | Column Name     | Type     |
# +-----------------+----------+
# | order_number    | int      |
# | customer_number | int      |
# +-----------------+----------+
# order_number is the primary key for this table.
# This table contains information about the order ID and the customer ID.
# ------------------------------
# Find the customer_number for the customer who has placed the largest number of orders.
# The test cases are generated so that exactly one customer will have placed more orders than any other customer.
# ^^This, we can simply limit 1 in ordered by DESC, grouped by customer_number.

# Sql schema for simplier copy:
# ------------------------
# DROP TABLE IF EXISTS orders;
# Create table If Not Exists orders (order_number int, customer_number int);
# Truncate table orders;
# insert into orders (order_number, customer_number) values ('1', '1');
# insert into orders (order_number, customer_number) values ('2', '2');
# insert into orders (order_number, customer_number) values ('3', '3');
# insert into orders (order_number, customer_number) values ('4', '3');

db: Session = next(get_session())
db.execute(
    text(
        "DROP TABLE IF EXISTS orders;"
        "CREATE TABLE orders("
        "order_number INTEGER,"
        "customer_number INTEGER"
        ");"
        "INSERT INTO orders(order_number, customer_number) "
        "VALUES "
        "(1, 1),"
        "(2, 2),"
        "(3, 3),"
        "(4, 3);"
    )
)
db.commit()

# PostgreSQL query:
# SELECT customer_number
# FROM orders
# GROUP BY customer_number
# ORDER BY COUNT(order_number) DESC
# LIMIT 1;

postgresql_query: str = "SELECT customer_number " \
                        "FROM orders " \
                        "GROUP BY customer_number " \
                        "ORDER BY COUNT(order_number) DESC " \
                        "LIMIT 1;"
data: Result = db.execute(text(postgresql_query))
for _ in data:
    print(_)


# Expected output:
# +-----------------+
# | customer_number |
# +-----------------+
# | 3               |
# +-----------------+


# If test cases were designed with duplicates?
# Like there's 1+ customers with same MAX() orders?
# Guess I would just take MAX(order_number) and use it as a subquery to filter all customer with this order_number.
# Should work, let's even try this.
print("\nWith duplicates")
db.execute(
    text("INSERT INTO orders(order_number, customer_number) "
         "VALUES (5, 2)")
)
db.commit()

# Most basic query:
# SELECT customer_number
# FROM orders
# GROUP BY customer_number
# HAVING COUNT(order_number) IN (
#   SELECT MAX(count)
#   FROM (
#       SELECT customer_number, COUNT(order_number)
#       FROM orders
#       GROUP BY customer_number
#       ORDER BY COUNT(order_number) DESC
#       ) AS test
# );

# Overcomplicated, but working and good experience on using multiple GROUP BY.
postgresql_query = "SELECT customer_number " \
                   "FROM orders " \
                   "GROUP BY customer_number " \
                   "HAVING COUNT(order_number) IN (" \
                   "    SELECT MAX(count) " \
                   "    FROM (" \
                   "        SELECT customer_number, COUNT(order_number) " \
                   "        FROM orders " \
                   "        GROUP BY customer_number " \
                   "        ORDER BY COUNT(order_number) DESC " \
                   "        ) AS test " \
                   ");"

data = db.execute(text(postgresql_query))
for _ in data:
    print(_)
