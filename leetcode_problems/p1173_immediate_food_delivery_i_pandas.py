import pandas as pd


# If the customer's preferred delivery date is the same as the order date,
#   then the order is called immediate; otherwise, it is called scheduled.
# Write a solution to find the percentage of immediate orders in the table,
#   rounded to 2 decimal places.
# ----------------------
# Delivery table:
# +-------------+-------------+------------+-----------------------------+
# | delivery_id | customer_id | order_date | customer_pref_delivery_date |
# +-------------+-------------+------------+-----------------------------+
# | 1           | 1           | 2019-08-01 | 2019-08-02                  |
# | 2           | 5           | 2019-08-02 | 2019-08-02                  |
# | 3           | 1           | 2019-08-11 | 2019-08-11                  |
# | 4           | 3           | 2019-08-24 | 2019-08-26                  |
# | 5           | 4           | 2019-08-21 | 2019-08-22                  |
# | 6           | 2           | 2019-08-11 | 2019-08-13                  |
# +-------------+-------------+------------+-----------------------------+
# Output:
# +----------------------+
# | immediate_percentage |
# +----------------------+
# | 33.33                |
# +----------------------+


def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    # All customers.
    all_: int = len(delivery.index)
    # Filter only those with immediate delivery ->
    immediate: pd.DataFrame = delivery[delivery['order_date'] == delivery['customer_pref_delivery_date']]
    # -> count them ->
    immediate_: int = len(immediate.index)
    # -> standard math:
    result: float = round((immediate_ / all_) * 100, 2)
    # It's simplier to just return new_DataFrame.
    return pd.DataFrame([result], columns=['immediate_percentage'])
