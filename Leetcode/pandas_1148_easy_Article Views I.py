"""
Done 30.05.2024. Topics: Pandas
1148. Article Views I
https://leetcode.com/problems/article-views-i/description/

SQL Schema
Pandas Schema
Table: Views
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key (column with unique values) for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date.
Note that equal author_id and viewer_id indicate the same person.

Write a solution to find all the authors that viewed at least one of their own articles.
Return the result table sorted by id in ascending order.
The result format is in the following example.

Example 1:
Input:
Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+
Output:
+------+
| id   |
+------+
| 4    |
| 7    |
+------+
"""

data=[
[1, 3, 5,'2019-08-01'],
[1, 3, 6,'2019-08-02'],
[2, 7, 7,'2019-08-01'],
[2, 7, 6,'2019-08-02'],
[4, 7, 1,'2019-07-22'],
[3, 4, 4,'2019-07-21'],
[3, 4, 4,'2019-07-21']]
nm=['article_id','author_id','viewer_id','view_date']

import pandas as pd

def maketable():
    print('\n--def maketable--')
    p2=pd.DataFrame(data,columns=nm)
    print(p2)
    return p2

# Runtime 570 ms Beats 83.77% of users with Pandas
# Memory 66.86 MB Beats 45.86% of users with Pandas

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    nf=sorted(views[views['author_id']==views['viewer_id']]['author_id'].unique())
    return pd.DataFrame(nf,columns=['id'])

pd1=maketable()
print(article_views(pd1))
