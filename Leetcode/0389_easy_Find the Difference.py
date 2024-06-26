"""
Done 28.04.2024
389. Find the Difference
https://leetcode.com/problems/find-the-difference/description/

You are given two strings s and t.
String t is generated by random shuffling string s and then add one more letter at a random position.
Return the letter that was added to t.

Example 1:
Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.

Example 2:
Input: s = "", t = "y"
Output: "y"
"""

# Runtime 14 ms Beats 82.68% of users with Python
# Memory 11.75 MB Beats 43.08% of users with Python

from collections import Counter
def findTheDifference(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    ls_ = len(s);    lt_ = len(t)
    sd = dict(Counter(s));    td = dict(Counter(t))
    sds = set(sd);    tds = set(td)
    if len(sds) == len(tds) and ls_ == 1 and t.count(s) == lt_:
        return list(sds)[0]
    lst = list(tds - sds)
    if len(lst) == 1:
        return list(tds - sds)[0]
    else:
        for k, v in td.items():
            if k not in sd:
                return k
            elif sd[k] - td[k] != 0:
                return k


print(findTheDifference( s ="ae", t = "aea"))

