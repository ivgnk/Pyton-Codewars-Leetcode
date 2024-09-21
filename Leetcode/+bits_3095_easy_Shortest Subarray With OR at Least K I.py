"""
21.09.2024. Topics: Array, Bit Manipulation, Sliding Window
3095. Shortest Subarray With OR at Least K I
https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/description/

You are given an array nums of non-negative integers and an integer k.
An array is called special if the bitwise OR of all of its elements is at least k.
Return the length of the shortest special non-empty
subarray of nums, or return -1 if no special subarray exists.

Example 1:
Input: nums = [1,2,3], k = 2
Output: 1
Explanation:
The subarray [3] has OR value of 3. Hence, we return 1.

Example 2:
Input: nums = [2,1,8], k = 10
Output: 3
Explanation:
The subarray [2,1,8] has OR value of 11. Hence, we return 3.

Example 3:
Input: nums = [1,2], k = 0
Output: 1
Explanation:
The subarray [1] has OR value of 1. Hence, we return 1.

Constraints:
1 <= nums.length <= 50
0 <= nums[i] <= 50
0 <= k < 64

Hint 1
The constraints are small. Brute force checking all the subarrays.

Solution
https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/solutions/5212705/brute-force-and-optimized-solutions-with-full-explanations/

Intuition
To find the minimum length of a subarray whose bitwise OR is at least k,
we need to evaluate subarrays dynamically as we iterate through the list.
A sliding window approach is suitable for this problem,
where we expand and contract the window to find the smallest subarray that meets the condition.

Brute Force Approach:
Iterate over all possible subarrays.
For each subarray, calculate the bitwise OR and check if it meets the condition.
Track the minimum length of valid subarrays.
This approach is straightforward but inefficient for large inputs.
"""


# O(n^2) time.
# O(1) space
# Runtime 46 ms Beats 17.95%
# Memory 11.82 MB Beats 5.13%
# Runtime 34 ms Beats 48.72%
# Memory 11.44 MB Beats 92.31%
def minimumSubarrayLength(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # Brute Force
    min_length = 10000
    for start in range(len(nums)):
        arr = 0
        for end in range(start, len(nums)):
            arr |= nums[end]
            if arr >= k:
                min_length = min(min_length, end - start + 1)
                # Break after finding the first valid subarray starting at 'start',
                # because extending this subarray further will only increase its length
                # and any subsequent subarrays starting from the same point cannot be shorter.
                break

    return min_length if min_length != 10000 else -1

