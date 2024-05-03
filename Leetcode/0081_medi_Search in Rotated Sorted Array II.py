"""
Done 03.05.2024
81. Search in Rotated Sorted Array II
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
You must decrease the overall operation steps as much as possible.
"""


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: bool
    """
    # Runtime 27 ms Beats 89.35% of users with Python
    # Memory 12.21 MB Beats 9.26% of users with Python
    if target not in nums:
        return False
    else:
        return True

print(search(nums = [2,5,6,0,0,1,2], target = 0))
