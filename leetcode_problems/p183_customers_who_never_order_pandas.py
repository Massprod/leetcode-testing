import pandas as pd


# Write a solution to find all customers who never order anything.
# Return the result table in any order.
# Customers table:
# +----+-------+
# | id | name  |
# +----+-------+
# | 1  | Joe   |
# | 2  | Henry |
# | 3  | Sam   |
# | 4  | Max   |
# +----+-------+
# Orders table:
# +----+------------+
# | id | customerId |
# +----+------------+
# | 1  | 3          |
# | 2  | 1          |
# +----+------------+


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # isin() -> IN analog with pandas.
    customers = customers[~customers['id'].isin(orders['customerId'])]
    customers = customers.rename(
        columns={
            'name': 'Customers',
        }
    )
    return customers[['Customers']]


def find_customers_join(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Left|Right joins with pandas:
    customers = customers.merge(orders, left_on='id', right_on='customerId', how='left')
    # isna() -> Is None, filter everything except rows with None.
    customers = customers[customers['customerId'].isna()]
    customers = customers[['name']].rename(
        columns={
            'name': 'Customers'
        }
    )
    return customers
