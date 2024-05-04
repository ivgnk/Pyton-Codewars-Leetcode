"""
Done 05.05.2024
476. Number Complement
https://leetcode.com/problems/number-complement/description/

The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.

Example 1:
Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits),
and its complement is 010. So you need to output 2.

Example 2:
Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits),
and its complement is 0. So you need to output 0.
"""

# Runtime 14 ms Beats 57.79% of users with Python
# Memory 11.58 MB Beats 73.38% of users with Python

def findComplement(num):
    """
    :type num: int
    :rtype: int
    """
    s = bin(num)[2:]
    ns = ''.join(['1' if i == '0' else '0'  for i in s])
    return int(ns,2)

print(findComplement(5))
