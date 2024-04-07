'''
0018. 4Sum
https://leetcode.com/problems/4sum/description/

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
'''

#  Time Limit Exceeded -- 275 / 294 testcases passed

def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    ll = len(nums)
    res=[]
    for i in range(ll):
        for j in range(i+1, ll):
            for k in range(j+1, ll):
                for l in range(k + 1, ll):
                    if i != j:
                        if j != k:
                            if k != l:
                                if i != k:
                                    if i != l:
                                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                                            res.append(sorted([nums[i], nums[j], nums[k], nums[l]]))
    # https://stackoverflow.com/questions/3724551/uniqueness-for-list-of-lists
    res = [list(x) for x in set(tuple(x) for x in res)]
    return res

# print(fourSum(nums = [1,0,-1,0,-2,2], target = 0))
print(fourSum(nums = [2,2,2,2,2], target =8))