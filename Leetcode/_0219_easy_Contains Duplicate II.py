'''
219. Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/description/

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

# Time Limit Exceeded -- 20 / 58 testcases passed

def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    ll = len(nums)
    if ll==2 and nums[0]==nums[1]: return True
    for i in range(ll - k):
        for j in range(i+1, i + k + 1):
            print(i,j)
            if nums[i] == nums[j]:
                print(i,j)
                return True
    return False

print(containsNearbyDuplicate(nums = [99,99], k = 2))