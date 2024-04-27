"""
Done 27.04.2024
459. Repeated Substring Pattern
https://leetcode.com/problems/repeated-substring-pattern/

Given a string s, check if it can be constructed by taking a substring of it
and appending multiple copies of the substring together.

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
"""

from collections import Counter

def get_n(n):
    res=[]
    divisor =2
    while (divisor<n):
        if (n % divisor)==0:
            res.append([divisor, n // divisor])
        divisor=divisor+1
    return res

# Runtime 40 ms Beats 43.16% of users with Python
# Memory 11.94 MB Beats 59.42% of users with Python

def repeatedSubstringPattern(s):
    """
    :type s: str
    :rtype: bool
    """
    lens=len(s)
    if lens == 1: return False
    if s.count(s[0])==lens: return True
    llen = get_n(lens)
    print(llen)
    for llen1 in llen:
        if s[:llen1[0]]*llen1[1]==s: return True
    return False



print(repeatedSubstringPattern("abaababaab"))


