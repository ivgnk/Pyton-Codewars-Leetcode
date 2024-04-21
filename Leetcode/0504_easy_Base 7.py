"""
504. Base 7
https://leetcode.com/problems/base-7/description/

Given an integer num, return a string of its base 7 representation.

Example 1:
Input: num = 100
Output: "202"

Example 2:
Input: num = -7
Output: "-10"
"""

# https://stackoverflow.com/questions/74961556/how-to-convert-the-given-number-into-base7-representation-using-the-process-of-r

# def base7(n: int) -> str:
#     frac = n % 7
#     rest = n // 7
#     return base7(rest) + str(frac) if rest else str(frac)

# Runtime 37 ms Beats 44.50% of users with Python3
# Memory 16.51 MB Beats 67.53% of users with Python3

def base7(n: int) -> str:
    if n == 0:
        return ""
    quotient, remainder = divmod(n, 7)
    return base7(quotient) + str(remainder)

def convertToBase7(num):
    """
    :type num: int
    :rtype: str
    """
    if num == 0: return "0"
    n=abs(num)
    sgn = "" if num>=0 else "-"
    return sgn+base7(n)

print(convertToBase7(100))
print(convertToBase7(-7))