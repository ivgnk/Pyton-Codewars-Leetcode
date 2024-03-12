'''
414. Third Maximum Number
https://leetcode.com/problems/third-maximum-number/description/

Given an integer array nums, return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number.
'''


def thirdMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1: return nums[0]
    if len(nums) == 2: return max(nums)

    sset = set(nums)
    res = sorted(list(sset))
    if len(res) == 1: return res[0]
    if len(res) == 1: return max(res)
    return res[len(res) - 3]

print(thirdMax([1,1,1]))