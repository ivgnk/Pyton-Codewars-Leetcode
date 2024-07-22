"""
Done 22.07.2024. Topics: Array, Hash Table, Two Pointers, Sorting
1679 Max Number of K-Sum Pairs
https://leetcode.com/problems/max-number-of-k-sum-pairs/

You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.

Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.

Constraints:
1 <= nums.length <= 10**5
1 <= nums[i] <= 10**9
1 <= k <= 10**9

Hint 1
The abstract problem asks to count the number of disjoint pairs with a given sum k.
Hint 2
For each possible value x, it can be paired up with k - x.
Hint 3
The number of such pairs equals to min(count(x), count(k-x)), unless that x = k / 2, where the number of such pairs will be floor(count(x) / 2).
"""

# Runtime 486 ms Beats 75.93%
# Memory 29.86 MB Beats 9.60%
# Runtime 473 ms Beats 93.81%
# Memory 29.91 MB Beats 9.60%

from icecream import ic
from math import floor
def maxOperations(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    dd=dict(); dd2=dict()
    for i in nums:
        if i in dd:
            dd[i] = dd[i]+1
        else:
            dd[i] = 1
            dd2[i] = True
    ssum=0
    b = k%2==0
    for ke, va in dd.items():
        dd2[ke]=False
        if b and ke== k//2:
            ssum = ssum + floor(dd[ke]/2)
        else:
            if k-ke in dd and dd2[k-ke]:
                ssum = ssum + min(dd[ke], dd[k-ke])
                dd2[k-ke]=False
    return ssum

ic(maxOperations(nums = [1,2,3,4], k = 5))
# print(maxOperations(nums = [3,1,3,4,3], k = 6))




