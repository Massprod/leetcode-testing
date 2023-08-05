import pandas as pd


# Write a solution to find the customer_number for the customer who has placed the largest number of orders.
# The test cases are generated so that exactly one customer will have placed more orders than any other customer.
# --------------------
# Orders table:
# +--------------+-----------------+
# | order_number | customer_number |
# +--------------+-----------------+
# | 1            | 1               |
# | 2            | 2               |
# | 3            | 3               |
# | 4            | 3               |
# +--------------+-----------------+
# Output:
# +-----------------+
# | customer_number |
# +-----------------+
# | 3               |
# +-----------------+


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # Unique case with empy_input.
    if len(orders.index) == 0:
        return orders[['customer_number']]
    # GroupBy to count (every customer_number + order_number) pair.
    orders['count'] = orders.groupby(by=['customer_number'])['order_number'].transform('count')
    # Filter any customers with less than max(count).
    orders = orders[orders['count'] == max(orders['count'])]
    # Delete duplicates.
    orders.drop_duplicates(subset=['customer_number'], inplace=True)
    return orders[['customer_number']]
