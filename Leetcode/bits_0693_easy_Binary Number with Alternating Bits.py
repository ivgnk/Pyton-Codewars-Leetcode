"""
Done 22.09.2024. Topics: Bit Manipulation
693. Binary Number with Alternating Bits
https://leetcode.com/problems/binary-number-with-alternating-bits/description/

Given a positive integer, check whether it has alternating bits: namely,
if two adjacent bits will always have different values.

Example 1:
Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101

Example 2:
Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.

Example 3:
Input: n = 11
Output: false
Explanation: The binary representation of 11 is: 1011.

Constraints:
1 <= n <= 2**31 - 1
"""

# Runtime 4 ms Beats 98.94%
# Memory 11.62 MB Beats 28.57%
def hasAlternatingBits(n):
    """
    :type n: int
    :rtype: bool
    """
    s = bin(n)[2:]
    print(s)
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            return False
    return True

print(hasAlternatingBits(5))