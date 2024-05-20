"""
Done 20.05.2024. Topics: Math
263. Ugly Number
https://leetcode.com/problems/ugly-number/

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return true if n is an ugly number.

Example 1:
Input: n = 6
Output: true
Explanation: 6 = 2 × 3

Example 2:
Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Example 3:
Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.
"""

# Runtime 13 ms Beats 69.55% of users with Python
# Memory 11.70 MB Beats 42.06% of users with Python
# Runtime 11 ms Beats 83.53% of users with Python
# Memory 11.67 MB Beats 42.06% of users with Python

def isUgly(n):
    """
    :type n: int
    :rtype: bool
    """
    if n <= 0: return False
    while n>2:
        if n%2==0: n = n//2
        elif n%3==0: n = n//3
        elif n%5==0: n = n//5
        else: return False
    return True

