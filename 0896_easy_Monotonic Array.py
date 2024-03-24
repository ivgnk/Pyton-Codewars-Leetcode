'''
896. Monotonic Array
https://leetcode.com/problems/monotonic-array/description/

An array is monotonic if it is either monotone increasing or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
Given an integer array nums, return true if the given array is monotonic, or false otherwise.
'''

# Runtime 820 ms
# Beats 13.12% of users with Python
# Memory # 24.34 MB
# Beats 5.96% of users with Python

def isMonotonic(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    rasc = sorted(nums)
    rdsc = sorted(nums, reverse=True)
    if nums == rasc or nums == rdsc:
        return True
    else:
        return False

