"""
Done 29.09.2024. Topics: String
3300. Minimum Element After Replacement With Digit Sum
https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/description/

You are given an integer array nums.
You replace each element in nums with the sum of its digits.
Return the minimum element in nums after all replacements.

Example 1:
Input: nums = [10,12,13,14]
Output: 1
Explanation:
nums becomes [1, 3, 4, 5] after all replacements, with minimum element 1.

Example 2:
Input: nums = [1,2,3,4]
Output: 1
Explanation:
nums becomes [1, 2, 3, 4] after all replacements, with minimum element 1.

Example 3:
Input: nums = [999,19,199]
Output: 10
Explanation:
nums becomes [27, 10, 19] after all replacements, with minimum element 10.

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 104

Hint 1
Convert to string and calculate the sum for each element.
"""

# Runtime 43 ms Beats 100.00%
# Memory 11.52 MB Beats 100.00%
def minElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n=[sum(map(int,list(str(i)))) for i in nums]
    return min(n)

print(minElement([10,12,13,14]))
