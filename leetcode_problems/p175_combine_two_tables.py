from sqlalchemy.sql import text
from tasks_database.db import get_session

# Table: Person
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | personId    | int     |
# | lastName    | varchar |
# | firstName   | varchar |
# +-------------+---------+
# personId is the primary key column for this table.
# This table contains information about the ID of some persons and their first and last names.
# ---------------------
# Table: Address
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | addressId   | int     |
# | personId    | int     |
# | city        | varchar |
# | state       | varchar |
# +-------------+---------+
# addressId is the primary key column for this table.
# Each row of this table contains information about the city and state of one person with ID = PersonId.
# ---------------------
# Write an SQL query to report the first name, last name, city, and state of each person in the Person table.
# If the address of a personId is not present in the Address table, report null instead.
# Return the result table in any order.


db = next(get_session())
db.execute(
    text(
        "DROP TABLE IF EXISTS person;"
        "DROP TABLE IF EXISTS address;"
    )
)
db.execute(
    text(
        "CREATE TABLE person("
        "personId SERIAL PRIMARY KEY,"
        "lastName VARCHAR(50),"
        "firstName VARCHAR(50)"
        ");"
        
        "INSERT INTO person(lastName, firstName)"
        "values"
        "('Wang', 'Allen'),"
        "('Alice', 'Bob');"
    )
)
db.commit()

db.execute(
    text(
        "CREATE TABLE address("
        "addressId SERIAL PRIMARY KEY,"
        "personId INTEGER UNIQUE,"
        "city VARCHAR(50),"
        "state VARCHAR(50)"
        ");"
        
        "INSERT INTO address(personId, city, state)"
        "VALUES"
        "(2, 'New York City', 'New York'),"
        "(3, 'Leetcode', 'California');"
    )
)
db.commit()

data = (db.execute(
    text(
        "SELECT "
        "firstName, "
        "lastName, "
        "address.city, "
        "address.state "
        "FROM person "
        "LEFT OUTER JOIN address ON address.personId = person.personId;"
    )
))
for _ in data:
    print(_)

# DesiredOutput:
# +-----------+----------+---------------+----------+
# | firstName | lastName | city          | state    |
# +-----------+----------+---------------+----------+
# | Allen     | Wang     | Null          | Null     |
# | Bob       | Alice    | New York City | New York |
# +-----------+----------+---------------+----------+
# ---------------------
# Working correctly, but I need to think about design of these tasks,
# and maybe don't just use execute().
# Because it's more convenient to use sqlalchemy select() and get more experience with framework.
