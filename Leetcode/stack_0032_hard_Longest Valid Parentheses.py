"""
32. Longest Valid Parentheses
https://leetcode.com/problems/longest-valid-parentheses/description/

Given a string containing just the characters '(' and ')',
return the length of the longest valid (well-formed) parentheses
substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0
"""


def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """
    ll=len(s)
    if ll<2: return False

    m = 0; smax = 0
    for i in range(len(s)):
        if s[i]=='(':
            m=m+1
            smax=max(smax,m)
        else:
            m=m-1
            smax=max(smax,m)
    return smax
