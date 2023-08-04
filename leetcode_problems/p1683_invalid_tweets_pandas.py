import pandas as pd


# Write a solution to find the IDs of the invalid tweets.
# The tweet is invalid if the number of characters used in the content
#   of the tweet is strictly greater than 15.
# Return the result table in any order.
# +----------+----------------------------------+
# | tweet_id | content                          |
# +----------+----------------------------------+
# | 1        | Vote for Biden                   |
# | 2        | Let us make America great again! |
# +----------+----------------------------------+


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets = tweets[tweets['content'].str.len() > 15]
    return tweets[['tweet_id']]
