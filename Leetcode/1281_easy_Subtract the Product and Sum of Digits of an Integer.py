'''
1281. Subtract the Product and Sum of Digits of an Integer
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/

Given an integer number n, return the difference between the product of its digits and the sum of its digits.

Example 1:
Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15

Example 2:
Input: n = 4421
Output: 21
Explanation:
Product of digits = 4 * 4 * 2 * 1 = 32
Sum of digits = 4 + 4 + 2 + 1 = 11
Result = 32 - 11 = 21
'''

#  Runtime 3 ms Beats 99.82% of users with Python
#  Memory 11.70 MB Beats 43.62% of users with Python

def subtractProductAndSum(n):
    """
    :type n: int
    :rtype: int
    """
    s = str(n);  ssum = 0;   pprod = 1
    for s1 in s:
        i = int(s1)
        ssum = ssum + i
        pprod = pprod * i
    return pprod - ssum

