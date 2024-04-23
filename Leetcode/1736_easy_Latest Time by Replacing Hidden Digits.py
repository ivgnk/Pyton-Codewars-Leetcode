"""
1736. Latest Time by Replacing Hidden Digits
https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/description/

You are given a string time in the form of  hh:mm, where some of the digits in the string are hidden (represented by ?).
The valid times are those inclusively between 00:00 and 23:59.
Return the latest valid time you can get from time by replacing the hidden digits.

Example 1:
Input: time = "2?:?0"
Output: "23:50"
Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.

Example 2:
Input: time = "0?:3?"
Output: "09:39"

Example 3:
Input: time = "1?:22"
Output: "19:22"
"""

# Runtime 6 ms Beats 95.65% of users with Python
# Memory 11.78 MB Beats 26.09% of users with Python

def maximumTime(time):
    """
    :type time: str
    :rtype: str
    """
    s1 = time.split(":")
    s2, s3 = s1
    if s2 == "??":
        s2 = "23"
    elif s1[0].find("?") >= 0:
        for i in range(9, -1, -1):
            s2 = s1[0].replace("?", str(i))
            if s2 < "24": break
    if s3 == "??":
        s3 = "59"
    elif s1[1].find("?") >= 0:
        for i in range(9, -1, -1):
            s3 = s1[1].replace("?", str(i))
            if s3 <= "59": break
    return ":".join([s2, s3])
