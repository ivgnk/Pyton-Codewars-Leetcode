"""
Done 30.06.2024. Topics: Math
509. Fibonacci Number
https://leetcode.com/problems/fibonacci-number/description/

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


Constraints:
0 <= n <= 30
"""

# Runtime 42 ms Beats 43.91%
# Memory 16.40 MB Beats 91.97%
# Runtime 33 ms Beats 79.97%
# Memory 16.48 MB Beats 57.94%
def fib2(n):
    """
    :type n: int
    :rtype: int
    """
    ff = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]  #
    ffl = 10
    if n<ffl: return ff[n]
    else:
        for i in range(ffl,n+1):
            ff.append(ff[i-1]+ff[i-2])
        return ff[-1]


# Runtime 29 ms Beats 92.18%
# Memory 16.32 MB Beats 91.97%
ff = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]  #
def fib(n):
    """
    :type n: int
    :rtype: int
    """
    ffl=len(ff)
    if n<ffl: return ff[n]
    else:
        for i in range(ffl,n+1):
            ff.append(ff[i-1]+ff[i-2])
        return ff[-1]


print(fib(12))