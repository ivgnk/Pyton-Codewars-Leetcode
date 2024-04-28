"""
Done 29.04.2024
215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/1244467310/
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""

# Runtime 447 ms Beats 92.79% of users with Python
# Memory 22.16 MB Beats 24.30% of users with Python

def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    return sorted(nums)[-k]