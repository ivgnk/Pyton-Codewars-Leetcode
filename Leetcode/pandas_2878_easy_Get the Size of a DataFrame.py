"""
Done 23.05.2024. Topics: Pandas, Database
2878. Get the Size of a DataFrame
https://leetcode.com/problems/get-the-size-of-a-dataframe/description/

DataFrame players:
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| player_id   | int    |
| name        | object |
| age         | int    |
| position    | object |
| ...         | ...    |
+-------------+--------+
Write a solution to calculate and display the number of rows and columns of players.
Return the result as an array:
[number of rows, number of columns]
The result format is in the following example.

Example 1:
Input:
+-----------+----------+-----+-------------+--------------------+
| player_id | name     | age | position    | team               |
+-----------+----------+-----+-------------+--------------------+
| 846       | Mason    | 21  | Forward     | RealMadrid         |
| 749       | Riley    | 30  | Winger      | Barcelona          |
| 155       | Bob      | 28  | Striker     | ManchesterUnited   |
| 583       | Isabella | 32  | Goalkeeper  | Liverpool          |
| 388       | Zachary  | 24  | Midfielder  | BayernMunich       |
| 883       | Ava      | 23  | Defender    | Chelsea            |
| 355       | Violet   | 18  | Striker     | Juventus           |
| 247       | Thomas   | 27  | Striker     | ParisSaint-Germain |
| 761       | Jack     | 33  | Midfielder  | ManchesterCity     |
| 642       | Charlie  | 36  | Center-back | Arsenal            |
+-----------+----------+-----+-------------+--------------------+
Output:
[10, 5]
Explanation:
This DataFrame contains 10 rows and 5 columns.
"""

# www.geeksforgeeks.org/get-the-number-of-rows-and-number-of-columns-in-pandas-dataframe/

import pandas as pd
from typing import List

# Runtime 548 ms Beats 80.81% of users with Pandas
# Memory 66.00 MB Beats 8.59% of users with Pandas

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    rows = len(players.axes[0])
    cols = len(players.axes[1])
    return [rows, cols]
