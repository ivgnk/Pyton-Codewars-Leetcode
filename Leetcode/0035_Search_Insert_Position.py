'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
https://leetcode.com/problems/search-insert-position/description/

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
'''


def searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if target<nums[0]: return 0;
    llen = len(nums)
    if target>nums[llen-1]: return llen;
    for i, dat in enumerate(nums):
        if dat == target:
            return i
        elif (nums[i] < target):
            curri = i + 1
    return curri
