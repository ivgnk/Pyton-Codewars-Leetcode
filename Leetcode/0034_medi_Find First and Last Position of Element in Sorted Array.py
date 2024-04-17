"""
34. Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.


Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
 """

# Runtime 53 ms Beats 82.38% of users with Python
# Memory 13.18 MB Beats 7.91% of users with Python

def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    ll = len(nums)
    res = [i for i in range(ll) if nums[i] == target]
    if res == []:
        return [-1, -1]
    else:
        ll2=len(res)
        if  ll2 == 1:
            return [res[0], res[0]]
        elif ll2>2:
            return [res[0], res[ll2-1]]
        else: return res