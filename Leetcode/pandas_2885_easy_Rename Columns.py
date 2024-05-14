"""
Done 15.05.2024. Topics: Pandas
2885. Rename Columns

DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| id          | int    |
| first       | object |
| last        | object |
| age         | int    |
+-------------+--------+
Write a solution to rename the columns as follows:

id to student_id
first to first_name
last to last_name
age to age_in_years
The result format is in the following example.

Example 1:
Input:
+----+---------+----------+-----+
| id | first   | last     | age |
+----+---------+----------+-----+
| 1  | Mason   | King     | 6   |
| 2  | Ava     | Wright   | 7   |
| 3  | Taylor  | Hall     | 16  |
| 4  | Georgia | Thompson | 18  |
| 5  | Thomas  | Moore    | 10  |
+----+---------+----------+-----+
Output:
+------------+------------+-----------+--------------+
| student_id | first_name | last_name | age_in_years |
+------------+------------+-----------+--------------+
| 1          | Mason      | King      | 6            |
| 2          | Ava        | Wright    | 7            |
| 3          | Taylor     | Hall      | 16           |
| 4          | Georgia    | Thompson  | 18           |
| 5          | Thomas     | Moore     | 10           |
+------------+------------+-----------+--------------+
Explanation:
The column names are changed accordingly.

Hint 1
Consider using a build-in function in pandas
library with a dictionary to rename the columns as specified.
"""

# Runtime 579 ms Beats 69.94% of users with Pandas
# Memory 64.64 MB Beats 86.56% of users with Pandas

import pandas as pd
def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    # https://www.codecamp.ru/blog/pandas-rename-columns/
    # df.rename(columns = {' old_col1 ':' new_col1', 'old_col2 ':' new_col2 '}, inplace = True )
    students.rename(columns={'id':'student_id', 'first':'first_name','last':'last_name','age':'age_in_years'}, inplace = True)
    return students