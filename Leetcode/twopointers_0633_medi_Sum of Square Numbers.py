"""
Done 07.05.2024. Topics: Math, Two Pointers, Binary Search
633. Sum of Square Numbers
Given a non-negative integer c,
decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
Input: c = 3
Output: false
"""

# Runtime 61 ms Beats 66.50%
# Memory 11.37 MB Beats 99.01%

from math import sqrt
def judgeSquareSum(c):
    """
    :type c: int
    :rtype: bool
    """
    i=0; j=int(sqrt(c))
    while i<=j:
        n = i * i + j * j
        if n==c: return True
        if n>c: j=j-1
        else: i=i+1
    return False

print(judgeSquareSum(2))