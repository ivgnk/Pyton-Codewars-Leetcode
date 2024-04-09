"""
1800. Maximum Ascending Subarray Sum
https://leetcode.com/problems/maximum-ascending-subarray-sum/description/

Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.
A subarray is defined as a contiguous sequence of numbers in an array.
A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending
if for all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending.


Example 1:
Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.

Example 2:
Input: nums = [10,20,30,40,50]
Output: 150
Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.

Example 3:
Input: nums = [12,17,15,13,10,11,12]
Output: 33
Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.
"""
# Runtime 15 ms Beats 76.64% of users with Python
# Memory 11.45 MB Beats 94.39% of users with Python

def maxAscendingSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll=len(nums); mmax = nums[0]
    for i in range(ll):
        res=[nums[i]]
        calc=True
        for j in range(i+1,ll):
            if calc:
                if res[-1]<nums[j]:
                    res.append(nums[j])
                else: calc=False
        ssum=sum(res)
        if ssum>mmax: mmax=ssum
    return mmax


# print(f'{maxAscendingSum([10,20,30,5,10,50])=}')
print(f'{maxAscendingSum([10,20,30,40,50])=}')
# print(f'{maxAscendingSum([12,17,15,13,10,11,12])=}')