import pandas as pd


# Write a solution to calculate the number of bank accounts for each salary category.
# The salary categories are:
#   "Low Salary": All the salaries strictly less than $20000.
#   "Average Salary": All the salaries in the inclusive range [$20000, $50000].
#   "High Salary": All the salaries strictly greater than $50000.
# The result table must contain all three categories.
# If there are no accounts in a category, return 0.
# Return the result table in any order.
# ---------------------
# Accounts table:
# +------------+--------+
# | account_id | income |
# +------------+--------+
# | 3          | 108939 |
# | 2          | 12747  |
# | 8          | 87709  |
# | 6          | 91796  |
# +------------+--------+
# Output:
# +----------------+----------------+
# | category       | accounts_count |
# +----------------+----------------+
# | Low Salary     | 1              |
# | Average Salary | 0              |
# | High Salary    | 3              |
# +----------------+----------------+


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    # Filter everything on conditions and count it.
    low_sal: int = len(accounts[(accounts['income'] < 20000)].index)
    # ! <= value <= ! <- restricted, always one by one check.
    average_sal: int = len(accounts[(accounts['income'] <= 50000) & (accounts['income'] >= 20000)].index)
    high_sal: int = len(accounts[(accounts['income'] > 50000)].index)
    # Building new DF:
    new: pd.DataFrame = pd.DataFrame(columns=['category', 'accounts_count'])
    new['category'] = ['Low Salary', 'Average Salary', 'High Salary']
    new['accounts_count'] = [low_sal, average_sal, high_sal]
    return new
