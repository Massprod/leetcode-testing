import pandas as pd


# Write a solution to report the number of customers who had at least one bill
#   with an amount strictly greater than 500.
# ---------------
# Store table:
# +---------+-------------+--------+
# | bill_id | customer_id | amount |
# +---------+-------------+--------+
# | 6       | 1           | 549    |
# | 8       | 1           | 834    |
# | 4       | 2           | 394    |
# | 11      | 3           | 657    |
# | 13      | 3           | 257    |
# +---------+-------------+--------+
# Output:
# +------------+
# | rich_count |
# +------------+
# | 2          |
# +------------+


def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    # Filter everything with less|equal 500.
    store = store[(store['amount'] > 500)]
    # Count every unique customer, returns list of unique_values.
    uniques: int = len(store['customer_id'].unique())
    # It's either create new DF or just reuse already given ->
    store.rename(
        columns={
            'customer_id': 'rich_count',
        },
        inplace=True,
    )
    # -> reset indexing after deleting rows ->
    store.reset_index(inplace=True)
    # -> reusing inputDF, by changing and returning [0]  row.
    store['rich_count'][0] = uniques
    return store[['rich_count']].iloc[0:1]
