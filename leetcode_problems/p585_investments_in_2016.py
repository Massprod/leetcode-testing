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

