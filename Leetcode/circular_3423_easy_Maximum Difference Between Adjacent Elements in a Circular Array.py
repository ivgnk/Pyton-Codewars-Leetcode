"""
Done 23.01.2025. Topics: Array
3423. Maximum Difference Between Adjacent Elements in a Circular Array
https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array

Given a circular array nums, find the maximum absolute difference between adjacent elements.
Note: In a circular array, the first and last elements are adjacent.

Example 1:
Input: nums = [1,2,4]
Output: 3
Explanation:
Because nums is circular, nums[0] and nums[2] are adjacent.
They have the maximum absolute difference of |4 - 1| = 3.

Example 2:
Input: nums = [-5,-10,-5]
Output: 5
Explanation:
The adjacent elements nums[0] and nums[1] have the maximum absolute difference of |-5 - (-10)| = 5.

Constraints:
2 <= nums.length <= 100
-100 <= nums[i] <= 100

Hint 1
Traverse from the second element to the last element and check the difference of every adjacent pair.
Hint 2
The edge case is to check the difference between the first and last elements.

My solution https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/solutions/6316790/fast-0-ms-and-easy-python-solution-for-p-njcp/
Fast (0 ms) and easy Python solution for Problem 3423
Intuition
Use List comprehension for speed
"""
# Runtime 2 ms Beats 62.74%
# Memory 17.64 MB Beats 90.95%
# Runtime 0 ms Beats 100.00%
# Memory 17.86 MB Beats 39.73%

# Time Complexity O(N)
# Space Complexity O(N)

def maxAdjacentDistance(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n1=nums+[nums[0]]; ll=len(n1)
    return max([abs(n1[i]-n1[i-1]) for i in range(1, ll)])