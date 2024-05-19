"""
Done 19.05.2024. Topics: Array, Backtracking
47. Permutations II
https://leetcode.com/problems/permutations-ii/description/

Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

# Runtime 43 ms Beats 40.59% of users with Python
# Memory 11.80 MB Beats 93.91% of users with Python
# Runtime 39 ms Beats 52.99% of users with Python
# Memory 11.94 MB Beats 65.16% of users with Python
# Runtime 34 ms Beats 74.97% of users with Python
# Memory 11.92 MB Beats 65.16% of users with Python

from itertools import permutations

def permuteUnique(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    return set(permutations(nums, len(nums)))