"""
1512. Number of Good Pairs
https://leetcode.com/problems/number-of-good-pairs/description/

Given an array of integers nums, return the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:
Input: nums = [1,2,3]
Output: 0
"""

# Runtime 12 ms Beats 84.54% of users with Python
# Memory 11.76 MB Beats 11.70% of users with Python

def numIdenticalPairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = 0; ll = len(nums)
    for i in range(ll):
        for j in range(i + 1, ll):
            if nums[i] == nums[j]: n = n + 1
    return n
