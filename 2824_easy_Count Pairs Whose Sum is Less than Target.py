"""
2824. Count Pairs Whose Sum is Less than Target
https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/

Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.

Example 1:
Input: nums = [-1,1,2,3,1], target = 2
Output: 3
Explanation: There are 3 pairs of indices that satisfy the conditions in the statement:
- (0, 1) since 0 < 1 and nums[0] + nums[1] = 0 < target
- (0, 2) since 0 < 2 and nums[0] + nums[2] = 1 < target
- (0, 4) since 0 < 4 and nums[0] + nums[4] = 0 < target
Note that (0, 3) is not counted since nums[0] + nums[3] is not strictly less than the target.
"""

# Runtime 24 ms Beats 88.10% of users with Python
# Memory 11.74 MB Beats 12.30% of users with Python

def countPairs(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    n = 0; ll = len(nums)
    for i in range(ll):
        for j in range(i + 1, ll):
            if nums[i]+nums[j]<target: n=n+1
    return n