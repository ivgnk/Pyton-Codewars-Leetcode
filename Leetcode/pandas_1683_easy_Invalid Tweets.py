"""
Done 22.05.2024. Topics: Pandas, Database
1683. Invalid Tweets
https://leetcode.com/problems/invalid-tweets/description/

SQL Schema
Pandas Schema
Table: Tweets

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
tweet_id is the primary key (column with unique values) for this table.
This table contains all the tweets in a social media app.

Write a solution to find the IDs of the invalid tweets.
The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.
Return the result table in any order.
The result format is in the following example.

Example 1:
Input:
Tweets table:
+----------+----------------------------------+
| tweet_id | content                          |
+----------+----------------------------------+
| 1        | Vote for Biden                   |
| 2        | Let us make America great again! |
+----------+----------------------------------+
Output:
+----------+
| tweet_id |
+----------+
| 2        |
+----------+
Explanation:
Tweet 1 has length = 14. It is a valid tweet.
Tweet 2 has length = 32. It is an invalid tweet.
"""
import pandas as pd

# Runtime 554 ms Beats 87.49% of users with Pandas
# Memory 66.38 MB Beats 48.74% of users with Pandas

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    t = tweets.loc[tweets['content'].str.len() > 15]
    return pd.DataFrame(t['tweet_id'])




# https://leetcode.com/problems/invalid-tweets/solutions/3853009/pandas-mysql-an-effortless-simple-approach/
def invalid_tweets2(tweets: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where the length of 'content' is strictly greater than 15
    invalid_tweets_df = tweets[tweets['content'].str.len() > 15]

    # Select only the 'tweet_id' column from the invalid tweets DataFrame
    result_df = invalid_tweets_df[['tweet_id']]

    return result_df