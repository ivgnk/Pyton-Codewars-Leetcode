"""
2544. Alternating Digit Sum
https://leetcode.com/problems/alternating-digit-sum/description/

You are given a positive integer n. Each digit of n has a sign according to the following rules:
The most significant digit is assigned a positive sign.
Each other digit has an opposite sign to its adjacent digits.
Return the sum of all digits with their corresponding sign.

Example 1:
Input: n = 521
Output: 4
Explanation: (+5) + (-2) + (+1) = 4.

Example 2:
Input: n = 111
Output: 1
Explanation: (+1) + (-1) + (+1) = 1.

Example 3:
Input: n = 886996
Output: 0
Explanation: (+8) + (-8) + (+6) + (-9) + (+9) + (-6) = 0.
"""

# Runtime 8 ms Beats 89.63% of users with Python
# Memory 11.51 MB Beats 73.17% of users with Python

def alternateDigitSum(n):
    """
    :type n: int
    :rtype: int
    """
    ns=str(n)
    nn=0; sgn=1
    for i in range(len(ns)):
        nn += int(ns[i])*sgn
        sgn=-sgn
    return nn

print(alternateDigitSum(521))
