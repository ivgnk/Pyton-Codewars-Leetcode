"""
Done 28.06.2024. Topics: Array, Hash Table
961. N-Repeated Element in Size 2N Array
https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/

You are given an integer array nums with the following properties:
nums.length == 2 * n.
nums contains n + 1 unique elements.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times.

Example 1:
Input: nums = [1,2,3,3]
Output: 3

Example 2:
Input: nums = [2,1,2,5,3,2]
Output: 2

Example 3:
Input: nums = [5,1,5,2,5,3,5,4]
Output: 5
"""

# Runtime 153 ms Beats 58.19%
# Memory 13.00 MB Beats 15.95%
# Runtime 150 ms Beats 69.83%
# Memory 12.67 MB Beats 78.45%
# Runtime 135 ms Beats 99.14%
# Memory 13.05 MB Beats 15.95%
def repeatedNTimes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dd=dict()
    for i in range(len(nums)):
        if nums[i] in dd:
            return nums[i]
        else:
            dd[nums[i]]=1


