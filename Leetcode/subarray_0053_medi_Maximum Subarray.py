"""
Done 24.05.2025. Topics: Array, Divide and Conquer, Dynamic Programming
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/description/

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""

# https://en.wikipedia.org/wiki/Maximum_subarray_problem

# Runtime 538 ms Beats 51.80% of users with Python
# Memory 24.82 MB Beats 7.83% of users with Python
def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    best_sum = - 2**39
    current_sum = 0
    for x in nums:
        current_sum = max(x, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([1]))
print(maxSubArray([5,4,-1,7,8]))

