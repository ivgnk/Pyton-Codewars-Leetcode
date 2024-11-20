"""
Done 20.11.2024. Topics: Sliding Window
413. Arithmetic Slices
https://leetcode.com/problems/arithmetic-slices/description

An integer array is called arithmetic if it consists of at least three elements and
if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.
Example 1:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.

Example 2:
Input: nums = [1]
Output: 0

Constraints:
1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000
"""
# Time Limit Exceeded - 12 / 15 testcases passed
def numberOfArithmeticSlices4(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll=len(nums); ll1=ll+1
    if ll<3: return 0
    n=0
    for i in range(ll-2):
        for j in range(i+3,ll1):
            s=nums[i:j]
            d=s[1]-s[0]
            if all((s[i]-s[i-1])==d for i in range(1,len(s))):
                n+=1
    return n

# Runtime 65 ms Beats 5.41%
# Memory 12.15 MB Beats 6.34%
def numberOfArithmeticSlices3(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll=len(nums); ll1=ll+1
    if ll<3: return 0
    n=0
    for i in range(ll-2):
        i3=i+3
        for j in range(i3,ll1):
            if j==i3:
                s=nums[i:j]
                d=s[1]-s[0]
            else: s=s+[nums[j-1]]
            if all((s[i]-s[i-1])==d for i in range(1,len(s))):
                n+=1
            else: break
    return n

# Runtime 0 ms Beats 100.00%
# Memory 11.92 MB Beats 23.94%
def numberOfArithmeticSlices(nums):
    if len(nums) < 3: return 0
    n = 0
    clen = 0
    for i in range(2, len(nums)):
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            clen += 1
            n += clen
        else:
            clen = 0
    return n

print(numberOfArithmeticSlices([1,2,3,4]))
print(numberOfArithmeticSlices([1]))


class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        if n < 3:
            return 0
        count = 0
        diff = nums[1] - nums[0]
        length = 2
        for i in range(2, n):
            if nums[i] - nums[i - 1] == diff:
                length += 1
            else:
                if length >= 3:
                    count += (length - 2) * (length - 1) // 2
                diff = nums[i] - nums[i - 1]
                length = 2
        if length >= 3:
            count += (length - 2) * (length - 1) // 2
        return count
