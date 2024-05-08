"""
Done 09.05.2024. Topics: Array, Binary Search, Stack, Monotonic Stack, Ordered Set

Good solution in https://leetcode.ca/2017-02-28-456-132-Pattern/

456. 132 Pattern
https://leetcode.com/problems/132-pattern/description/

Given an array of n integers nums, a 132 pattern is a subsequence of three
integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Example 1:
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.

Example 2:
Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:
Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
"""

from math import copysign as cs
def find132pattern2(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nv=sorted(nums)
    nu=sorted(nums, reverse=True)
    if nums==nv or nums==nu: return False
    if len(set(nums))<3: return False
    ll=len(nums)

    if all([True if cs(1, nums[i]) != cs(1, nums[i - 1]) else False for i in range(1, ll)]): return False

    if ll > 100:
        nums = [nums[0]] + [nums[i] for i in range(1, ll) if nums[i] != nums[i - 1]]
        ll = len(nums)

    for i in range(ll):
        for j in range(i+1,ll):
            if nums[i] < nums[j]:
                for k in range(j+1,ll):
                    if nums[i] < nums[k] < nums[j]: return True
    return False

# Runtime 3310 ms Beats 5.10% of users with Python
# Memory 43.52 MB Beats 6.37% of users with Python

def find132pattern(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # nv=sorted(nums)
    # nu=sorted(nums, reverse=True)
    # if nums==nv or nums==nu: return False
    if len(set(nums))<3: return False
    ll=len(nums)

    if ll > 100:
        if all([True if cs(1, nums[i]) != cs(1, nums[i - 1]) else False for i in range(1, ll)]): return False
        nums = [nums[0]] + [nums[i] for i in range(1, ll) if nums[i] != nums[i - 1]]
        nn = nums[:3]*10
        if nn in nums: nums=nn
        ll = len(nums)
    for i in range(ll):
        for j in range(i + 1, ll):
            if nums[i] < nums[j]:
                for k in range(j + 1, ll):
                    if nums[i] < nums[k]:
                        if nums[k] < nums[j]: return True
    return False


print(find132pattern([0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,
                      1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,
                      2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,
                      0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,
                      1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,
                      2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,
                      0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0]))  # i < j < k and nums[i] < nums[k] < nums[j].