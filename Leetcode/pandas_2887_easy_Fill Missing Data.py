"""
Done 22.05.2024. Topics: Pandas, Database
2887. Fill Missing Data
https://leetcode.com/problems/fill-missing-data/description/

DataFrame products
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | object |
| quantity    | int    |
| price       | int    |
+-------------+--------+
Write a solution to fill in the missing value as 0 in the quantity column.
The result format is in the following example.


Example 1:
Input:
+-----------------+----------+-------+
| name            | quantity | price |
+-----------------+----------+-------+
| Wristwatch      | None     | 135   |
| WirelessEarbuds | None     | 821   |
| GolfClubs       | 779      | 9319  |
| Printer         | 849      | 3051  |
+-----------------+----------+-------+
Output:
+-----------------+----------+-------+
| name            | quantity | price |
+-----------------+----------+-------+
| Wristwatch      | 0        | 135   |
| WirelessEarbuds | 0        | 821   |
| GolfClubs       | 779      | 9319  |
| Printer         | 849      | 3051  |
+-----------------+----------+-------+
Explanation:
The quantity for Wristwatch and WirelessEarbuds are filled by 0.

Hint 1
Consider using a build-in function in pandas library to fill the missing values of specified columns
"""

import pandas as pd

# Runtime 586 ms Beats 65.00% of users with Pandas
# Memory 65.64 MB Beats 8.76% of users with Pandas

# stackoverflow.com/questions/10715519/conditionally-fill-column-values-based-on-another-columns-value-in-pandas
def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'].loc[products['quantity'].isnull()] = 0
    return products



