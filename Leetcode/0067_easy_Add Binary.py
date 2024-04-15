"""
67. Add Binary
https://leetcode.com/problems/add-binary/description/

Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
"""

# Runtime 38 ms Beats 53.53% of users with Python3
# Memory 16.48 MB Beats 95.82% of users with Python3

def addBinary(a: str, b: str) -> str:
    # dat = bin(int(a,2)+int(b,2))
    # return dat[2:]
    return bin(int(a, 2) + int(b, 2))[2:]

print(addBinary(a = "11", b = "1"))
print(addBinary(a = "1010", b = "1011"))
