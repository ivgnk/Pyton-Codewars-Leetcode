"""
Done 14.10.2024. Topics: Heap (Priority Queue)
2530. Maximal Score After Applying K Operations
https://leetcode.com/problems/maximal-score-after-applying-k-operations/

You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.

In one operation:
- choose an index i such that 0 <= i < nums.length,
- increase your score by nums[i], and
- replace nums[i] with ceil(nums[i] / 3).
- Return the maximum possible score you can attain after applying exactly k operations.

The ceiling function ceil(val) is the least integer greater than or equal to val.

Example 1:
Input: nums = [10,10,10,10,10], k = 5
Output: 50
Explanation: Apply the operation to each array element exactly once. The final score is 10 + 10 + 10 + 10 + 10 = 50.

Example 2:
Input: nums = [1,10,3,3,3], k = 3
Output: 17
Explanation: You can do the following operations:
Operation 1: Select i = 1, so nums becomes [1,4,3,3,3]. Your score increases by 10.
Operation 2: Select i = 1, so nums becomes [1,2,3,3,3]. Your score increases by 4.
Operation 3: Select i = 2, so nums becomes [1,1,1,3,3]. Your score increases by 3.
The final score is 10 + 4 + 3 = 17.

Constraints:
1 <= nums.length, k <= 105
1 <= nums[i] <= 109

Hint 1
It is always optimal to select the greatest element in the array.
Hint 2
Use a heap to query for the maximum in O(log n) time.

My solution
✏️ Python solution with heapq
https://leetcode.com/problems/maximal-score-after-applying-k-operations/solutions/5912332/python-solution-with-heapq/

Intuition
Use information in hints and tags

Approach
Standard using heapq functions
The Solution without heapq gives the answer:
"Time Limit Exceeded - 32 / 39 testcases passed"
"""
# Runtime 719 ms Beats 68.35%
# Memory 31.35 MB Beats 20.57%
# Time Complexity O(NLogK)
# Space Complexity O(K)
import heapq
def maxKelements(nums, k):
    nums=[-n for n in nums]
    ssum = 0
    heapq.heapify(nums)
    for i in range(k):
        dat=heapq.heappop(nums)
        ssum = ssum - dat
        heapq.heappush(nums, -ceil(-dat / 3))
    return ssum

# Time Limit Exceeded - 32 / 39 testcases passed
from  math import ceil
def maxKelements2(nums, k):
    ssum = 0
    for i in range(k):
        mmax = max(nums)
        ind = nums.index(mmax)
        ssum = ssum + mmax
        nums[ind] = ceil(mmax / 3)
    return ssum

print(maxKelements(nums = [10,10,10,10,10], k = 5))
print(maxKelements(nums = [1,10,3,3,3], k = 3))