"""
2357. Make Array Zero by Subtracting Equal Amounts
https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/description/

You are given a non-negative integer array nums. In one operation, you must:
Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
Subtract x from every positive element in nums.
Return the minimum number of operations to make every element in nums equal to 0.

Example 1:
Input: nums = [1,5,0,3,5]
Output: 3
Explanation:
In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].

Example 2:
Input: nums = [0]
Output: 0
Explanation: Each element in nums is already 0 so no operations are needed.
"""

import numpy as np
def minimumOperations2(nums:list):
    """
    :type nums: List[int]
    :rtype: int
    """
    n=0
    nums1=np.array(nums)
    if (nums1==0).all(): return n
    while not (nums1==0).all():
        nums1=np.sort(nums1)
        # stackoverflow.com/questions/47269390/how-to-find-first-non-zero-value-in-every-column-of-a-numpy-array
        subb=nums1[(nums1!=0).argmax()]
        nums1[nums1>0]=nums1[nums1>0]-subb
        n=n+1
        # print('n=',n,nums1); input()
    return n


print(minimumOperations2([1,5,0,3,5]))
# a=np.array([0,0,1,5,0,3,5])
# b = (a!=0).argmax()
# print(b)