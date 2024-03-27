'''
643. Maximum Average Subarray I
https://leetcode.com/problems/maximum-average-subarray-i/description/

You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted.


Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000
'''


import numpy as np
def findMaxAverage2(nums, k):
    # Time Limit Exceeded # 124 / 127 testcases passed
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    llen=len(nums)
    if llen==1 and k==1: return nums[0]
    i=0; aver=-1e38
    kfloat=float(k)
    while i+k<=llen:
        arr=nums[i:i+k]
        caver=sum(arr)/kfloat
        if caver>aver: aver=caver
        i=i+1
    return aver

def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    # Runtime 4238 ms Beats 5.00% of users with Python
    # Memory 32.55 MB Beats 6.01% of users with Python
    llen=len(nums)
    if llen==1 and k==1: return nums[0]
    i=0; aver=-1e38
    kfloat=float(k)
    nums1=np.array(nums)
    while i+k<=llen:
        caver=np.average(nums1[i:i+k])
        if caver>aver: aver=caver
        i=i+1
    return aver


print(findMaxAverage([1,12,-5,-6,50,3],4))

