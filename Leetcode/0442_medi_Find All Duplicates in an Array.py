"""
442. Find All Duplicates in an Array
https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

Given an integer array nums of length n where all the integers of nums are in the range [1, n]
and each integer appears once or twice, return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant extra space.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:
Input: nums = [1,1,2]
Output: [1]

Example 3:
Input: nums = [1]
Output: []
"""

# Runtime 296 ms Beats 13.31% of users with Python
# Memory 23.72 MB Beats 5.70% of users with Python

from collections import Counter
def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    dd=dict(Counter(nums))
    return [k for k,v in dd.items() if v==2]