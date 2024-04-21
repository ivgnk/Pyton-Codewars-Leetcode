"""
540. Single Element in a Sorted Array
https://leetcode.com/problems/single-element-in-a-sorted-array/description/

You are given a sorted array consisting of only integers where every element
appears exactly twice, except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10
"""

from icecream import ic
from collections import Counter
def singleNonDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dd=dict(Counter(nums))
    sorted_x = sorted(dd.items(), key=lambda kv: kv[1])
    return sorted_x[0][0]
    # for k,v in dd.items():
    #     if v==1: return k

ic(singleNonDuplicate([1,1,2,3,3,4,4,8,8]))