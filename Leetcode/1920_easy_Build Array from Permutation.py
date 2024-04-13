"""
1920. Build Array from Permutation
https://leetcode.com/problems/build-array-from-permutation/description/

Given a zero-based permutation nums (0-indexed), build an array ans of the same length where
ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
"""

# 73 ms Beats 96.72% of users with Python
# Memory 11.96 MB Beats 32.71% of users with Python

def buildArray(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    return [nums[nums[i]] for i in range(len(nums))]