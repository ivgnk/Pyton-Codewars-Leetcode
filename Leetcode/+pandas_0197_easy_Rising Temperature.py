"""
26.09.2024. Topisc: Pandas
197. Rising Temperature
Table: Weather
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this table.
There are no different rows with the same recordDate.
This table contains information about the temperature on a certain day.

Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).
Return the result table in any order.
The result format is in the following example.

Example 1:

Input:
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
Output:
+----+
| id |
+----+
| 2  |
| 4  |
+----+
Explanation:
In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
In 2015-01-04, the temperature was higher than the previous day (20 -> 30).
"""

import pandas as pd

# https://leetcode.com/problems/rising-temperature/solutions/5751145/pandas-simple/
def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values('recordDate', inplace=True)
    filtered_df = weather[
        (weather['temperature'].diff() > 0) &
        (weather['recordDate'].diff() == pd.Timedelta(days=1))
        ]
    return filtered_df[['id']]

# Wrong Answer - 13 / 15 testcases passed
# Weather =
# | id | recordDate | temperature |
# | -- | ---------- | ----------- |
# | 1  | 2000-12-14 | 3           |
# | 2  | 2000-12-16 | 5           |
def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    # https://www.codecamp.ru/blog/pandas-difference-between-rows/
    weather.sort_values(by='recordDate', ascending=True)
    t = weather[weather['temperature'].diff() > 0]
    return t[['id']]
