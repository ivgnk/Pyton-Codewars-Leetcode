'''
Re-resolutions 03.05.2024

191. Number of 1 Bits
https://leetcode.com/problems/number-of-1-bits/description/

Write a function that takes the binary representation of a positive integer and returns the number of
set bits it has (also known as the Hamming weight).

Example 1:
Input: n = 11
Output: 3
Explanation: The input binary string 1011 has a total of three set bits.

Example 2:
Input: n = 128
Output: 1
Explanation: The input binary string 10000000 has a total of one set bit.
'''

# Runtime 7 ms Beats 97.34% of users with Python
# Memory 11.51 MB Beats 70.39% of users with Python

def hammingWeight1(n):
    """
    :type n: int
    :rtype: int
    """
    s = bin(n);  s = s[2:]
    return sum([1 for s1 in s if s1 == '1'])


# Runtime 9 ms Beats 90.12% of users with Python
# Memory 11.51 MB Beats 72.24% of users with Python
def hammingWeight(n):
    return bin(n).count('1')
