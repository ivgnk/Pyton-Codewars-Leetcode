"""
Done 04.05.2024
2176. Count Equal and Divisible Pairs in an Array
https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/description/

Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j)
where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.

Example 1:
Input: nums = [3,1,2,2,2,1,3], k = 2
Output: 4
Explanation:
There are 4 pairs that meet all the requirements:
- nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2.
- nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2.
- nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2.
- nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.

Example 2:
Input: nums = [1,2,3,4], k = 1
Output: 0
Explanation: Since no value in nums is repeated, there are no pairs (i,j) that meet all the requirements.
"""

# Runtime 65 ms Beats 57.86% of users with Python
# Memory 11.54 MB Beats 80.50% of users with Python
# Runtime 59 ms Beats 81.76% of users with Python
# Memory 11.87 MB Beats 5.03% of users with Python

def countPairs(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    ll=len(nums); n=0
    for i in range(ll):
        for j in range(i+1,ll):
            if nums[i]==nums[j]:
                if i*j%k==0:
                    n=n+1
    return n

print(countPairs(nums = [3,1,2,2,2,1,3], k = 2))


