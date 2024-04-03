'''
349. Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/description/

Given two integer arrays nums1 and nums2, return an array of their intersection
Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
'''

# Runtime 19 ms Beats 95.48% of users with Python
# Memory 11.87 MB Beats 35.76% of users with Python

def intersection(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    return list(set(nums1) & set(nums2))
