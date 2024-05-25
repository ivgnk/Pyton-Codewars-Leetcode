"""
Done 25.05.2024. Topics: String
392. Is Subsequence
https://leetcode.com/problems/is-subsequence/description/

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by
deleting some (can be none) of the characters without disturbing the relative positions
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
"""

# Runtime 11 ms Beats 83.36% of users with Python
# Memory 11.86 MB Beats 39.10% of users with Python

# https://docs-python.ru/tutorial/operatsii-tekstovymi-strokami-str-python/metod-str-find/
def isSubsequence(s, t):
# Wrong Answer -- 18 / 20 testcases passed
    index=-1
    for s1 in s:
        index=t.find(s1,index+1)
        if index==-1: return False
    else:
        return True


def isSubsequence3(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if t.find(s) >= 0: return True
    sets = set(s)
    sett = set(t)
    sr = sett - sets;    print(sr)
    tlist = list(t);    slist = list(s)
    tnew = []
    for i, ss in enumerate(tlist):
        if not (ss in sr):
            tnew.append(ss)
    print(tnew);    print(slist)
    return tnew == slist