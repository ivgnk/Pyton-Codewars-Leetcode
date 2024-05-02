"""
Done 02.05.2024
189. Rotate Array
https://leetcode.com/problems/rotate-array/description/

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

# Runtime 163 ms Beats 46.43% of users with Python3
# Memory 28.02 MB Beats 35.94% of users with Python3

from copy import deepcopy
# https://pygame.ru/blog/python-tsiklicheskiy-sdvig-vpravo.php
def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    #   nums = nums[-k:] + nums[:-k]
    ll = len(nums)
    if ll <= 1: return nums
    n = deepcopy(nums)
    if ll == 2:
        if k % 2 != 0:
            nums[0] = n[1];  nums[1] = n[0]
    elif ll == 3:
        if k % 3 == 1: nums[0] = n[2]; nums[1] = n[0]; nums[2] = n[1]
        if k % 3 == 2: nums[0] = n[1]; nums[1] = n[2]; nums[2] = n[0]
    else:
        kn = k % ll
        for i in range(kn):
            nums[i] = n[-kn + i]
        for i in range(kn, ll):
            nums[i] = n[i - kn]


# print(rotate(nums = [1,2,3,4,5,6,7], k = 3))
print(rotate(nums = [-1,-100,3,99], k = 2))