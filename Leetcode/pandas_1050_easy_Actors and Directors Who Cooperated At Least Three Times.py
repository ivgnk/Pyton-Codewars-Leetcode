"""
20.06.2024. Topics: Pandas, Database
1050. Actors and Directors Who Cooperated At Least Three Times
https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/description/

Table: ActorDirector
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| actor_id    | int     |
| director_id | int     |
| timestamp   | int     |
+-------------+---------+
timestamp is the primary key (column with unique values) for this table.
Write a solution to find all the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.
Return the result table in any order.
The result format is in the following example.

Example 1:
Input:
ActorDirector table:
+-------------+-------------+-------------+
| actor_id    | director_id | timestamp   |
+-------------+-------------+-------------+
| 1           | 1           | 0           |
| 1           | 1           | 1           |
| 1           | 1           | 2           |
| 1           | 2           | 3           |
| 1           | 2           | 4           |
| 2           | 1           | 5           |
| 2           | 1           | 6           |
+-------------+-------------+-------------+
Output:
+-------------+-------------+
| actor_id    | director_id |
+-------------+-------------+
| 1           | 1           |
+-------------+-------------+
Explanation: The only pair is (1, 1) where they cooperated exactly 3 times.
"""

import pandas as pd


# stackoverflow.com/questions/8916302/selecting-across-multiple-columns-with-pandas
# https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/solutions/3820292/pandas-solution/
# Runtime 496 ms Beats 78.07%
# Memory 66.72 MB Beats 37.92%

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director.groupby(['actor_id', 'director_id']).agg(count=('director_id', 'count')).reset_index()
    df = df[df['count'] >= 3]
    return df[['actor_id', 'director_id']]

def actors_and_directors2(actor_director: pd.DataFrame) -> pd.DataFrame:
    # get collaboration counts for each actor/director pair
    actor_director = actor_director.groupby(['actor_id', 'director_id']).size().to_frame('collab_count').reset_index()
    # keep only those who collaborated at least 3 times
    actor_director = actor_director[actor_director.collab_count > 2][['actor_id', 'director_id']]
    return actor_director

# Runtime 388 ms Beats 93.80%
# Memory 66.89 MB Beats 29.24%
# https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/solutions/3858400/2-line-pandas/
def actors_and_directors3(actor_director: pd.DataFrame) -> pd.DataFrame:
    z=actor_director.groupby(['actor_id','director_id']).count().reset_index()
    return z[z['timestamp']>=3][['actor_id','director_id']]
