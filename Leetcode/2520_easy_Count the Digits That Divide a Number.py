"""
Done 02.05.2024
2520. Count the Digits That Divide a Number
https://leetcode.com/problems/count-the-digits-that-divide-a-number/description/

Given an integer num, return the number of digits in num that divide num.
An integer val divides nums if nums % val == 0.

Example 1:
Input: num = 7
Output: 1
Explanation: 7 divides itself, hence the answer is 1.

Example 2:
Input: num = 121
Output: 2
Explanation: 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.
"""

# Runtime 13 ms Beats 56.99% of users with Python
# Memory 11.61 MB Beats 36.01% of users with Python
# Runtime 10 ms Beats 79.37% of users with Python
# Memory 11.74 MB Beats 10.14% of users with Python

from collections import Counter
def countDigits(num):
    """
    :type num: int
    :rtype: int
    """
    dd = dict(Counter(str(num)))
    return sum([v for k, v in dd.items() if num % int(k) == 0])


print(countDigits(1248))