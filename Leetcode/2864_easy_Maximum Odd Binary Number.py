"""
Done 08.05.2024. Topics: Math, String, Greedy
2864. Maximum Odd Binary Number
https://leetcode.com/problems/maximum-odd-binary-number/description/

You are given a binary string s that contains at least one '1'.
You have to rearrange the bits in such a way that the resulting binary number
is the maximum odd binary number that can be created from this combination.

Return a string representing the maximum odd binary number that can be created from the given combination.
Note that the resulting string can have leading zeros.

Example 1:
Input: s = "010"
Output: "001"
Explanation: Because there is just one '1', it must be in the last position. So the answer is "001".

Example 2:
Input: s = "0101"
Output: "1001"
Explanation: One of the '1's must be in the last position. The maximum number that can be made with the remaining digits is "100". So the answer is "1001".

Hint 1
The binary representation of an odd number contains '1' in the least significant place.
"""

# Runtime 14 ms Beats 86.20% of users with Python
# Memory 11.75 MB Beats 27.91% of users with Python

def maximumOddBinaryNumber(s):
    """
    :type s: str
    :rtype: str
    """
    c0=s.count('0');  c1=s.count('1')
    if c1==1:
        return '0'*c0+'1'
    else:
        return '1'*(c1-1)+'0'*c0+'1'
