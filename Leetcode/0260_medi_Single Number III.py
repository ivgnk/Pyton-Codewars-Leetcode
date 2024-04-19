"""
260. Single Number III
https://leetcode.com/problems/single-number-ii/description/

Given an integer array nums, in which exactly two elements appear
only once and all the other elements appear exactly twice.
Find the two elements that appear only once. You can return the answer in any order.
You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
"""

# Runtime 38 ms Beats 68.63% of users with Python
# Memory 14.99 MB Beats 5.09% of users with Python

from collections import Counter
from icecream import ic
def singleNumber(nums):
    dd=dict(Counter(nums))
    lst=[]
    for k,v in dd.items():
        if v==1: lst.append(k)
    return lst

ic(singleNumber(nums = [1,2,1,3,2,5]))
