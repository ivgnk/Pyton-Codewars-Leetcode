"""
You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have.
Each character in stones is a type of stone you have.
You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0
"""

# Runtime 13 ms Beats 67.92% of users with Python
# Memory 11.70 MB Beats 57.82% of users with Python

def numJewelsInStones(jewels, stones):
    """
    :type jewels: str
    :type stones: str
    :rtype: int
    """
    return(sum(1 for s1 in stones if s1 in jewels))
