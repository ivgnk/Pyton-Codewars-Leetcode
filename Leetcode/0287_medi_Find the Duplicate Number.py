"""
Done 04.05.2024
287. Find the Duplicate Number
https://leetcode.com/problems/find-the-duplicate-number/description/

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [3,3,3,3,3]
Output: 3
"""

from collections import Counter

# Runtime 590 ms Beats 8.33% of users with Python
# Memory 37.64 MB Beats 5.09% of users with Python
# Runtime 579 ms Beats 10.23% of users with Python
# Memory 37.97 MB Beats 5.09% of users with Python
def findDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dd = dict(Counter(nums))
    for k, v in dd.items():
        if v >= 2: return k


