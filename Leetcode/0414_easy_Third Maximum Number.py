"""
Done 02.05.2024
414. Third Maximum Number
https://leetcode.com/problems/third-maximum-number/description/

Given an integer array nums, return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number.

Example 1:
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

Example 2:
Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
"""

# Runtime 24 ms Beats 94.72% of users with Python
# Memory 12.39 MB Beats 93.53% of users with Python

def thirdMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n1 = sorted(set(nums))
    if len(n1) < 3:
        return n1[-1]
    else:
        return n1[-3]