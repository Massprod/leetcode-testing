
# DROP TABLE IF EXISTS tweets;
# Create table If Not Exists Tweets(tweet_id int, content varchar(50));
# Truncate table Tweets;
# insert into Tweets (tweet_id, content) values ('1', 'Vote for Biden');
# insert into Tweets (tweet_id, content) values ('2', 'Let us make America great again!');
# -----------------------------
# Find the IDs of the invalid tweets.
# The tweet is invalid if the number of characters used in the content of the tweet
#   is strictly greater than 15.
# Return the result table in any order.

# SQL query:
# SELECT tweet_id
# FROM tweets
# WHERE LENGTH(content) > 15;
