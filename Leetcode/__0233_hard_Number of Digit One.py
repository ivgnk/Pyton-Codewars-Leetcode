"""
233. Number of Digit One
https://leetcode.com/problems/number-of-digit-one/description/

Given an integer n, count the total number of digit 1
appearing in all non-negative integers less than or equal to n.
Example 1:

Input: n = 13
Output: 6
Example 2:

Input: n = 0
Output: 0
"""

#  Memory Limit Exceeded -- 35 / 38 testcases passed

def countDigitOne2(n):
    """
    :type n: int
    :rtype: int
    """
    nn=0
    for i in range(n+1):
        s=str(i)
        for s1 in s:
            if s1=='1': nn=nn+1
    return nn

def countDigitOne(n):
    nn=0
    for i in range(n+1):
        nn=nn+str(i).count('1')
    return nn

print(countDigitOne(13))