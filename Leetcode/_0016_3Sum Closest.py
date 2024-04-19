"""
16. 3Sum Closest
https://leetcode.com/problems/3sum-closest/description/

Given an integer array nums of length n and an integer target,
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0)
"""

# Time Limit Exceeded -- 46 / 102 testcases passed

from itertools import permutations, combinations
def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    r=1e38
    perm=list(combinations(nums,3))
    ll=len(perm)
    for i in range(ll):
        s=sum(perm[i])
        r1=abs(s-target)
        if r1<r:
            r=r1
            mmin=s
        # print(i, perm[i], s,r1,mmin)
    return mmin


print(threeSumClosest(nums = [-1,2,1,-4], target = 1))
