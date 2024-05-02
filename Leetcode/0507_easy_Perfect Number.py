"""
Done 02.05.2024
507. Perfect Number
https://leetcode.com/problems/perfect-number/description/

A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.
A divisor of an integer x is an integer that can divide x evenly.
Given an integer n, return true if n is a perfect number, otherwise return false.

Example 1:
Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.

Example 2:
Input: num = 7
Output: false
"""

# Runtime 15 ms Beats 75.72% of users with Python
# Memory 11.97 MB Beats 26.88% of users with Python

# https://proghunter.ru/articles/how-to-find-all-divisors-of-a-number-in-python
import math
def find_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    d =sorted(divisors)[:-1]
    return d

def checkPerfectNumber(num):
    """
    :type num: int
    :rtype: bool
    """
    return sum(find_divisors(num))==num

print(checkPerfectNumber(28))