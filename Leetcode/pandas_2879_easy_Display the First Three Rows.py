"""
Done 09.05.2024. Topics: Pandas
2879. Display the First Three Rows
https://leetcode.com/problems/display-the-first-three-rows/description/

DataFrame: employees
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| employee_id | int    |
| name        | object |
| department  | object |
| salary      | int    |
+-------------+--------+
Write a solution to display the first 3 rows of this DataFrame.
"""

# Runtime 572 ms Beats 71.40% of users with Pandas
# Memory 65.37 MB Beats 52.58% of users with Pandas

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
     return employees.head(n=3)