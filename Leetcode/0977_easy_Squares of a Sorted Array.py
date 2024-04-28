"""
Done 28.04.2024
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""

# Runtime 134 ms Beats 97.66% of users with Python
# Memory 13.93 MB Beats 7.81% of users with Python

def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    return sorted([x * x for x in nums])
