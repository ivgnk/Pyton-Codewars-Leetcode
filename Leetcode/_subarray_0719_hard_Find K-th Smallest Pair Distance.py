"""
14.08.2024. Topics: Two Pointers, Binary Search, Sorting
719. Find K-th Smallest Pair Distance
https://leetcode.com/problems/find-k-th-smallest-pair-distance

The distance of a pair of integers a and b is defined as the absolute difference between a and b.
Given an integer array nums and an integer k, return the kth smallest distance
among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

Example 1:
Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.

Example 2:
Input: nums = [1,1,1], k = 2
Output: 0
Example 3:
Input: nums = [1,6,1], k = 3
Output: 5

Constraints:
n == nums.length
2 <= n <= 104
0 <= nums[i] <= 106
1 <= k <= n * (n - 1) / 2

Hint 1
Binary search for the answer. How can you check how many pairs have distance <= X?
"""

# Time Limit Exceeded - 13 / 19 testcases passed
# k = 62500
# nums= [2,2,0,1,0,1,2,0,2,1,1,1,1,0,1,2,1,1,1,2,1,2,1,0,1,0,1,1,0,2,1,0,0,2,2,1,1,1,2,2,1,0,0,0,2,0,0,0,0,0,1,0,1,2,2,2,2,2,2,1,1,0,1,0,1,1,1,1,2,1,1,2,2,2,0,1,2,2,2,0,0,2,0,1,2,2,1,2,0,2,1,0,0,2,1,1,0,1,0,1,0,0,0,1,1,2,0,0,1,2,2,2,2,2,2,0,2,1,1,1,1,1,2,0,2,2,2,0,2,0,1,0,1,2,1,0,1,2,1,2,1,2,0,2,0,1,0,1,2,2,1,2,2,1,0,0,1,2,1,1,0,0,2,1,0,2,1,2,0,0,1,0,2,0,1,2,2,2,1,2,0,2,2,2,2,2,0,0,0,1,0,2,0,0,1,1,0,0,2,2,1,0,0,0,2,0,1,1,1,2,1,1,2,1,1,0,1,0,1,1,1,2,0,0,2,2,2,1,1,1,2,2,2,0,1,0,0,0,0,1,0,2,2,0,2,2,1,1,1,2,1,1,1,0,2,0,2,1,1,2,2,1,1,2,0,0,2,1,2,0,1,1,1,2,2,0,1,2,2,2,1,1,0,1,0,0,1,2,1,1,0,1,0,2,2,2,0,1,1,0,1,0,1,2,2,2,1,1,0,1,0,0,2,1,1,1,0,0,0,0,2,2,2,0,1,0,2,0,0,0,0,0,0,2,0,1,0,0,0,1,1,2,2,1,2,2,0,2,1,0,2,1,2,0,1,2,1,2,2,2,2,2,0,0,1,0,0,2,2,0,1,0,0,0,2,1,0,1,2,1,1,0,0,1,1,0,0,2,2,2,1,0,0,0,0,0,0,1,0,1,2,0,1,1,2,1,0,0,0,2,2,1,2,2,0,0,1,0,1,0,0,1,2,0,0,0,1,1,0,0,1,0,0,0,0,0,2,0,2,0,0,0,0,0,1,2,1,1,1,2,2,0,2,1,0,2,1,0,2,1,1,0,2,0,2,1,0,0,0,1,1,0,1,0,2,2,2,1,2,0,1,2,0,0,0,2,2,2,1,1,1,2,2,2,2,0,1,0,0,1]
def smallestDistancePair3(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # if k>10:
    #     nums = sorted(set(nums))
    ll=len(nums)
    marr=[]; mmax = 1000000000; lmin=0
    for i in range(ll):
        for j in range(i+1,ll):
            z = abs(nums[i]-nums[j])
            if lmin==k:
                if z<mmax:
                    marr.pop()
                    marr.append(z)
                    marr.sort()
                    mmax = marr[-1]
            else:
                marr.append(z); marr.sort()
                mmax = marr[-1]
                lmin +=1
            # print(i,j,marr)
    return marr[-1]

# Memory Limit Exceeded - # 16 / 19 testcases passed
# k = 25 000 000
from heapq import *

def smallestDistancePair2(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    maxHeap = []
    heapify(maxHeap)

    for idx, val1 in enumerate(nums):
        for val2 in nums[idx + 1:]:
            pair = [val1, val2]
            heappush(maxHeap, [-1 * abs(pair[0] - pair[1]), pair])
            if len(maxHeap) > k:
                heappop(maxHeap)

    return -1 * maxHeap[0][0]


# Time Limit Exceeded - 18 / 19 testcases passed
# k =25 000 000
def smallestDistancePair4(nums, k):
    diffs = [0 for _ in range(1000000)]

    for i, num in enumerate(nums):
        for num2 in nums[i + 1:]:
            diffs[abs(num - num2)] += 1

    for i, diff in enumerate(diffs):
        k -= diff
        if k <= 0:
            return i

import math
import heapq
def smallestDistancePair(nums, k):
    n = len(nums)
    nums.sort()

    k = n * (n - 1) // 2 - k
    k += 1

    arr = [(nums[0] - nums[-1], 0, n - 1)]
    vis = set([(0, n - 1)])

    res = math.inf

    for _ in range(k):
        res, x, y = heapq.heappop(arr)

        if x + 1 < y and (x + 1, y) not in vis:
            vis.add((x + 1, y))
            heapq.heappush(arr, (nums[x + 1] - nums[y], x + 1, y))

        if y - 1 > x and (x, y - 1) not in vis:
            vis.add((x, y - 1))
            heapq.heappush(arr, (nums[x] - nums[y - 1], x, y - 1))

    return -res

print(smallestDistancePair(nums = [1,3,1], k = 1))
print(smallestDistancePair(nums = [1,1,1], k = 2))
print(smallestDistancePair(nums = [1,6,1], k = 3))
# print(smallestDistancePair(nums = [9,10,7,10,6,1,5,4,9,8], k = 18))
# print(len([2,2,0,1,0,1,2,0,2,1,1,1,1,0,1,2,1,1,1,2,1,2,1,0,1,0,1,1,0,2,1,0,0,2,2,1,1,1,2,2,1,0,0,0,2,0,0,0,0,0,1,0,1,2,2,2,2,2,2,1,1,0,1,0,1,1,1,1,2,1,1,2,2,2,0,1,2,2,2,0,0,2,0,1,2,2,1,2,0,2,1,0,0,2,1,1,0,1,0,1,0,0,0,1,1,2,0,0,1,2,2,2,2,2,2,0,2,1,1,1,1,1,2,0,2,2,2,0,2,0,1,0,1,2,1,0,1,2,1,2,1,2,0,2,0,1,0,1,2,2,1,2,2,1,0,0,1,2,1,1,0,0,2,1,0,2,1,2,0,0,1,0,2,0,1,2,2,2,1,2,0,2,2,2,2,2,0,0,0,1,0,2,0,0,1,1,0,0,2,2,1,0,0,0,2,0,1,1,1,2,1,1,2,1,1,0,1,0,1,1,1,2,0,0,2,2,2,1,1,1,2,2,2,0,1,0,0,0,0,1,0,2,2,0,2,2,1,1,1,2,1,1,1,0,2,0,2,1,1,2,2,1,1,2,0,0,2,1,2,0,1,1,1,2,2,0,1,2,2,2,1,1,0,1,0,0,1,2,1,1,0,1,0,2,2,2,0,1,1,0,1,0,1,2,2,2,1,1,0,1,0,0,2,1,1,1,0,0,0,0,2,2,2,0,1,0,2,0,0,0,0,0,0,2,0,1,0,0,0,1,1,2,2,1,2,2,0,2,1,0,2,1,2,0,1,2,1,2,2,2,2,2,0,0,1,0,0,2,2,0,1,0,0,0,2,1,0,1,2,1,1,0,0,1,1,0,0,2,2,2,1,0,0,0,0,0,0,1,0,1,2,0,1,1,2,1,0,0,0,2,2,1,2,2,0,0,1,0,1,0,0,1,2,0,0,0,1,1,0,0,1,0,0,0,0,0,2,0,2,0,0,0,0,0,1,2,1,1,1,2,2,0,2,1,0,2,1,0,2,1,1,0,2,0,2,1,0,0,0,1,1,0,1,0,2,2,2,1,2,0,1,2,0,0,0,2,2,2,1,1,1,2,2,2,2,0,1,0,0,1]))