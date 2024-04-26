"""
905. Sort Array By Parity
https://leetcode.com/problems/sort-array-by-parity/description/

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
Return any array that satisfies this condition.

Example 1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:
Input: nums = [0]
Output: [0]
"""

# Runtime 50 ms Beats 64.47% of users with Python
# Memory 12.35 MB Beats 94.72% of users with Python
# Runtime 45 ms Beats 87.85% of users with Python
# Memory 12.43 MB Beats 74.37% of users with Python

def sortArrayByParity(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if len(nums)==1: return nums
    l1 = [i for i in nums if i%2==0]
    l2 = [i for i in nums if i%2!=0]
    return l1+l2
