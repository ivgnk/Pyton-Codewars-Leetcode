"""
Done 22.05.2024. Topics: Pandas, Database
2883. Drop Missing Data
https://leetcode.com/problems/drop-missing-data/description/

DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+
There are some rows having missing values in the name column.
Write a solution to remove the rows with missing values.
The result format is in the following example.

Example 1:
Input:
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 32         | Piper   | 5   |
| 217        | None    | 19  |
| 779        | Georgia | 20  |
| 849        | Willow  | 14  |
+------------+---------+-----+
Output:
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 32         | Piper   | 5   |
| 779        | Georgia | 20  |
| 849        | Willow  | 14  |
+------------+---------+-----+
Explanation:
Student with id 217 havs empty value in the name column, so it will be removed.
"""

import pandas as pd

# Runtime 629 ms Beats 56.71% of users with Pandas
# Memory 66.50 MB Beats 5.13% of users with Pandas
# https://leetcode.com/problems/drop-missing-data/solutions/4920076/best-pandas-solution-with-simple-meaning-of-every-line

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=['name'])


# Wrong Answer -- 11 / 21 testcases passed

# https://stackoverflow.com/questions/45512763/python-pandas-dataframe-remove-all-rows-where-none-is-the-value-in-any-column
# https://saturncloud.io/blog/python-pandas-conditionally-delete-rows/
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.mask(students.eq('None')).dropna()
    # return students[students['name'] != None]
