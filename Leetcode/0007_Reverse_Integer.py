'''
7. Reverse Integer (Medium)
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21

https://leetcode.com/problems/reverse-integer/
'''

def reverse(x:int):
    """
    :type x: int
    :rtype: int
    """
    mmin = -2147483648 # (-2)**31
    mmax =  2147483647 # 2**31 - 1
    the_str = str(x)
    if x<0: the_str = the_str[1:]
    the_str = the_str[::-1]
    x_rev = int(the_str)
    if x < 0: x_rev =- x_rev
    if (x_rev < mmin) or (x_rev > mmax): return 0
    return x_rev

print(reverse(-123))