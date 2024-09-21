"""
Done 22.09.2024. Topics: Array, Math, Sorting
628. Maximum Product of Three Numbers
https://leetcode.com/problems/maximum-product-of-three-numbers/description/
Given an integer array nums,
find three numbers whose product is maximum and return the maximum product.

Example 1:
Input: nums = [1,2,3]
Output: 6

Example 2:
Input: nums = [1,2,3,4]
Output: 24

Example 3:
Input: nums = [-1,-2,-3]
Output: -6

Constraints:
3 <= nums.length <= 10**4
-1000 <= nums[i] <= 1000
"""

# Wrong Answer - 69 / 93 testcases passed
# Input
# nums = [-100,-98,-1,2,3,4]
# Output 24
# Expected 39200

# Runtime 392 ms Beats 9.45%
# Memory 12.97 MB Beats 8.43%
def maximumProduct2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 3: return nums[0] * nums[1] * nums[2]
    if all([i > 0 for i in nums]):
        nums = sorted(nums)
        return nums[-1] * nums[-2] * nums[-3]
    elif all([i < 0 for i in nums]):
        nums = sorted(nums)
        return nums[-1] * nums[-2] * nums[-3]
    else:
        nums = sorted(nums)
        # one negative element
        if nums[0] < 0 and nums[1] > 0:
            return nums[-1] * nums[-2] * nums[-3]
        # two or more negative elements
        else:
            lft = nums[0] * nums[1] * nums[-1]
            rgt = nums[-1] * nums[-2] * nums[-3]
            return max(lft, rgt)

# Runtime 390 ms Beats 10.76%
# Memory 12.78 MB Beats 72.97%
# Runtime 381 ms Beats 15.70%
# Memory 12.83 MB Beats 36.05%
def maximumProduct3(nums):
    nums = sorted(nums)
    return max(nums[0]*nums[1]*nums[-1],
               nums[-1] * nums[-2] * nums[-3])

# Runtime 393 ms Beats 8.87%
# Memory 12.99 MB Beats 8.43%
import heapq
def maximumProduct(nums):
    # heapq.heapify(nums)
    res3 = heapq.nlargest(3, nums) # [4, 3, 2] from more max
    res2 = heapq.nsmallest(2, nums) # [1, 2] from more min
    return max(res2[0]*res2[1]*res3[0],
               res3[0]*res3[1]*res3[2])

print(maximumProduct([1,2,3,4]))


def maximumProduct888(l):
    """
    :type nums: List[int]
    :rtype: int
    """
    m1 = max(l)
    l.remove(m1)
    m2 = max(l)
    l.remove(m2)
    m3 = max(l)
    l.remove(m3)
    if (len(l) >= 2):
        min1 = min(l)
        l.remove(min1)
        min2 = min(l)
        l.remove(min2)
        return max((m1 * m2 * m3), (min1 * min2 * m1))
    if (len(l) == 1):
        min1 = min(l)
        l.remove(min1)
        min2 = m3
        return max((m1 * m2 * m3), (min1 * min2 * m1))

    return m1 * m2 * m3
