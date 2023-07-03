from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from tasks_database.db import get_session

# Table: Trips
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | id          | int      |
# | client_id   | int      |
# | driver_id   | int      |
# | city_id     | int      |
# | status      | enum     |
# | request_at  | date     |
# +-------------+----------+
# id is the primary key for this table.
# The table holds all taxi trips. Each trip has a unique id,
#   while client_id and driver_id are foreign keys to the users_id at the Users table.
# Status is an ENUM type of ('completed', 'cancelled_by_driver', 'cancelled_by_client').

# Table: Users
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | users_id    | int      |
# | banned      | enum     |
# | role        | enum     |
# +-------------+----------+
# users_id is the primary key for this table.
# The table holds all users. Each user has a unique users_id,
#   and role is an ENUM type of ('client', 'driver', 'partner').
# banned is an ENUM type of ('Yes', 'No').
# --------------------------
# The cancellation rate is computed by dividing the number of canceled (by client or driver)
#   requests with unbanned users by the total number of requests with unbanned users on that day.
# Write a SQL query to find the cancellation rate of requests with unbanned users
#   (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03".
# Round Cancellation Rate to two decimal points.
# Return the result table in any order.

db: Session = next(get_session())
db.execute(
    text(
        "DROP TABLE IF EXISTS users, trips;"
    )
)
db.commit()
# Creating of TYPES to use
db.execute(
    text(
        "DROP TYPE IF EXISTS status; "
        "CREATE TYPE status AS ENUM ('completed', 'cancelled_by_driver', 'cancelled_by_client');"
    )
)
db.execute(
    text(
        "DROP TYPE IF EXISTS role;"
        "CREATE TYPE role AS ENUM ('client', 'driver', 'partner');"
    )
)
db.execute(
    text(
        "DROP TYPE IF EXISTS banned;"
        "CREATE TYPE banned AS ENUM ('Yes', 'No');"
    )
)
db.commit()
# Creating of users table
db.execute(
    text(
        "CREATE TABLE users("
        "   users_id SERIAL PRIMARY KEY,"
        "   banned banned NOT NULL,"
        "   role role NOT NULL"
        ");"
    )
)
db.commit()
# Creating of trips table
db.execute(
    text(
        "CREATE TABLE trips("
        "   id SERIAL PRIMARY KEY,"
        "   client_id INTEGER NOT NULL,"
        "   driver_id INTEGER NOT NULL,"
        "   city_id INTEGER NOT NULL,"
        "   status status NOT NULL,"
        "   request_at DATE NOT NULL,"
        "   CONSTRAINT client_id"
        "       FOREIGN KEY (client_id)"
        "       REFERENCES users(users_id),"
        "   CONSTRAINT driver_id"
        "       FOREIGN KEY (driver_id)"
        "       REFERENCES users(users_id)"
        ");"
    )
)
db.commit()
db.execute(
    text(
        "insert into Users (users_id, banned, role) values ('1', 'No', 'client');"
        "insert into Users (users_id, banned, role) values ('2', 'Yes', 'client');"
        "insert into Users (users_id, banned, role) values ('3', 'No', 'client');"
        "insert into Users (users_id, banned, role) values ('4', 'No', 'client');"
        "insert into Users (users_id, banned, role) values ('10', 'No', 'driver');"
        "insert into Users (users_id, banned, role) values ('11', 'No', 'driver');"
        "insert into Users (users_id, banned, role) values ('12', 'No', 'driver');"
        "insert into Users (users_id, banned, role) values ('13', 'No', 'driver');"
        "insert into Trips (id, client_id, driver_id, city_id, status, request_at)"
        " values ('1', '1', '10', '1', 'completed', '2013-10-01');"
        "insert into Trips (id, client_id, driver_id, city_id, status, request_at)"
        " values ('2', '2', '11', '1', 'cancelled_by_driver', '2013-10-01');"
        "insert into Trips (id, client_id, driver_id, city_id, status, request_at)"
        " values ('3', '3', '12', '6', 'completed', '2013-10-01');"
        "insert into Trips (id, client_id, driver_id, city_id, status, request_at)"
        " values ('4', '4', '13', '6', 'cancelled_by_client', '2013-10-01');"
        "insert into Trips (id, client_id, driver_id, city_id, status, request_at)"
        " values ('5', '1', '10', '1', 'completed', '2013-10-02');"
        "insert into Trips (id, client_id, driver_id, city_id, status, request_at)"
        " values ('6', '2', '11', '6', 'completed', '2013-10-02');"
        "insert into Trips (id, client_id, driver_id, city_id, status, request_at)"
        " values ('7', '3', '12', '6', 'completed', '2013-10-02');"
        "insert into Trips (id, client_id, driver_id, city_id, status, request_at)"
        " values ('8', '2', '12', '12', 'completed', '2013-10-03');"
        "insert into Trips (id, client_id, driver_id, city_id, status, request_at)"
        " values ('9', '3', '10', '12', 'completed', '2013-10-03');"
        "insert into Trips (id, client_id, driver_id, city_id, status, request_at)"
        " values ('10', '4', '13', '12', 'cancelled_by_driver', '2013-10-03');"
    )
)
db.commit()

# We need to use COUNT() to count particular rows, and I have no idea if there's some
# method like IF statement in python. Without it, I don't see how to solve it and there's 99% something like that.
# ---------------
# There's CASE( WHEN condition THEN result END) clause, so we can filter every row by that and count all we need.
# After that it's just default filtering on SUBQUERY from users with unbanned users in it.
# ---------------
# Failed on part with WHERE client_id, driver_id. Because I was thinking we can just use them together,
# but in SQL we should filter one by one -> first check client_id IN(), and only after driver_id IN().

# Working with leet_code MySQL db, but for my local Postgresql I need to change it.
mysql_query: str = "SELECT " \
                   "request_at AS Day, " \
                   "ROUND(" \
                   "   COUNT(CASE WHEN status LIKE 'cancelled%' THEN 1 END)" \
                   "   /" \
                   "   COUNT(trips.id), 2) AS 'Cancellation Rate' " \
                   "FROM trips " \
                   "WHERE " \
                   "client_id IN (" \
                   "   SELECT users_id " \
                   "   FROM users " \
                   "   WHERE banned NOT LIKE 'Yes'" \
                   ")" \
                   "AND " \
                   "driver_id IN (" \
                   "   SELECT users_id " \
                   "   FROM users " \
                   "   WHERE banned NOT LIKE 'Yes'" \
                   ")" \
                   "AND " \
                   "request_at BETWEEN '2013-10-01' AND '2013-10-03' " \
                   "GROUP BY Day, 'Cancellation Rate';"

# In postgresql we can't use COUNT() in GROUP BY, and we can't set name of a column 'Cancellation rate' with
# single quotes, it's need to be double quotes.
# So we're first creating subquery with day, total_trips, cancelled trips and grouping them,
# and only after that we can use it to calculate "Cancellation rate".
# Another thing which done in MySQL automatically, in postgresql we need to convert ENUM into TEXT
# before we can use LIKE on it -> ::type.
# Same goes for COUNT() it's better to convert them into numeric explicitly otherwise they're ignored or incorrect,
# at least in this case.
postgresql_query: str = 'WITH cancellation_rates AS (' \
                        '   SELECT ' \
                        '       request_at AS Day,' \
                        '       COUNT(id) AS total_trips,' \
                        '       COUNT(' \
                        "           CASE WHEN status::text LIKE 'cancelled%' THEN 1 END" \
                        '       ) AS cancelled_trips' \
                        '   FROM trips ' \
                        '   WHERE' \
                        '   client_id IN (' \
                        '       SELECT users_id ' \
                        '       FROM users ' \
                        "       WHERE banned::text NOT LIKE 'Yes'" \
                        '   )' \
                        '   AND' \
                        '   driver_id IN (' \
                        '       SELECT users_id ' \
                        '       FROM users ' \
                        "       WHERE banned::text NOT LIKE 'Yes'" \
                        '   )' \
                        '   AND ' \
                        "   request_at BETWEEN '2013-10-01' AND '2013-10-03'" \
                        '   GROUP BY request_at' \
                        ')' \
                        'SELECT' \
                        '   Day,' \
                        '   ROUND(cancelled_trips::numeric / total_trips::numeric, 2) AS "Cancellation rate"' \
                        'FROM' \
                        '   cancellation_rates;'

data: Result = db.execute(text(postgresql_query))

test_out: set[float] = {0.33, 0.00, 0.50}
count: int = 0
for _ in data:
    print(_)
    assert float(_[1]) in test_out
    count += 1
assert count == len(test_out)
