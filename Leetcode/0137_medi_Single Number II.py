"""
137. Single Number II
https://leetcode.com/problems/single-number-ii/description/

Given an integer array nums where every element appears three times except for one, which appears exactly once.
Find the single element and return it.
You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

from collections import Counter
from icecream import ic
# def singleNumber2(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     nc = 0
#     while nc != 1:
#         nnn = nums[0]
#         nc = nums.count(nnn)
#         ic(nums,nc)
#         if nc == 1:
#             return nnn
#         else:
#             nums =  [value for value in nums if value != nnn]
#     return nums[0]

# Runtime 56 ms Beats 66.44% of users with Python3
# Memory 18.68 MB Beats 57.57% of users with Python3

def singleNumber(nums):
    dd=dict(Counter(nums))
    ic(dd)
    for k,v in dd.items():
        if v==1: return k

ic(singleNumber(nums = [0,1,0,1,0,1,99]))
