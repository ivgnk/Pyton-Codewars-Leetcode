"""
2552. Count Increasing Quadruplets
https://leetcode.com/problems/count-increasing-quadruplets/description/

Given a 0-indexed integer array nums of size n containing all numbers from 1 to n, return the number of increasing quadruplets.
A quadruplet (i, j, k, l) is increasing if:
0 <= i < j < k < l < n, and
nums[i] < nums[k] < nums[j] < nums[l].

Example 1:
Input: nums = [1,3,2,4,5]
Output: 2
Explanation:
- When i = 0, j = 1, k = 2, and l = 3, nums[i] < nums[k] < nums[j] < nums[l].
- When i = 0, j = 1, k = 2, and l = 4, nums[i] < nums[k] < nums[j] < nums[l].
There are no other quadruplets, so we return 2.

Example 2:
Input: nums = [1,2,3,4]
Output: 0
Explanation: There exists only one quadruplet with
i = 0, j = 1, k = 2, l = 3, but since nums[j] < nums[k], we return 0.
"""

# Time Limit Exceeded -- 66 / 121 testcases passed

def countQuadruplets(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll = len(nums); n = 0
    for i in range(ll):
        for j in range(i + 1, ll):
            if nums[i] < nums[j]:
                for k in range(j + 1, ll):
                    if nums[i] < nums[k] < nums[j]:
                        for l in range(k + 1, ll):
                            if nums[i] < nums[k] < nums[j] < nums[l]: n = n + 1
    return n


# print(countQuadruplets(nums = [1,3,2,4,5]))
print(countQuadruplets(nums = [1,2,3,4]))