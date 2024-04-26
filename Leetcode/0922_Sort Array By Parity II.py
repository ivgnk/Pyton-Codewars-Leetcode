"""
922. Sort Array By Parity II
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
Return any answer array that satisfies this condition.

Example 1:
Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
Example 2:

Input: nums = [2,3]
Output: [2,3]
"""

# Runtime 143 ms Beats 67.97% of users with Python
# Memory 13.71 MB Beats 36.36% of users with Python

def sortArrayByParityII(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ll = len(nums)
    eve_ = [i for i in nums if i % 2 == 0]
    odd_ = [i for i in nums if i % 2 != 0]
    return [eve_[i // 2] if i % 2 == 0 else odd_[i // 2] for i in range(ll)]
