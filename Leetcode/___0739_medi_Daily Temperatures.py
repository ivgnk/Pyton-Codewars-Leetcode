"""
Done 09.05.2024. Topics: Array, Stack, Monotonic Stack
739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/description/

Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to
wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
"""


# Time Limit Exceeded -- 34 / 48 testcases passed
def dailyTemperatures2(t):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    ll=len(t);  res=[]
    for i in range(ll):
        for j in range(i+1,ll):
            if t[i]<t[j]:
                res.append(j-i)
                break
        else: res.append(0)
    return res

# decision from https://leetcode.com/satyam_mishra13/
# Runtime 3477 ms Beats 5.02% of users with Python
# Memory 25.62 MB Beats 57.16% of users with Python

def dailyTemperatures3(temperatures):
    temps = dict()

    for i in range(30, 101):
        temps[i] = []

    for index, temp in enumerate(temperatures):
        temps[temp].append(index)

    ans = []
    for temp in temperatures:
        closestTemp = 0
        closestIndex = 0
        for i in range(temp + 1, 101):
            if temps[i]:
                if not closestIndex or closestIndex > temps[i][0]:
                    closestIndex = temps[i][0]
                    closestTemp = i
        if closestIndex == 0:
            temps[temp].pop(0)
            ans.append(0)
            continue
        ans.append(temps[closestTemp][0] - temps[temp].pop(0))

    return ans

# my decision on the base of https://leetcode.com/satyam_mishra13/
# Runtime 3081 ms Beats 5.01% of users with Python3
# Memory 30.52 MB Beats 74.64% of users with Python3
def dailyTemperatures(temperatures):
    temps = dict()
    for i in range(30, 101):
        temps[i] = []

    # temps = dict.fromkeys(range(30, 101),[])
    for index, temp in enumerate(temperatures):
        temps[temp].append(index)

    ans = []
    for temp in temperatures:
        closestTemp = 0
        closestIndex = 0
        i = temp + 1
        while i<101:
            if temps[i]:
                if not closestIndex or closestIndex > temps[i][0]:
                    closestIndex = temps[i][0]
                    closestTemp = i
            i=i+1
        if closestIndex == 0:
            temps[temp].pop(0)
            ans.append(0)
            continue
        ans.append(temps[closestTemp][0] - temps[temp].pop(0))

    return ans


print(dailyTemperatures([73,74,75,71,69,72,76,73]))