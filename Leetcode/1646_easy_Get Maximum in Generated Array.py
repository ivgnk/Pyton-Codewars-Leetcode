'''
1646. Get Maximum in Generated Array
https://leetcode.com/problems/get-maximum-in-generated-array/description/

You are given an integer n.
A 0-indexed integer array nums of length n + 1 is generated in the following way:
nums[0] = 0
nums[1] = 1
nums[2 * i] = nums[i] when 2 <= 2 * i <= n
nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
Return the maximum integer in the array nums
'''

# Runtime 10 ms Beats 86.05% of users with Python
# Memory 11.85 MB Beats 41.86% of users with Python

def getMaximumGenerated(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0: return 0
    if n == 1: return 1
    nums = [0] * (n + 1)
    nums[1] = 1
    for i in range(1, n + 1):
        k = 2 * i
        if k <= n: nums[k] = nums[i]
        if k + 1 <= n:  nums[k + 1] = nums[i] + nums[i + 1]
    return max(nums)

print(getMaximumGenerated(4))