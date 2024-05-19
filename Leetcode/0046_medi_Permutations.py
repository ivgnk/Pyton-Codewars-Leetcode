"""
Done 19.05.2024. Topics: Array, Backtracking
46. Permutations
https://leetcode.com/problems/permutations/description/

Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
"""

from itertools import permutations

# Runtime 20 ms Beats 60.27% of users with Python
# Memory 11.57 MB Beats 99.34% of users with Python

def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    return list(permutations(nums, len(nums)))
