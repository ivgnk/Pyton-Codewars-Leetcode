'''
1185. Day of the Week
https://leetcode.com/problems/day-of-the-week/description/
Given a date, return the corresponding day of the week for that date.
The input is given as three integers representing the day, month and year respectively.
Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.



Example 1:
Input: day = 31, month = 8, year = 2019
Output: "Saturday"

Example 2:
Input: day = 18, month = 7, year = 1999
Output: "Sunday"

Example 3:
Input: day = 15, month = 8, year = 1993
Output: "Sunday"
'''

# Runtime 11 ms Beats 79.67% of users with Python
# Memory 11.78 MB Beats 16.26% of users with Python

import datetime
def dayOfTheWeek(day, month, year):
    """
    :type day: int
    :type month: int
    :type year: int
    :rtype: str
    """
    #  https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
    theday = datetime.datetime(year,month,day)
    # return  theday.isoweekday() - число
    d= theday.isoweekday()
    if d==1: return "Monday"
    elif d==2: return "Tuesday"
    elif d==3: return "Wednesday"
    elif d==4: return "Thursday"
    elif d==5: return "Friday"
    elif d==6: return "Saturday"
    elif d==7: return "Sunday"

print(dayOfTheWeek(day = 31, month = 8, year = 2019))