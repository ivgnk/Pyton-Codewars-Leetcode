"""
Done 25.06.2024. Topics: Array, Math
3190. Find Minimum Operations to Make All Elements Divisible by Three
https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description/

You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.
Return the minimum number of operations to make all elements of nums divisible by 3.

Example 1:
Input: nums = [1,2,3,4]
Output: 3
Explanation:
All array elements can be made divisible by 3 using 3 operations:
Subtract 1 from 1.
Add 1 to 2.
Subtract 1 from 4.

Example 2:
Input: nums = [3,6,9]
Output: 0

Hint 1
If x % 3 != 0 we can always increment or decrement x such that we only need 1 operation.
Hint 2
Add min(nums[i] % 3, 3 - (num[i] % 3)) to the count of operations.
"""

# Runtime 21 ms Beats 44.83%
# Memory 11.48 MB Beats 87.13%
# Runtime 14 ms Beats 91.42%
# Memory 11.68 MB Beats 19.30%

def minimumOperations(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return sum([min(nums[i] % 3, 3 - (nums[i] % 3)) for i in range(len(nums))])