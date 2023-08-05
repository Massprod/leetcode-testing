import pandas as pd


# Write a solution to find the rank of the scores.
# The ranking should be calculated according to the following rules:
# The scores should be ranked from the highest to the lowest.
# If there is a tie between two scores, both should have the same ranking.
# After a tie, the next ranking number should be the next consecutive integer value.
# In other words, there should be no holes between ranks.
# Return the result table ordered by score in descending order.
# Scores table:
# +----+-------+
# | id | score |
# +----+-------+
# | 1  | 3.50  |
# | 2  | 3.65  |
# | 3  | 4.00  |
# | 4  | 3.85  |
# | 5  | 4.00  |
# | 6  | 3.65  |
# +----+-------+


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # dense_rank with() with descending ranking, standard output is Float ->
    # -> so we need to change for INT.
    scores['rank'] = scores['score'].rank(method='dense', ascending=False).astype(int)
    # Extra sorting -> ! Return the result table ordered by score in descending order !.
    scores.sort_values(by='score', ascending=False, inplace=True)
    return scores[['score', 'rank']]


# https://pandas.pydata.org/docs/reference/api/pandas.Series.rank.html <- rank()
