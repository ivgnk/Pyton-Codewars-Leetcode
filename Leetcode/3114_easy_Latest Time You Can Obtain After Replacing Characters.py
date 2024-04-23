"""
3114. Latest Time You Can Obtain After Replacing Characters
https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/description/

You are given a string s representing a 12-hour format time where some of the digits (possibly none) are replaced with a "?".
12-hour times are formatted as "HH:MM", where HH is between 00 and 11, and MM is between 00 and 59.
The earliest 12-hour time is 00:00, and the latest is 11:59.
You have to replace all the "?" characters in s with digits such that the time we obtain by the resulting string is
a valid 12-hour format time and is the latest possible.
Return the resulting string.

Example 1:
Input: s = "1?:?4"
Output: "11:54"
Explanation: The latest 12-hour format time we can achieve by replacing "?" characters is "11:54".

Example 2:
Input: s = "0?:5?"
Output: "09:59"
Explanation: The latest 12-hour format time we can achieve by replacing "?" characters is "09:59".
"""

# Runtime 17 ms Beats 50.48% of users with Python
# Memory 11.70 MB Beats 65.22% of users with Python

def findLatestTime(s):
    """
    :type s: str
    :rtype: str
    """
    s1 = s.split(":")
    s2, s3 = s1
    if s2 == "??":
        s2 = "11"
    elif s1[0].find("?") >= 0:
        for i in range(9, -1, -1):
            s2 = s1[0].replace("?", str(i))
            if s2 < "12": break
    if s3 == "??":
        s3 = "59"
    elif s1[1].find("?") >= 0:
        for i in range(9, -1, -1):
            s3 = s1[1].replace("?", str(i))
            if s3 <= "59": break
    return ":".join([s2, s3])


print(findLatestTime("?3:12"))