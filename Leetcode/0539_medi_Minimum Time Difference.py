"""
539. Minimum Time Difference
https://leetcode.com/problems/minimum-time-difference/description/
Given a list of 24-hour clock time points in "HH:MM" format,
return the minimum minutes difference between any two time-points in the list.

Example 1:
Input: timePoints = ["23:59","00:00"]
Output: 1

Example 2:
Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
"""

# Runtime 48 ms Beats 89.47% of users with Python
# Memory 15.09 MB Beats 97.37% of users with Python

from icecream import ic
from collections import Counter
def findMinDifference(timePoints):
    """
    :type timePoints: List[str]
    :rtype: int
    """
    c=dict(Counter(timePoints))
    if c[next(iter(c))]>1: return 0
    ll = len(timePoints)
    t2=sorted(timePoints)
    ic(t2)
    t3=[tt.split(":") for tt in t2]
    t4=[int(tt[0])*60+int(tt[1]) for tt in t3]
    t12=12*60; t24 = 24*60
    mini=20000
    for i in range(1,ll):
        r=t4[i] - t4[i - 1]
        if (t4[i]<t12 and t4[i-1]<t12) or (t4[i]>t12 and t4[i-1]>t12):
            if r<mini: mini=r
        else:
            if r<t12:
                if r<mini: mini=r
            elif t24-r<mini:
                mini=t24-r
    mini=min(mini, t24-(t4[ll-1]-t4[0]))
    return mini

ic(findMinDifference(["00:00","04:00","22:00"]))
# ic(findMinDifference(timePoints = ["00:00","23:59","00:00","00:01","00:00"]))
# ic(findMinDifference(timePoints = ["23:59","00:00"]))
