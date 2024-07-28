"""
Done 28.07.2024. Topics: Array, Two Pointers
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/description/

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 10**4
-231 <= nums[i] <= 2**31 - 1

Hint 1
In-place means we should not be allocating any space for extra array. But we are allowed to modify the existing array.
However, as a first step, try coming up with a solution that makes use of additional space.
For this problem as well, first apply the idea discussed using an additional array and
the in-place solution will pop up eventually.
Hint 2
A two-pointer approach could be helpful here.
The idea would be to have one pointer for iterating the array and another pointer
that just works on the non-zero elements of the array.
"""

from icecream import ic
# Wrong Answer
def moveZeroes2(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    n0 = nums.count(0)
    nums = [x for x in nums if x != 0] + [0] * n0
    return nums


# Runtime 114 ms Beats 69.20%
# Memory 12.95 MB Beats 24.11%
def moveZeroes3(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    res1 = [x for x in nums if x != 0];    ll1 = len(res1)
    res2 = [x for x in nums if x == 0];    ll2 = len(res2)
    for i in range(ll1): nums[i] = res1[i]
    for i in range(ll1, ll1 + ll2): nums[i] = res2[i - ll1]


def moveZeroes4(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    zeroes = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zeroes += 1
        else:
            nums[i], nums[i - zeroes] = nums[i - zeroes], nums[i]
    return nums

def moveZeroes(nums):
    count = nums.count(0)
    for i in range(count):
        nums.remove(0)
        nums.append(0)
    return nums

ic(moveZeroes2([0,1,0,3,12]))
ic(moveZeroes([0,1,0,3,12]))
