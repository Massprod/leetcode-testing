import pandas as pd


# Write a solution to find the ids of products that are both low fat and recyclable.
# Return the result table in any order.
# --------------
# Actually there's no reasons to populate for such easy cases,
# cuz I'm already done all DB tasks with SQL, and it's just redoing with pandas.
# Already know how to make DF and populate it, no reasons to repeat.


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    products = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]['product_id']
    return products[['product_id']]
