"""
Done 05.08.2024. Topics: Math, Combinatorics

2928. Distribute Candies Among Children I
https://leetcode.com/problems/distribute-candies-among-children-i/description/

You are given two positive integers n and limit.
Return the total number of ways to distribute n candies among 3 children such that no
child gets more than limit candies.

Example 1:
Input: n = 5, limit = 2
Output: 3
Explanation: There are 3 ways to distribute 5 candies such that no child gets more than 2 candies: (1, 2, 2), (2, 1, 2) and (2, 2, 1).

Example 2:
Input: n = 3, limit = 3
Output: 10
Explanation: There are 10 ways to distribute 3 candies such that no child gets more than 3 candies: (0, 0, 3), (0, 1, 2), (0, 2, 1), (0, 3, 0), (1, 0, 2), (1, 1, 1), (1, 2, 0), (2, 0, 1), (2, 1, 0) and (3, 0, 0).


Constraints:
1 <= n <= 50
1 <= limit <= 50

Hint 1
Use three nested for loops to check all the triplets.
"""

# Runtime 426 ms Beats 59.26%
# Memory 11.80 MB Beats 12.04%
# Runtime 432 ms Beats 59.26%
# Memory 11.51 MB Beats 64.81%
def distributeCandies(n, limit):
    """
    :type n: int
    :type limit: int
    :rtype: int
    """
    nn = 0; rn = range(limit + 1)
    for i in rn:
        in_ = i - n
        for j in rn:
            ij = in_ + j
            for k in rn:
                if ij == -k:
                    nn += 1
    return nn


# Runtime 511 ms Beats 56.48%
# Memory 11.70 MB Beats 12.04%
def distributeCandies(n, limit):
    """
    :type n: int
    :type limit: int
    :rtype: int
    """
    nn = 0;    rn = range(limit + 1)
    for i in rn:
        for j in rn:
            ij = i + j
            for k in rn:
                if (ij + k) == n:
                    nn += 1
    return nn


# Runtime 571 ms Beats 53.70%
# Memory 11.52 MB Beats 64.81%
def distributeCandies3(n, limit):
    """
    :type n: int
    :type limit: int
    :rtype: int
    """
    nn=0; rn = range(limit+1)
    for i in rn:
        for j in rn:
            for k in rn:
                if (i+j+k)==n:
                    nn+=1
    return nn

print(distributeCandies(n = 5, limit = 2))
print(distributeCandies(n = 3, limit = 3))

