"""
Done 05.10.2024
2229. Check if an Array Is Consecutive
Given an integer array nums , return true if nums is consecutive,
otherwise return false .

An array is consecutive if it contains every number in the range
[x,  x + n  - 1]   (inclusive), where x
is the minimum number in the array and n is the length of the array.
"""

from icecream import ic
def isConsecutive(nums):
    mmin=min(nums)
    ll=len(nums)
    return nums==[i for i in range(mmin,mmin+ll)]

ic(isConsecutive([2, 3, 4, 5, 6]))
ic(isConsecutive([4, 5, 7, 8]))

# https://romankurnovskii.com/ru/tracks/algorithms-101/leetcode/easy/2229/
def isConsecutive2(nums):
    mi, mx = min(nums), max(nums)
    n = len(nums)
    return len(set(nums)) == n and mx == mi + n - 1

ic(isConsecutive2([2, 3, 4, 5, 6]))
ic(isConsecutive2([4, 5, 7, 8]))

# 5 Best Ways to Check if Array Elements are Consecutive in Python
# https://blog.finxter.com/5-best-ways-to-check-if-array-elements-are-consecutive-in-python/

