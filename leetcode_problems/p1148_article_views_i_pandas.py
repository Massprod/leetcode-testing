import pandas as pd


# Write a solution to find all the authors that viewed at least one of their own articles.
# Return the result table sorted by id in ascending order.
# +------------+-----------+-----------+------------+
# | article_id | author_id | viewer_id | view_date  |
# +------------+-----------+-----------+------------+
# | 1          | 3         | 5         | 2019-08-01 |
# | 1          | 3         | 6         | 2019-08-02 |
# | 2          | 7         | 7         | 2019-08-01 |
# | 2          | 7         | 6         | 2019-08-02 |
# | 4          | 7         | 1         | 2019-07-22 |
# | 3          | 4         | 4         | 2019-07-21 |
# | 3          | 4         | 4         | 2019-07-21 |
# +------------+-----------+-----------+------------+


def article_vies(views: pd.DataFrame) -> pd.DataFrame:
    # views = views.query("author_id == viewer_id")
    # Didn't worked at first, hmm. ^^Equal approach.
    views = views[(views['author_id'] == views['viewer_id'])]
    views = views[['author_id']].rename(
        columns={
            'author_id': 'id'
        }
    )
    # There's no DISTINCT, so it's extra drop_duplicates()
    views = views.drop_duplicates()
    views.sort_values(by='id', ascending=True, inplace=True)
    return views
