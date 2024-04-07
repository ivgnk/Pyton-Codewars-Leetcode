'''
1523. Count Odd Numbers in an Interval Range
https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/

Given two non-negative integers low and high.
Return the count of odd numbers between low and high (inclusive).

Example 1:
Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].

Example 2:
Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9]
'''

# Runtime 10 ms Beats 84.64% of users with Python
# Memory 11.60 MB Beats 71.43% of users with Python

def countOdds(low, high):
    """
    :type low: int
    :type high: int
    :rtype: int
    """
    hl = high - low
    if hl == 1: return 1
    hb0 = high % 2 == 0;    hb0n = not hb0
    lb0 = low % 2 == 0;    lb0n = not lb0
    if hb0n and lb0n:
        add = 1
    elif (hb0 and lb0n) or (hb0n and lb0):
        add = 1
    else:
        add = 0
    return hl // 2 + add