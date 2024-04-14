"""
43. Multiply Strings
https://leetcode.com/problems/multiply-strings/description/

Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"
"""

# Runtime 29 ms Beats 95.65% of users with Python3
# Memory 16.44 MB Beats# 93.81%
# of users with Python3
def multiply(self, num1: str, num2: str) -> str:
    n1 = int(num1)
    n2 = int(num2)
    return str(n1 * n2)

# Runtime 32 ms Beats 88.83% of users with Python3
# Memory 16.65 MB Beats 27.47% of users with Python3
def multiply2(self, num1: str, num2: str) -> str:
    return str(eval(f'{num1}*{num2}'))
