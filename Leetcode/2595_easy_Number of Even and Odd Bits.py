"""
Done 09.05.2024. Topics: Bit Manipulation
2595. Number of Even and Odd Bits
https://leetcode.com/problems/number-of-even-and-odd-bits/description/

You are given a positive integer n.
Let even denote the number of even indices in the binary representation of n (0-indexed) with value 1.
Let odd denote the number of odd indices in the binary representation of n (0-indexed) with value 1.
Return an integer array answer where answer = [even, odd].



Example 1:

Input: n = 17
Output: [2,0]
Explanation: The binary representation of 17 is 10001.
It contains 1 on the 0th and 4th indices.
There are 2 even and 0 odd indices.
Example 2:

Input: n = 2
Output: [0,1]
Explanation: The binary representation of 2 is 10.
It contains 1 on the 1st index.
There are 0 even and 1 odd indices.

!!!!! Note: Indices of binary representations start from the right
"""

# Runtime 19 ms Beats 40.00% of users with Python
# Memory 11.71 MB Beats 6.00% of users with Python

def evenOddBit2(n):
    """
    :type n: int
    :rtype: List[int]
    """
    s=bin(n)[2:][::-1]

    ev_=sum([1 for i in range(len(s)) if (s[i] == '1') and (i % 2 == 0)])
    od_=sum([1 for i in range(len(s)) if (s[i] == '1') and (i % 2 != 0)])
    return [ev_, od_]

# Runtime 18 ms Beats 50.00% of users with Python
# Memory 11.56 MB Beats 80.00% of users with Python
def evenOddBit(n):
    """
    :type n: int
    :rtype: List[int]
    """
    s=bin(n)[2:][::-1]
    ev_, od_ = 0, 0
    for i in range(len(s)):
        if (s[i] == '1'):
            if i % 2 == 0:
                ev_+=1
            else:
                od_+=1
    return [ev_, od_]


print(evenOddBit(2))
