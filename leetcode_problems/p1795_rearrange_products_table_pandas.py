import pandas as pd


# Write a solution to rearrange the Products table so that each row has (product_id, store, price).
# If a product is not available in a store, do not include a row with that product_id
#   and store combination in the result table.
# Return the result table in any order.
# Input:
# +------------+--------+--------+--------+
# | product_id | store1 | store2 | store3 |
# +------------+--------+--------+--------+
# | 0          | 95     | 100    | 105    |
# | 1          | 70     | null   | 80     |
# +------------+--------+--------+--------+


Products: pd.DataFrame = pd.DataFrame(
    [],
    columns=['product_id', 'store1', 'store2', 'store3']
).astype(
    {
        'product_id': 'int64',
        'store1': 'int64',
        'store2': 'int64',
        'store3': 'int64',
    }
)

Products['product_id'] = [0, 1]
Products['store1'] = [95, 70]
Products['store2'] = [100, None]
Products['store3'] = [105, 80]

# Output:
# +------------+--------+-------+
# | product_id | store  | price |
# +------------+--------+-------+
# | 0          | store1 | 95    |
# | 0          | store2 | 100   |
# | 0          | store3 | 105   |
# | 1          | store1 | 70    |
# | 1          | store3 | 80    |
# +------------+--------+-------+


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    products = products.melt(
        id_vars=['product_id'],
        value_vars=['store1', 'store2', 'store3'],
        var_name='store',
        value_name='price',
    )
    products.dropna(inplace=True)
    return products


# https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.melt.html
print(rearrange_products_table(Products))
