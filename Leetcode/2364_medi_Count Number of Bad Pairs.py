"""
Done 04.05.2024
2364. Count Number of Bad Pairs
You are given a 0-indexed integer array nums.
A pair of indices (i, j) is a bad pair
if i < j and j - i != nums[j] - nums[i].
Return the total number of bad pairs in nums.

Example 1:
Input: nums = [4,1,3,3]
Output: 5
Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
There are a total of 5 bad pairs, so we return 5.

Example 2:
Input: nums = [1,2,3,4,5]
Output: 0
Explanation: There are no bad pairs.
"""

from collections import Counter
from icecream import ic

# Time Limit Exceeded -- 48 / 65 testcases passed
def countBadPairs2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll=len(nums); n=0
    for i in range(ll):
        for j in range(i+1,ll):
            if j-i != nums[j]-nums[i]:
                 n=n+1
    return n

# Time Limit Exceeded -- 52 / 65 testcases passed
def countBadPairs3(nums):
    ll=len(nums); n=0
    for i in range(ll):
        nn = nums[i]-i
        for j in range(i+1,ll):
            if nn != nums[j]-j:
                 n=n+1
    return n

# Time Limit Exceeded -- # 53 / 65 testcases passed
# len(nums) = 8252
def countBadPairs4(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll = len(nums);  n = 0
    n2 = [nums[i] - i for i in range(ll)]
    for i in range(ll):
        nn = n2[i]
        for j in range(i + 1, ll):
            if nn != n2[j]:
                n = n + 1
    return n


# Time Limit Exceeded -- 55 / 65 testcases passed
# len(nums) = 31179
def countBadPairs5(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll = len(nums);  n = 0
    n2 = [nums[i] - i for i in range(ll)]
    total_number_of_pairs = ll * ( ll - 1 ) // 2
    for i in range(ll):
        nn = n2[i]
        for j in range(i + 1, ll):
            if nn == n2[j]:
                n = n + 1
    return total_number_of_pairs-n


# Runtime 625 ms Beats 7.69% of users with Python
# Memory 36.42 MB Beats 7.69%# of users with Python
def countBadPairs(nums):
    ll = len(nums)
    n2 = [nums[i] - i for i in range(ll)]
    total_number_of_pairs = ll * (ll - 1) // 2
    dd = dict(Counter(n2))
    # if len(dd) == 1: return 0
    ngood = sum([v * (v - 1) // 2 for k, v in dd.items()])
    return total_number_of_pairs - ngood

ic(countBadPairs(nums = [1,2,3,4,5]))
