"""
Done 25.05.2024. Topics: Array, Dynamic Programming
1749. Maximum Absolute Sum of Any Subarray
https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description/

You are given an integer array nums.
The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is
abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.
Note that abs(x) is defined as follows:
If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.

Example 1:
Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.

Example 2:
Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.

Hint 1
What if we asked for maximum sum, not absolute sum?
Hint 2
It's a standard problem that can be solved by Kadane's algorithm.
Hint 3
The key idea is the max absolute sum will be either the max sum or the min sum.
Hint 4
So just run kadane twice, once calculating the max sum and once calculating the min sum.
"""

# https://en.wikipedia.org/wiki/Maximum_subarray_problem

# Runtime 344 ms Beats 56.00% of users with Python
# Memory 22.67 MB Beats 96.00% of users with Python

def maxAbsoluteSum2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #-(1)---- Kadane +1
    best_sum_p = - 2 ** 39
    current_sum = 0
    for x in nums:
        current_sum = max(x, current_sum + x)
        best_sum_p = max(best_sum_p, current_sum)

    #-(2)---- Kadane -1
    best_sum_m =  2 ** 39
    current_sum = 0
    for x in nums:
        current_sum = min(x, current_sum + x)
        best_sum_m = min(best_sum_m, current_sum)
    return max(abs(best_sum_p), abs(best_sum_m))

# Runtime 349 ms Beats 40.00% of users with Python
# Memory 22.73 MB Beats 68.00% of users with Python

def maxAbsoluteSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #-(1)---- Kadane +1
    best_sum_p = - 2 ** 39
    best_sum_m =  2 ** 39
    current_sum_p = 0
    current_sum_m = 0
    for x in nums:
        current_sum_p = max(x, current_sum_p + x)
        current_sum_m = min(x, current_sum_m + x)
        best_sum_p = max(best_sum_p, current_sum_p)
        best_sum_m = min(best_sum_m, current_sum_m)

    return max(abs(best_sum_p), abs(best_sum_m))
