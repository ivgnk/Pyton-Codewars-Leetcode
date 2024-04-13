"""
3105. Longest Strictly Increasing or Strictly Decreasing Subarray
https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/

You are given an array of integers nums. Return the length of the longest subarray  of nums which is either
strictly increasing or strictly decreasing

Example 1:
Input: nums = [1,4,3,3,2]
Output: 2
Explanation:
The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].
The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].
Hence, we return 2.

Example 2:
Input: nums = [3,3,3,3]
Output: 1
Explanation:
The strictly increasing subarrays of nums are [3], [3], [3], and [3].
The strictly decreasing subarrays of nums are [3], [3], [3], and [3].
Hence, we return 1.

Example 3:
Input: nums = [3,2,1]
Output: 3
Explanation:
The strictly increasing subarrays of nums are [3], [2], and [1].
The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].
Hence, we return 3.
"""

# 25 ms Beats 74.58% of users with Python
# Memory 11.56 MB Beats 75.83% of users with Python

# More challenges
# 1566 easy Detect Pattern of Length M Repeated K or More Times
# 1260 easy Shift 2D Grid
# 775 medium Global and Local Inversions

from icecream import ic
def longestMonotonicSubarray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll=len(nums)
    lmax=0; lmaxc=1
    lmin=0; lminc=1
    for i in range(1,ll):
        if nums[i]>nums[i-1]:
            lmaxc=lmaxc+1
            lminc=1
        elif nums[i]==nums[i-1]:
            lmaxc=1
            lminc=1
        else:
            lminc = lminc + 1
            lmaxc=1
        lmin = max(lmin, lminc)
        lmax = max(lmax, lmaxc)
        ic(i,nums[i],lminc,lmaxc)
    return max(lmax,lmin,lminc,lmaxc)

# print(longestMonotonicSubarray([1,4,3,3,2]))
# print(longestMonotonicSubarray([3,3,3,3]))
# print(longestMonotonicSubarray([3,2,1]))
print(longestMonotonicSubarray([1,10,10]))
