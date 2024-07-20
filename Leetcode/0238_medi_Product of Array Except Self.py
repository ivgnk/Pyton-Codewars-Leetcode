"""
Done 20.07.2024. Topics: Array, Prefix Sum
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/description/

Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity analysis.)

Hint 1
Think how you can efficiently utilize prefix and suffix products to calculate the product of all elements except self for each index. Can you pre-compute the prefix and suffix products in linear time to avoid redundant calculations?
Hint 2
Can you minimize additional space usage by reusing memory or modifying the input array to store intermediate results?
"""

# Runtime 267 ms Beats 65.10%
# Memory 25.68 MB Beats 73.68%
# Runtime 259 ms Beats 86.80%
# Memory 25.70 MB Beats 73.68%

import math
def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if 0 in nums:
        cnt = nums.count(0)
        r = [n for n in nums if n != 0]
        if r == [] or cnt > 1: # (len(r) == 1 and len(nums) > 2 and cnt > 1):
            pr = 0
            print('inn')
        else:
            pr = math.prod(r)
        return [pr if n == 0 else 0 for n in nums]
    else:
        pr = math.prod(nums)
        return [pr // n for n in nums]


# print(productExceptSelf([1,2,3,4]))
# print(productExceptSelf([-1,1,0,-3,3]))
print(productExceptSelf([2,3,0,0]))
