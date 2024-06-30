"""
Done 30.06.2024. Topics: Database
610. Triangle Judgement
https://leetcode.com/problems/triangle-judgement/description/

Table: Triangle

+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
| z           | int  |
+-------------+------+
In SQL, (x, y, z) is the primary key column for this table.
Each row of this table contains the lengths of three line segments.

Report for every three line segments whether they can form a triangle.
Return the result table in any order.
The result format is in the following example.

Example 1:
Input:
Triangle table:
+----+----+----+
| x  | y  | z  |
+----+----+----+
| 13 | 15 | 30 |
| 10 | 20 | 15 |
+----+----+----+
Output:
+----+----+----+----------+
| x  | y  | z  | triangle |
+----+----+----+----------+
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |
+----+----+----+----------+
"""

# Runtime 360 ms Beats 95.85%
# Memory 65.26 MB Beats 82.39%

import pandas as pd
def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle["triangle"]=""
    for i in range(len(triangle)):
        x = triangle["x"].iloc[i]
        y = triangle["y"].iloc[i]
        z = triangle["z"].iloc[i]
        b1 = x+y >z
        b2 = x+z >y
        b3 = y+z >x
        s = "Yes" if b1 and b2 and b3 else "No"
        triangle["triangle"][i]=s
    return triangle
