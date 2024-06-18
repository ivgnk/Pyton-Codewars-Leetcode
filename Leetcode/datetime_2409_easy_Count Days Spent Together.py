"""
Done 18.06.2024. Topics: Math, String
2409. Count Days Spent Together
https://leetcode.com/problems/count-days-spent-together/description/

Alice and Bob are traveling to Rome for separate business meetings.
You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob.
Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive),
while Bob will be in the city from the dates arriveBob to leaveBob (inclusive).
Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.

Return the total number of days that Alice and Bob are in Rome together.
You can assume that all dates occur in the same calendar year, which is not a leap year.
Note that the number of days per month can be represented as:
[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].

Example 1:
Input: arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
Output: 3
Explanation: Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3.

Example 2:
Input: arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
Output: 0
Explanation: There is no day when Alice and Bob are in Rome together, so we return 0.

Hint 1
For a given day, determine if Alice or Bob or both are in Rome.
Hint 2
Brute force all 365 days for both Alice and Bob.
"""

# Runtime 10 ms Beats 87.18%
# Memory 11.70 MB Beats 76.92%
from datetime import datetime
def countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob):
    """
    :type arriveAlice: str
    :type leaveAlice: str
    :type arriveBob: str
    :type leaveBob: str
    :rtype: int
    """
    if arriveBob > leaveAlice or arriveAlice > leaveBob: return 0
    s = "%m-%d"
    aa = datetime.strptime(arriveAlice, s).date()
    la = datetime.strptime(leaveAlice, s).date()
    ab = datetime.strptime(arriveBob, s).date()
    lb = datetime.strptime(leaveBob, s).date()
    if ab < aa and lb > la: return (la - aa).days + 1
    if ab > aa and lb > la: return (la - ab).days + 1
    if ab < aa and la > lb: return (lb - aa).days + 1
    if ab >= aa and la > lb: return (lb - ab).days + 1
    return abs(ab - la).days + 1

print(countDaysTogether(arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"))
print(countDaysTogether(arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"))
print(countDaysTogether(arriveAlice = "10-20", leaveAlice = "12-22", arriveBob = "06-21", leaveBob = "07-05"))

