"""
Done 18.06.2024. Topics: Math, String

1360. Number of Days Between Two Dates
https://leetcode.com/problems/number-of-days-between-two-dates/

Write a program to count the number of days between two dates.
The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

Example 1:
Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1

Example 2:
Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15

Hint 1
Create a function f(date) that counts the number of days from 1900-01-01 to date. How can we calculate the answer ?
Hint 2
The answer is just |f(date1) - f(date2)|.
Hint 3
How to construct f(date) ?
Hint 4
For each year from 1900 to year - 1 sum up 365 or 366 in case of leap years.
Then sum up for each month the number of days, consider the case when the current year is leap,
finally sum up the days.

"""

# https://leetcode.com/problems/number-of-days-between-two-dates/description/comments/2141764
from datetime import datetime

# Runtime 8 ms Beats 97.40%
# Memory 11.70 MB Beats 71.43%
def daysBetweenDates(date1, date2):
    s = "%Y-%m-%d"
    a = datetime.strptime(date1, s).date()
    b = datetime.strptime(date2, s).date()
    return abs(a - b).days


# Runtime 20 ms Beats 23.38%
# Memory 11.71 MB Beats 45.45%
# Runtime 18 ms Beats 33.77%
# Memory 11.98 MB Beats 7.79%

def daysBetweenDates2(date1, date2):
    """
    :type date1: str
    :type date2: str
    :rtype: int
    """
    a = datetime.strptime(date1, "%Y-%m-%d").date()
    b = datetime.strptime(date2, "%Y-%m-%d").date()
    return abs(a-b).days

print(daysBetweenDates(date1 = "2019-06-29", date2 = "2019-06-30"))
print(daysBetweenDates(date1 = "2020-01-15", date2 = "2019-12-31"))