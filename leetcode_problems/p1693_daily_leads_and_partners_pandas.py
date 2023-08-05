import pandas as pd


# For each date_id and make_name, find the number of distinct lead_id's and distinct partner_id's.
# Return the result table in any order.
# ---------------------
# DailySales table:
# +-----------+-----------+---------+------------+
# | date_id   | make_name | lead_id | partner_id |
# +-----------+-----------+---------+------------+
# | 2020-12-8 | toyota    | 0       | 1          |
# | 2020-12-8 | toyota    | 1       | 0          |
# | 2020-12-8 | toyota    | 1       | 2          |
# | 2020-12-7 | toyota    | 0       | 2          |
# | 2020-12-7 | toyota    | 0       | 1          |
# | 2020-12-8 | honda     | 1       | 2          |
# | 2020-12-8 | honda     | 2       | 1          |
# | 2020-12-7 | honda     | 0       | 1          |
# | 2020-12-7 | honda     | 1       | 2          |
# | 2020-12-7 | honda     | 2       | 1          |
# +-----------+-----------+---------+------------+
# Output:
# +-----------+-----------+--------------+-----------------+
# | date_id   | make_name | unique_leads | unique_partners |
# +-----------+-----------+--------------+-----------------+
# | 2020-12-8 | toyota    | 2            | 3               |
# | 2020-12-7 | toyota    | 1            | 2               |
# | 2020-12-8 | honda     | 2            | 2               |
# | 2020-12-7 | honda     | 3            | 2               |
# +-----------+-----------+--------------+-----------------+


def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    # Count every unique pair of (date_id + make_name + lead_id).
    daily_sales['unique_leads'] = daily_sales.groupby(by=['date_id', 'make_name'])['lead_id'].transform('nunique')
    # Count every unique pair of (date_id + make_name + partner_id).
    daily_sales['unique_partners'] = daily_sales.groupby(by=['date_id', 'make_name'])['partner_id'].transform('nunique')
    # Delete any overlaps.
    daily_sales.drop_duplicates(subset=['date_id', 'make_name'], inplace=True)
    return daily_sales[['date_id', 'make_name', 'unique_leads', 'unique_partners']]


# A little bit off with row_lengths, but not me who's choosing names :).
