import pandas as pd


# Write a solution to find the names of all the salespersons
#   who did not have any orders related to the company with the name "RED".
# Return the result table in any order.
# ----------------
# SalesPerson table:
# +----------+------+--------+-----------------+------------+
# | sales_id | name | salary | commission_rate | hire_date  |
# +----------+------+--------+-----------------+------------+
# | 1        | John | 100000 | 6               | 4/1/2006   |
# | 2        | Amy  | 12000  | 5               | 5/1/2010   |
# | 3        | Mark | 65000  | 12              | 12/25/2008 |
# | 4        | Pam  | 25000  | 25              | 1/1/2005   |
# | 5        | Alex | 5000   | 10              | 2/3/2007   |
# +----------+------+--------+-----------------+------------+
# Company table:
# +--------+--------+----------+
# | com_id | name   | city     |
# +--------+--------+----------+
# | 1      | RED    | Boston   |
# | 2      | ORANGE | New York |
# | 3      | YELLOW | Boston   |
# | 4      | GREEN  | Austin   |
# +--------+--------+----------+
# Orders table:
# +----------+------------+--------+----------+--------+
# | order_id | order_date | com_id | sales_id | amount |
# +----------+------------+--------+----------+--------+
# | 1        | 1/1/2014   | 3      | 4        | 10000  |
# | 2        | 2/1/2014   | 4      | 5        | 5000   |
# | 3        | 3/1/2014   | 1      | 1        | 50000  |
# | 4        | 4/1/2014   | 1      | 4        | 25000  |
# +----------+------------+--------+----------+--------+
# Output:
# +------+
# | name |
# +------+
# | Amy  |
# | Mark |
# | Alex |
# +------+


def sales_persons(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Company ID can be  changed, so we need to get it first ->
    com_id: pd.DataFrame = company[company['name'] == 'RED'].reset_index()
    # -> reset_index(), to always get [0] correctly.
    com_id: int = com_id['com_id'][0]
    # Delete everything except orders from RED company.
    orders = orders[orders['com_id'] == com_id]
    # LEFT JOIN -> com_id will be set only for equal sales_id, and we're having only incorrect in orders ->
    sales_person = sales_person.merge(orders, left_on='sales_id', right_on='sales_id', how='left')
    # -> incorrect is set, and correct is N\A, just filter them.
    sales_person = sales_person[sales_person['com_id'].isna()]
    return sales_person[['name']]
