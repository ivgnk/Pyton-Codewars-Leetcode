"""
Done 01.06.2024. Topics: Pandas
2886. Change Data Type
https://leetcode.com/problems/change-data-type/description/

DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
| grade       | float  |
+-------------+--------+
Write a solution to correct the errors:
The grade column is stored as floats, convert it to integers.
The result format is in the following example.

Example 1:
Input:
DataFrame students:
+------------+------+-----+-------+
| student_id | name | age | grade |
+------------+------+-----+-------+
| 1          | Ava  | 6   | 73.0  |
| 2          | Kate | 15  | 87.0  |
+------------+------+-----+-------+
Output:
+------------+------+-----+-------+
| student_id | name | age | grade |
+------------+------+-----+-------+
| 1          | Ava  | 6   | 73    |
| 2          | Kate | 15  | 87    |
+------------+------+-----+-------+
Explanation:
The data types of the column grade is converted to int.
"""

# Runtime 546 ms Beats 85.34% of users with Pandas
# Memory 65.65 MB Beats 25.91% of users with Pandas
import pandas as pd

# https://stackoverflow.com/questions/15891038/change-column-type-in-pandas
def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students[['grade']]=students[['grade']].astype(int)
    return students
