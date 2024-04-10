"""
2413. Smallest Even Multiple
https://leetcode.com/problems/smallest-even-multiple/description/

Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.

Example 1:
Input: n = 5
Output: 10
Explanation: The smallest multiple of both 5 and 2 is 10.

Example 2:
Input: n = 6
Output: 6
Explanation: The smallest multiple of both 6 and 2 is 6. Note that a number is a multiple of itself.
"""

# Runtime 8 ms Beats 88.95% of users with Python
# Memory 11.65 MB Beats 37.42% of users with Python

def smallestEvenMultiple(n):
    """
    :type n: int
    :rtype: int
    """
    if n % 2 == 0:
        return n
    else:
        return 2 * n
