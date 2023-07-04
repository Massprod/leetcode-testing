from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from tasks_database.db import get_session


# Table: World
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | name        | varchar |
# | continent   | varchar |
# | area        | int     |
# | population  | int     |
# | gdp         | bigint  |
# +-------------+---------+
# name is the primary key column for this table.
# Each row of this table gives information about the name of a country,
#   the continent to which it belongs, its area, the population, and its GDP value.
# ---------------------------
# A country is big if:
#   it has an area of at least three million (i.e., 3000000 km2), or
#   it has a population of at least twenty-five million (i.e., 25000000).
# Find the name, population, and area of the big countries.
# Return the result table in any order.

# SQL schema:
# DROP TABLE IF EXISTS world;
# Create table If Not Exists World (name varchar(255), continent varchar(255), area int, population int, gdp bigint);
# insert into World (name, continent, area, population, gdp)
# values
# ('Afghanistan', 'Asia', '652230', '25500100', '20343000000'),
# ('Albania', 'Europe', '28748', '2831741', '12960000000'),
# ('Algeria', 'Africa', '2381741', '37100000', '188681000000'),
# ('Andorra', 'Europe', '468', '78115', '3712000000'),
# ('Angola', 'Africa', '1246700', '20609294', '100990000000');

db: Session = next(get_session())
db.execute(
    text(
        "DROP TABLE IF EXISTS world;"
        "CREATE TABLE world("
        "name VARCHAR(255),"
        "continent VARCHAR(255),"
        "area INTEGER,"
        "population INTEGER,"
        "gdp BIGINT"
        ");"
        "INSERT INTO world (name, continent, area, population, gdp) "
        "VALUES "
        "('Afghanistan', 'Asia', '652230', '25500100', '20343000000'),"
        "('Albania', 'Europe', '28748', '2831741', '12960000000'),"
        "('Algeria', 'Africa', '2381741', '37100000', '188681000000'),"
        "('Andorra', 'Europe', '468', '78115', '3712000000'),"
        "('Angola', 'Africa', '1246700', '20609294', '100990000000');"
    )
)
db.commit()

# Query:
# SELECT name, population, area
# FROM world
# WHERE
# area >= 3000000
# OR
# population >= 25000000;

postgresql_query: str = "SELECT name, population, area " \
                        "FROM world " \
                        "WHERE " \
                        "area >= 3000000 " \
                        "OR " \
                        "population >= 25000000;"
data: Result = db.execute(text(postgresql_query))
for _ in data:
    print(_)

# Expected output:
# +-------------+------------+---------+
# | name        | population | area    |
# +-------------+------------+---------+
# | Afghanistan | 25500100   | 652230  |
# | Algeria     | 37100000   | 2381741 |
# +-------------+------------+---------+
