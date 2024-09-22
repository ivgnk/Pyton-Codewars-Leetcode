"""
Done 22.09.2024. Topics: Database, Pandas
619. Biggest Single Number
https://leetcode.com/problems/biggest-single-number/description/

Table: MyNumbers
+-------------+------+
| Column Name | Type |
+-------------+------+
| num         | int  |
+-------------+------+
This table may contain duplicates (In other words, there is no primary key for this table in SQL).
Each row of this table contains an integer.

A single number is a number that appeared only once in the MyNumbers table.
Find the largest single number. If there is no single number, report null.
The result format is in the following example.

Example 1:
Input:
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 3   |
| 3   |
| 1   |
| 4   |
| 5   |
| 6   |
+-----+
Output:
+-----+
| num |
+-----+
| 6   |
+-----+
Explanation: The single numbers are 1, 4, 5, and 6.
Since 6 is the largest single number, we return it.
Example 2:

Input:
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 7   |
| 7   |
| 3   |
| 3   |
| 3   |
+-----+
Output:
+------+
| num  |
+------+
| null |
+------+
Explanation: There are no single numbers in the input table so we return null.
"""

import pandas as pd
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html
# https://www.geeksforgeeks.org/find-maximum-values-position-in-columns-and-rows-of-a-dataframe-in-pandas/
# https://www.geeksforgeeks.org/different-ways-to-create-pandas-dataframe/

# Runtime 362 ms Beats 62.24%
# Memory 68.50 MB Beats 98.21%
# Runtime 344 ms Beats 77.68%
# Memory 69.75 MB Beats 36.86%
def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html
    d = my_numbers.drop_duplicates(subset=['num'], keep=False).max()
    return pd.DataFrame(d, columns=['num'])
