"""
Done 17.05.2024. Topics: Bit Manipulation
2220. Minimum Bit Flips to Convert Number
https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/

A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1 to 0.
For example, for x = 7, the binary representation is 111 and we may choose any bit
(including any leading zeros not shown) and flip it.
We can flip the first bit from the right to get 110,
flip the second bit from the right to get 101,
flip the fifth bit from the right (a leading zero) to get 10111, etc.
Given two integers start and goal, return the minimum number of bit flips to convert start to goal.

Example 1:
Input: start = 10, goal = 7
Output: 3
Explanation: The binary representation of 10 and 7 are 1010 and 0111 respectively. We can convert 10 to 7 in 3 steps:
- Flip the first bit from the right: 1010 -> 1011.
- Flip the third bit from the right: 1011 -> 1111.
- Flip the fourth bit from the right: 1111 -> 0111.
It can be shown we cannot convert 10 to 7 in less than 3 steps. Hence, we return 3.

Example 2:
Input: start = 3, goal = 4
Output: 3
Explanation: The binary representation of 3 and 4 are 011 and 100 respectively. We can convert 3 to 4 in 3 steps:
- Flip the first bit from the right: 011 -> 010.
- Flip the second bit from the right: 010 -> 000.
- Flip the third bit from the right: 000 -> 100.
It can be shown we cannot convert 3 to 4 in less than 3 steps. Hence, we return 3.

Hint 1
If the value of a bit in start and goal differ, then we need to flip that bit.
Hint 2
Consider using the XOR operation to determine which bits need a bit flip.
"""

# Runtime 6 ms Beats 97.74% of users with Python
# Memory 11.57 MB Beats 72.32% of users with Python

def minBitFlips(start, goal):
    """
    :type start: int
    :type goal: int
    :rtype: int
    """
    s=bin(start)[2:]; ls=len(s)
    g=bin(goal)[2:];  lg=len(g)
    ll=max(ls,lg)
    if ll>ls:
        s='0'*(ll - ls) + s
    elif ll>lg:
        g='0'*(ll - lg) + g
    print(s,g)

    return sum([s[i]!=g[i] for i in range(ll)])

print(minBitFlips(10,7))