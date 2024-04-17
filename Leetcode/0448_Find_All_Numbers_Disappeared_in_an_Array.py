'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]
'''

# Runtime 251 ms Beats 76.84% of users with Python3
# Memory 29.09 MB Beats 9.07% of users with Python3

def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # n = len(nums)
    # return [i for i in range(1, n + 1) if i not in nums]
    return list(set(range(1, len(nums) + 1)) - set(nums))


print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))