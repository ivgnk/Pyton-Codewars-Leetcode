"""
03.11.2024. Topics: Array, Queue, Sliding Window, Heap (Priority Queue)
239. Sliding Window Maximum.
https://leetcode.com/problems/sliding-window-maximum/

You are given an array of integers nums, there is a sliding window of size k which
is moving from the very left of the array to the very right.
You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length

Hint 1
How about using a data structure such as deque (double-ended queue)?
Hint 2
The queue size need not be the same as the window’s size.
Hint 3
Remove redundant elements and the queue should store only elements that need to be considered.
"""

import inspect
import itertools
from collections import deque
from typing import List

from icecream import ic

class Solution2(object):
    def __init__(self):
        self.sliding_window_max = []

    def maxSlidingWindow(self, nums, k):
        while len(nums) >= k:
            window = nums[0:k]
            self.sliding_window_max.append(max(window))
            nums.pop(0)
        return self.sliding_window_max

# Time Limit Exceeded - 37 / 51 testcases passed
def maxSlidingWindow2(nums, k):
    ll=len(nums); res=[]
    for i in range(ll-k+1):
        res.append(max(nums[i:i+k]))
    return res

# Time Limit Exceeded - 37 / 51 testcases passed
def maxSlidingWindow3(nums, k):
    return [max(nums[i:i+k]) for i in range(len(nums)-k+1)]

# Time Limit Exceeded - 37 / 51 testcases passed
# Двусторонняя очередь в Python
# https://docs-python.ru/standart-library/modul-collections-python/klass-deque-modulja-collections/
def maxSlidingWindow4(nums, k):
    if k==1: return nums
    d = deque(nums[0:k],k)
    res=[max(d)]
    # ic(d, res)
    for i in range(k,len(nums)):
        d.append(nums[i])
        res.append(max(d))
        # d.popleft()
    return res

# Runtime 1144 ms Beats 5.01%
# Memory 30.62 MB Beats 85.33%
# https://www.geeksforgeeks.org/python-sorted-containers-an-introduction/
from sortedcontainers import SortedList
def maxSlidingWindow_1(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    ans = []
    heap = SortedList()  # Using SortedList from `sortedcontainers` module
    for i in range(n):
        heap.add(nums[i])
        if i >= k:
            heap.remove(nums[i - k])
        if i >= k - 1:
            ans.append(heap[-1])
    return ans

# Runtime: 126ms
def maxSlidingWindow_2(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    if k >= n:
        return [max(nums)]

    stack = deque()
    for i in range(k):
        while stack and stack[-1] < nums[i]:
            stack.pop()
        stack.append(nums[i])

    ans = [stack[0]]
    for i in range(k, n):
        if nums[i - k] == stack[0]:
            stack.popleft()
        while stack and stack[-1] < nums[i]:
            stack.pop()
        stack.append(nums[i])
        ans.append(stack[0])
    return ans

# Runtime: 198ms
def maxSlidingWindow_3(nums: List[int], k: int) -> List[int]:
    queue = deque([])
    ans = []
    for i in range(len(nums)):
        while (queue and queue[-1][0] < nums[i]):
            queue.pop()
        queue.append((nums[i], i))
        if i - queue[0][1] >= k:
            queue.popleft()
        if i >= k - 1:
            ans.append(queue[0][0])
    return ans

import heapq
def maxSlidingWindow_4(nums: List[int], k: int) -> List[int]:
    hq = []
    res = []
    for i in range(k):
        heapq.heappush(hq, (-nums[i], i))
    for j in range(k, len(nums)):
        res.append(-hq[0][0])
        heapq.heappush(hq, (-nums[j], j))
        left = j - k
        while hq[0][1] <= left:
            heapq.heappop(hq)

    res.append(-hq[0][0])
    return res


def maxSlidingWindow_5(self, nums: List[int], k: int) -> List[int]:
    # plan: max heap to track items in window
    # pop off heap until item in window
    heap = []
    out = []
    for i, n in enumerate(nums):
        heapq.heappush(heap, (-n, i))
        if len(heap) >= k:
            while heap[0][1] <= i - k:
                heapq.heappop(heap)
            out.append(-heap[0][0])
    return out

# Runtime: 584ms
def maxSlidingWindow_6(nums: List[int], k: int) -> List[int]:
        q = []
        ans = []
        for i,num in enumerate(nums):
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(i)
            if i-q[0] >= k: q.pop(0)
            if i >= k-1:  ans.append(nums[q[0]])
        return ans

import time
if __name__=="__main__":
    ic(maxSlidingWindow_1([1,3,-1,-3,5,3,6,7],3))
