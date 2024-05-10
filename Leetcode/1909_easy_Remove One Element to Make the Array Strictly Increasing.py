"""
Done 10.05.2024. Topics: Array
1909. Remove One Element to Make the Array Strictly Increasing
https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/description/

Given a 0-indexed integer array nums, return true
if it can be made strictly increasing after removing exactly one element, or false otherwise.
If the array is already strictly increasing, return true.

The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).

Example 1:
Input: nums = [1,2,10,5,7]
Output: true
Explanation: By removing 10 at index 2 from nums, it becomes [1,2,5,7].
[1,2,5,7] is strictly increasing, so return true.

Example 2:
Input: nums = [2,3,1,2]
Output: false
Explanation:
[3,1,2] is the result of removing the element at index 0.
[2,1,2] is the result of removing the element at index 1.
[2,3,2] is the result of removing the element at index 2.
[2,3,1] is the result of removing the element at index 3.
No resulting array is strictly increasing, so return false.

Example 3:
Input: nums = [1,1,1]
Output: false
Explanation: The result of removing any element is [1,1].
[1,1] is not strictly increasing, so return false.
"""

# Runtime 31 ms Beats 76.52% of users with Python
# Memory 11.88 MB Beats 25.22% of users with Python
# Runtime 30 ms Beats 79.13% of users with Python
# Memory 11.89 MB Beats 25.22% of users with Python

from icecream import ic
from collections import Counter
def canBeIncreasing(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    ll = len(nums)
    dd = dict(Counter(nums))
    if len(dd) == 1 and ll > 2: return False
    nu = [[k, v] for k, v in dd.items() if v > 1]
    if len(nu) > 1: return False

    if nums == sorted(nums): return True
    if ll == 2: return True

    if len(nu) != 0:
        bad = nu[0][0]
        indices = [i for i, x in enumerate(nums) if x == bad]
        for i in indices:
            s = nums[:i] + nums[i + 1:]
            if s == sorted(s): return True
        else: return False
    else:
        for i in range(ll):
            s = nums[:i] + nums[i + 1:]
            if s == sorted(s): return True
        else:
            return False


# Runtime 953 ms Beats 5.22% of users with Python
# Memory 12.10 MB Beats 6.09% of users with Python

def canBeIncreasing2(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    ll = len(nums)
    dd = dict(Counter(nums))
    if len(dd) == 1 and ll > 2: return False
    nu = [[k, v] for k, v in dd.items() if v > 1]
    if len(nu) > 1: return False

    if nums == sorted(nums): return True
    if ll == 2: return True

    for i in range(ll):
        s = nums[:i] + nums[i + 1:]
        # print(i,s)
        dd = dict(Counter(s))
        if all([True if v == 1 else False for k, v in dd.items()]):
            if s == sorted(s): return True
    else:
        return False

ic(canBeIncreasing([2,3,4,5,1,5]))

