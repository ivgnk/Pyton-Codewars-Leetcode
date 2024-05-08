"""
Done 08.05.2024. Topics: Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect

347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

# Runtime 85 ms Beats 77.61% of users with Python3
# Memory 21.16 MB Beats 56.48% of users with Python3

from collections import Counter
def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    ll = len(nums)
    if ll == 1: return nums
    elif ll == 2:
        if nums[0] == nums[1]: return [nums[0]]
        else: return nums

    dd=dict(Counter(nums))
    lst=sorted([[v,k] for k,v in dd.items()], reverse=True)
    if k == 1: return [lst[0][1]]

    return [lst[i][1] for i in range(k)]

print(topKFrequent(nums = [1,1,1,2,2,3], k = 2))