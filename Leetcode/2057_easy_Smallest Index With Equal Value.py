"""
Done 09.05.2024. Topics: Array
2057. Smallest Index With Equal Value
Given a 0-indexed integer array nums, return the smallest index i of nums such that i mod 10 == nums[i],
or -1 if such index does not exist.
x mod y denotes the remainder when x is divided by y.

Example 1:
Input: nums = [0,1,2]
Output: 0
Explanation:
i=0: 0 mod 10 = 0 == nums[0].
i=1: 1 mod 10 = 1 == nums[1].
i=2: 2 mod 10 = 2 == nums[2].
All indices have i mod 10 == nums[i], so we return the smallest index 0.

Example 2:
Input: nums = [4,3,2,1]
Output: 2
Explanation:
i=0: 0 mod 10 = 0 != nums[0].
i=1: 1 mod 10 = 1 != nums[1].
i=2: 2 mod 10 = 2 == nums[2].
i=3: 3 mod 10 = 3 != nums[3].
2 is the only index which has i mod 10 == nums[i].

Example 3:
Input: nums = [1,2,3,4,5,6,7,8,9,0]
Output: -1
Explanation: No index satisfies i mod 10 == nums[i].
"""

# Runtime 55 ms Beats 70.68% of users with Python
# Memory 11.73 MB Beats 9.77% of users with Python
def smallestEqual2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(len(nums)):
        if (i % 10) == nums[i]: return i
    return -1

# Runtime 49 ms Beats 91.73% of users with Python
# Memory 11.49 MB Beats 93.98% of users with Python
def smallestEqual(nums):
    for i in range(len(nums)):
        if (i % 10) == nums[i]: return i
    else: return -1