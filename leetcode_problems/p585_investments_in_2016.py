from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from tasks_database.db import get_session

# Table: Insurance
# +-------------+-------+
# | Column Name | Type  |
# +-------------+-------+
# | pid         | int   |
# | tiv_2015    | float |
# | tiv_2016    | float |
# | lat         | float |
# | lon         | float |
# +-------------+-------+
# pid is the primary key column for this table.
# Each row of this table contains information about one policy where:
#   pid is the policyholder's policy ID.
#   tiv_2015 is the total investment value in 2015
#       and tiv_2016 is the total investment value in 2016.
#   lat is the latitude of the policy holder's city.
#       It's guaranteed that lat is not NULL.
#   lon is the longitude of the policy holder's city.
#       It's guaranteed that lon is not NULL.

# Write an SQL query to report the sum of all total investment values in 2016 tiv_2016,
#   for all policyholders who:
#       have the same tiv_2015 value as one or more other policyholders, and are not located
#       in the same city like any other policyholder (i.e., the (lat, lon) attribute pairs must be unique).
# Round tiv_2016 to two decimal places.

sql_schema: str = "DROP TABLE IF EXISTS Insurance;" \
                  "Create Table Insurance (pid int, tiv_2015 float, tiv_2016 float, lat float, lon float);" \
                  "Truncate table Insurance;" \
                  "insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('1', '10', '5', '10', '10');" \
                  "insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('2', '20', '20', '20', '20');" \
                  "insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('3', '10', '30', '20', '20');" \
                  "insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('4', '10', '40', '40', '40');"

db: Session = next(get_session())
db.execute(text(sql_schema))
db.commit()


# We need to options to filter on.
# First is all holders with same tiv_2015 as at least 1 another holder.
# Second is all holders with unique city (lat, lon) pairs.
# If I can get them, I could filter on them easily with WHERE.

# Actually we can just find value of tiv_2015 which correct for multiple holders and filter on that.
# Now anyone who is having tiv_2015 equal to values in this subquery, is holder with equal to another holder tiv_2015.
first_option: str = "SELECT tiv_2015 " \
                    "FROM insurance " \
                    "GROUP BY tiv_2015 " \
                    "HAVING COUNT(tiv_2015) > 1;"
first_data: Result = db.execute(text(first_option))
print("FirstOption")
for _ in first_data:
    print(_)

# All (lat, lon) pairs with COUNT(pid) = 1 is unique pairs, or we can use COUNT(*), same approach and result,
# just need to find all unique rows and pid is PRIMARY_KEY, so it's better to filter on it.
second_option: str = "SELECT lat, lon " \
                     "FROM insurance " \
                     "GROUP BY lat, lon " \
                     "HAVING COUNT(pid) = 1;"
second_data: Result = db.execute(text(second_option))
print("\nSecondOption")
for _ in second_data:
    print(_)

# Now we can just filter on that 2 options.
# Only extra part we need is to change type of the SUM(), because we're having FLOAT as column values,
# and if I want to use ROUND() I need this to be numeric, or I could leave it like SUM() without ROUND().
# But in this case if columns will change, or they're not having 2 digits after decimal it's going to be wrong.
# So it's better to just change type and calc ROUND()
postgresql_query: str = "SELECT ROUND(SUM(tiv_2016)::numeric, 2) AS tiv_2016 " \
                        "FROM insurance " \
                        "WHERE tiv_2015 IN (" \
                        "   SELECT tiv_2015" \
                        "   FROM insurance" \
                        "   GROUP BY tiv_2015" \
                        "   HAVING COUNT(tiv_2015) > 1" \
                        ")" \
                        "AND" \
                        "(lat, lon) IN (" \
                        "   SELECT lat, lon " \
                        "   FROM insurance " \
                        "   GROUP BY lat, lon" \
                        "   HAVING COUNT(pid) = 1" \
                        ");"
data: Result = db.execute(text(postgresql_query))
print("\nQuery")
for _ in data:
    print(_)
# For MySQL query I don't need to change type for SUM(), it's done automatically, or I would need to use CAST(),
# than it's should be ok with Post and Mysql both.


# Expected output:
# +----------+
# | tiv_2016 |
# +----------+
# | 45.00    |
# +----------+
