from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from tasks_database.db import get_session


# SQL schema:
# DROP TABLE IF EXISTS accounts;
# Create table If Not Exists Accounts (account_id int, income int);
# Truncate table Accounts;
# insert into Accounts (account_id, income) values ('3', '108939');
# insert into Accounts (account_id, income) values ('2', '12747');
# insert into Accounts (account_id, income) values ('8', '87709');
# insert into Accounts (account_id, income) values ('6', '91796');
# --------------------
# Calculate the number of bank accounts of each salary category. The salary categories are:
#   - "Low Salary": All the salaries strictly less than $20000.
#   - "Average Salary": All the salaries in the inclusive range [$20000, $50000].
#   - "High Salary": All the salaries strictly greater than $50000.
# The result table must contain all three categories. If there are no accounts in a category, then report 0.
# Return the result table in any order.

db: Session = next(get_session())
db.execute(
    text(
        "DROP TABLE IF EXISTS accounts; "
        "CREATE TABLE IF NOT EXISTS accounts("
        "   account_id INTEGER, "
        "   income INTEGER "
        ");"
        "INSERT INTO accounts(account_id, income) "
        "VALUES "
        "('3', '108939'),"
        "('2', '12747'),"
        "('8', '87709'),"
        "('6', '91796');"
    )
)
db.commit()

# No idea how we can pivot table if we just search all required data.
# Because I can find everything,
#   but it will lead to table with columns -> Low, Avg, High salaries and rows with their count.
# But we can create table with just 1 row and place COUNT() on that row.

# SQL query:
# -- table with single row of low_salary --
# SELECT 'Low Salary' AS category, COUNT(account_id) AS accounts_count
# FROM accounts
# WHERE income < 20000
# UNION ALL
# -- table with single row of avg_salary --
# SELECT 'Average Salary' AS category, COUNT(account_id) AS accounts_count
# FROM accounts
# WHERE income BETWEEN 20000 AND 50000
# UNION ALL
# -- table with single row of avg_salary --
# SELECT 'High Salary' AS category, COUNT(account_id) AS accounts_count
# FROM accounts
# WHERE income > 50000;

data: Result = db.execute(
    text(
        "SELECT 'Low Salary' AS category,  COUNT(account_id) AS accounts_count "
        "FROM accounts "
        "WHERE income < 20000 "
        "UNION ALL "
        "SELECT 'Average Salary' AS category, COUNT(account_id) AS accounts_count "
        "FROM accounts "
        "WHERE income BETWEEN 20000 AND 50000 "
        "UNION ALL "
        "SELECT 'High Salary' AS category, COUNT(account_id) AS accounts_count "
        "FROM accounts "
        "WHERE income > 50000;"
    )
)

for _ in data:
    print(_)

# Expected output:
# +----------------+----------------+
# | category       | accounts_count |
# +----------------+----------------+
# | Low Salary     | 1              |
# | Average Salary | 0              |
# | High Salary    | 3              |
# +----------------+----------------+
