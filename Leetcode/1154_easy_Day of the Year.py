'''
Given a string date representing a Gregorian calendar date formatted
as YYYY-MM-DD, return the day number of the year.

Example 1:
Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.

Example 2:
Input: date = "2019-02-10"
Output: 41
'''

from datetime import date

# https://stackoverflow.com/questions/620305/convert-year-month-day-to-day-of-year-in-python

# Runtime 63 ms Beats 35.29% of users with Python
# Memory 11.87 MB Beats 11.76% of users with Python

def dayOfYear(d):
    """
    :type date: str
    :rtype: int
    """
    s=d.split('-')
    year=int(s[0]); month=int(s[1]); day=int(s[2])
    if month==day and day==1: return 1
    # www.geeksforgeeks.org/manipulate-date-and-time-with-the-datetime-module-in-python/
    d1 = date(year, month, day)
    d2 = date(year, 1, 1)
    dd=str(d1-d2)
    dd2=int(dd.split()[0])
    return dd2+1

print(dayOfYear("2019-01-09"))