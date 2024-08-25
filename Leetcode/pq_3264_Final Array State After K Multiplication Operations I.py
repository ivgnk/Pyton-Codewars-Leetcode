"""
25.08.2024
3264. Final Array State After K Multiplication Operations I
https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/description/

You are given an integer array nums, an integer k, and an integer multiplier.

You need to perform k operations on nums. In each operation:

Find the minimum value x in nums.
If there are multiple occurrences of the minimum value, select the one that appears first.
Replace the selected minimum value x with x * multiplier.
Return an integer array denoting the final state of nums after performing all k operations.

Example 1:
Input: nums = [2,1,3,5,6], k = 5, multiplier = 2
Output: [8,4,6,5,6]
Explanation:
Operation	Result
After operation 1	[2, 2, 3, 5, 6]
After operation 2	[4, 2, 3, 5, 6]
After operation 3	[4, 4, 3, 5, 6]
After operation 4	[4, 4, 6, 5, 6]
After operation 5	[8, 4, 6, 5, 6]

Example 2:
Input: nums = [1,2], k = 3, multiplier = 4
Output: [16,8]
Explanation:
Operation	Result
After operation 1	[4, 2]
After operation 2	[4, 8]
After operation 3	[16, 8]

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100
1 <= k <= 10
1 <= multiplier <= 5

Hint 1
Maintain sorted pairs (nums[index], index) in a priority queue.
Hint 2
Simulate the operation k times.
"""

from icecream import ic
import heapq
# https://docs-python.ru/standart-library/modul-heapq-python/


# Runtime 47 ms Beats 100.00%
# Memory 11.65 MB Beats 100.00%
def getFinalState2(nums, k, multiplier):
    """
    :type nums: List[int]
    :type k: int
    :type multiplier: int
    :rtype: List[int]
    """
    heap = list(zip(nums, range(len(nums))))
    heapq.heapify(heap)

    while k:
        num, idx = heapq.heappop(heap)
        heapq.heappush(heap, (num * multiplier, idx))
        k -= 1

    heap.sort(key=lambda x: x[1])
    ic(heap)
    ic(list(zip(*heap)))
    return list(zip(*heap))[0]

# Runtime 46 ms Beats 100.00%
# Memory 11.60 MB Beats 100.00%
def getFinalState(nums, k, multiplier):
    for i in range(k):
        s=min(nums)
        y=nums.index(s)
        nums[y]*=multiplier
    return nums

ic(getFinalState2( nums = [2,1,3,5,6], k = 5, multiplier = 2))


