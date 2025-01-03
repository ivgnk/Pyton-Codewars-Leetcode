"""
03.01.2025. Topics: Prefix Sum
2270. Number of Ways to Split Array
https://leetcode.com/problems/number-of-ways-to-split-array/description/

You are given a 0-indexed integer array nums of length n.
nums contains a valid split at index i if the following are true:
The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
There is at least one element to the right of i. That is, 0 <= i < n - 1.
Return the number of valid splits in nums.

Example 1:

Input: nums = [10,4,-8,7]
Output: 2
Explanation:
There are three ways of splitting nums into two non-empty parts:
- Split nums at index 0. Then, the first part is [10], and its sum is 10.
The second part is [4,-8,7], and its sum is 3. Since 10 >= 3, i = 0 is a valid split.
- Split nums at index 1. Then, the first part is [10,4], and its sum is 14.
The second part is [-8,7], and its sum is -1. Since 14 >= -1, i = 1 is a valid split.
- Split nums at index 2. Then, the first part is [10,4,-8], and its sum is 6.
The second part is [7], and its sum is 7. Since 6 < 7, i = 2 is not a valid split.
Thus, the number of valid splits in nums is 2.
Example 2:

Input: nums = [2,3,1,0]
Output: 2
Explanation:
There are two valid splits in nums:
- Split nums at index 1. Then, the first part is [2,3], and its sum is 5.
The second part is [1,0], and its sum is 1. Since 5 >= 1, i = 1 is a valid split.
- Split nums at index 2. Then, the first part is [2,3,1], and its sum is 6.
The second part is [0], and its sum is 0. Since 6 >= 0, i = 2 is a valid split.

Constraints:
2 <= nums.length <= 105
-105 <= nums[i] <= 105

Hint 1
For any index i, how can we find the sum of the first (i+1) elements from the sum of the first i elements?
Hint 2
If the total sum of the array is known, how can we check
if the sum of the first (i+1) elements greater than or equal to the remaining elements?
"""
from typing import List
# https://leetcode.com/problems/number-of-ways-to-split-array/editorial
# Runtime 91 ms Beats 21.38%
# Memory 33.26 MB Beats 16.48%
# Time Complexity O(N)
# Space Complexity O(N)

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        # Prefix sum array to store cumulative sums
        pref_sum = [0] * n
        pref_sum[0] = nums[0]

        # Build prefix sum array
        for i in range(1, n):
            pref_sum[i] = pref_sum[i - 1] + nums[i]

        # Check each possible split position
        count = sum(
            1 for i in range(n - 1) if pref_sum[i] >= pref_sum[-1] - pref_sum[i]
        )
        return count


