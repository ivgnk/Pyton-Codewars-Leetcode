"""
23.07.2024. Topics: Array, Greedy
334. Increasing Triplet Subsequence
https://leetcode.com/problems/increasing-triplet-subsequence/

Given an integer array nums, return true if there exists a triple of indices (i, j, k)
such that i < j < k and nums[i] < nums[j] < nums[k].
If no such indices exists, return false.

Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.


Constraints:
1 <= nums.length <= 5 * 10**5
-231 <= nums[i] <= 2**31 - 1

# https://leetcode.com/problems/increasing-triplet-subsequence/solutions/5287156/beats-99-simple-solution-explained-line-by-line-c-java-python/

Approach
1) Initialize two variables (first and second) to the largest possible integer values.
These will store the smallest and second smallest values encountered so far.
2) Traverse the array:
- Update first if the current element is smaller than or equal to first.
- Update second if the current element is smaller than or equal to second but larger than first.
- If an element larger than both first and second is found, return true.

Complexity
Time complexity:O(n), where n is the number of elements in the array. We traverse the array once.
Space complexity:O(1), since we are using a fixed amount of extra space.
"""

def increasingTriplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    first = second = 10000000
    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    return False