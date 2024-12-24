"""
24.12.2024. Topics: Database
595. Big Countries
https://leetcode.com/problems/big-countries/description/

Table: World
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |
+-------------+---------+
name is the primary key (column with unique values) for this table.
Each row of this table gives information about the name of a country,
the continent to which it belongs, its area, the population, and its GDP value.

A country is big if:
- it has an area of at least three million (i.e., 3000000 km2), or
- it has a population of at least twenty-five million (i.e., 25000000).
Write a solution to find the name, population, and area of the big countries.
Return the result table in any order.

The result format is in the following example.

Example 1:

Input:
World table:
+-------------+-----------+---------+------------+--------------+
| name        | continent | area    | population | gdp          |
+-------------+-----------+---------+------------+--------------+
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
+-------------+-----------+---------+------------+--------------+
Output:
+-------------+------------+---------+
| name        | population | area    |
+-------------+------------+---------+
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |
+-------------+------------+---------+

area >= 3000000 or( we use | operator for or) population >= 25000000
https://leetcode.com/problems/big-countries/solutions/6181344/soumya-shastri-by-w2tbd8frqx-zmoh/
"""

import pandas as pd
import numpy as np
# Runtime 264 ms Beats 94.38%
# Memory 68.30 MB Beats 85.22%

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    res = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    return res[['name', 'population', 'area']]

def big_countries2(world: pd.DataFrame) -> pd.DataFrame:
    world['bigornot']=np.where((world['area']>=3000000) | (world['population']>=25000000),1,0)
    out = world[world['bigornot']==1][['name','population','area']]
    return out

def big_countries3(world: pd.DataFrame) -> pd.DataFrame:
    return world[(world['population'] >= 25E6) | (world['area'] >= 3E6)][['name','population','area']]