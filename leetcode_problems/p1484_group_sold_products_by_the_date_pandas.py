import pandas as pd


# Write a solution to find for each date the number of different products sold and their names.
# The sold products names for each date should be sorted lexicographically.
# Return the result table ordered by sell_date.
# ------------------
# Activities table:
# +------------+------------+
# | sell_date  | product     |
# +------------+------------+
# | 2020-05-30 | Headphone  |
# | 2020-06-01 | Pencil     |
# | 2020-06-02 | Mask       |
# | 2020-05-30 | Basketball |
# | 2020-06-01 | Bible      |
# | 2020-06-02 | Mask       |
# | 2020-05-30 | T-Shirt    |
# +------------+------------+
# Output:
# +------------+----------+------------------------------+
# | sell_date  | num_sold | products                     |
# +------------+----------+------------------------------+
# | 2020-05-30 | 3        | Basketball,Headphone,T-shirt |
# | 2020-06-01 | 2        | Bible,Pencil                 |
# | 2020-06-02 | 1        | Mask                         |
# +------------+----------+------------------------------+


def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    # Count every unique pair of (sell_date + product).
    activities['num_sold'] = activities.groupby(by=['sell_date'])['product'].transform('nunique')
    # GroupBy every unique pair of (sell_date + num_sold) ->
    activities = activities.groupby(by=['sell_date', 'num_sold'])
    # -> assign all products which corresponds with this pair as string ->
    # -> by default column == list of all values, we're using set() to remove duplicates ->
    # -> sorting ! sold products names for each date should be sorted lexicographically ! ->
    # -> join everything from a set in a string with ',' as delimiter.
    activities = activities.agg({'product': lambda x: ','.join(sorted(set(x)))})
    # Reset columns.
    activities.reset_index(inplace=True)
    # Sort -> ! Return the result table ordered by sell_date !
    activities.sort_values(by=['sell_date'])
    activities.rename(
        columns={
            'product': 'products',
        },
        inplace=True,
    )
    return activities


# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html
