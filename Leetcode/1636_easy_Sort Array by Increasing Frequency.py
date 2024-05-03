"""
Done 03.05.2024
1636. Sort Array by Increasing Frequency
https://leetcode.com/problems/sort-array-by-increasing-frequency/description/

Given an array of integers nums, sort the array in increasing order based on the frequency of the values.
If multiple values have the same frequency, sort them in decreasing order.
Return the sorted array.

Example 1:
Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

Example 2:
Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.

Example 3:
Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]
"""

from collections import Counter
from functools import cmp_to_key

# Runtime 34 ms Beats 36.96% of users with Python
# Memory 11.92 MB Beats 7.97% of users with Python

def msrtr(a, b):
    if a[0] > b[0]:
        return 1
    elif a[0] < b[0]:
        return -1
    elif a[1] > b[1]:
        return -1
    elif a[1] < b[1]:
        return 1
    else: return 0
def frequencySort(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    dd = dict(Counter(nums))
    srt_ = sorted([[v, k] for k, v in dd.items()], key = cmp_to_key(msrtr))
    return [dat[1] for dat in srt_ for i in range(dat[0])]

# print(frequencySort([1,1,2,2,2,3]))
# print(frequencySort([2,3,1,3,2]))
print(frequencySort([-1,1,-6,4,5,-6,1,4,1]))   # [5,-1,4,4,-6,-6,1,1,1]
