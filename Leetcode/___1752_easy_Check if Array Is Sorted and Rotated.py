"""
10.05.2025. Topics: Array
1752. Check if Array Is Sorted and Rotated
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/

Given an array nums, return true if the array was originally sorted in non-decreasing order,
then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.
Note: An array A rotated by x positions results in an array
B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

Example 1:
Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].

Example 2:
Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.

Example 3:
Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
"""

# Runtime 58 ms Beats 5.24% of users with Python
# Memory 22.80 MB Beats 12.30% of users with Python

import numpy as np
def check(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    a = np.array(nums)
    ns=np.sort(a)
    if np.array_equal(a, ns):return True
    for i in range(len(nums)):
        if np.array_equal(np.roll(a,i),ns): return True
    else: return False

print(check([3,4,5,1,2]))
print(check([2,1,3,4]))
print(check([1,2,4]))

