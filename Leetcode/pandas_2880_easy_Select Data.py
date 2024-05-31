"""
Done 01.06.2024. Topics: Pandas
2880. Select Data
https://leetcode.com/problems/select-data/description/

DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+
Write a solution to select the name and age of the student with student_id = 101.
The result format is in the following example.

Example 1:
Input:
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 101        | Ulysses | 13  |
| 53         | William | 10  |
| 128        | Henry   | 6   |
| 3          | Henry   | 11  |
+------------+---------+-----+
Output:
+---------+-----+
| name    | age |
+---------+-----+
| Ulysses | 13  |
+---------+-----+
Explanation:
Student Ulysses has student_id = 101, we select the name and age.
"""

# Runtime 579 ms Beats 76.55% of users with Pandas
# Memory 66.09 MB Beats 29.33% of users with Pandas

import pandas as pd
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    t = students.loc[students['student_id ']==101]
    # www.geeksforgeeks.org/how-to-select-multiple-columns-in-a-pandas-dataframe/
    return t[['name','age']]
