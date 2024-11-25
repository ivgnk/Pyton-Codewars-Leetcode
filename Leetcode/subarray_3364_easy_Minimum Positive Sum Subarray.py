"""
Done 25.05.2024.
3364. Minimum Positive Sum Subarray
https://leetcode.com/problems/minimum-positive-sum-subarray/description/

You are given an integer array nums and two integers l and r.
Your task is to find the minimum sum of a subarray whose size
is between l and r (inclusive) and whose sum is greater than 0.

Return the minimum sum of such a subarray.
If no such subarray exists, return -1.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [3, -2, 1, 4], l = 2, r = 3
Output: 1
Explanation:
The subarrays of length between l = 2 and r = 3 where the sum is greater than 0 are:
[3, -2] with a sum of 1
[1, 4] with a sum of 5
[3, -2, 1] with a sum of 2
[-2, 1, 4] with a sum of 3
Out of these, the subarray [3, -2] has a sum of 1, which is the smallest positive sum. Hence, the answer is 1.

Example 2:
Input: nums = [-2, 2, -3, 1], l = 2, r = 3
Output: -1
Explanation:
There is no subarray of length between l and r that has a sum greater than 0. So, the answer is -1.

Example 3:
Input: nums = [1, 2, 3, 4], l = 2, r = 4
Output: 3
Explanation:
The subarray [1, 2] has a length of 2 and the minimum sum greater than 0. So, the answer is 3.

Constraints:
1 <= nums.length <= 100
1 <= l <= r <= nums.length
-1000 <= nums[i] <= 1000

Hint 1
Check every subarray, since constraints are small.
"""
from typing import List

# Runtime 115 ms Beats 100.00%
# Memory 16.73 MB Beats 100.00%
# Time Complexity O(N**2)
# Space Complexity O(1)

def minimumSumSubarray(nums, l, r):
    """
    :type nums: List[int]
    :type l: int
    :type r: int
    :rtype: int
    """
    mmin=float('inf')
    for i in range(len(nums)-l+1):
        for j in range(l,r+1):
            ssum=sum(nums[i:i+j])
            if ssum>0:
                mmin=min(mmin,ssum)
    if mmin==float('inf'): return -1
    else: return mmin

# print(minimumSumSubarray(nums = [3, -2, 1, 4], l = 2, r = 3))
# print(minimumSumSubarray(nums = [-2, 2, -3, 1], l = 2, r = 3))
# print(minimumSumSubarray(nums = [1, 2, 3, 4], l = 2, r = 4))
# print(minimumSumSubarray(nums = [17,13], l = 1, r = 2))
# print(minimumSumSubarray(nums = [-23,3], l = 2, r = 2))

class Solution1:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        small, large = l, r
        print(small, large)
        res = float('inf')
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarr = nums[i: j + 1]
                if l <= len(subarr) <= r:
                    if sum(subarr) > 0:
                        res = min(res, sum(subarr))
        if res == float('inf'):
            return -1
        return res


class Solution2:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float('inf')
        pre = [0]

        # Compute prefix sum
        for num in nums:
            pre.append(pre[-1] + num)

        # Iterate over lengths in the range [l, r]
        for j in range(l, r + 1):
            i = 0
            while j <= len(nums):
                # Calculate subarray sum using prefix sums
                temp = pre[j] - pre[i]
                if temp > 0:
                    ans = min(ans, temp)
                i += 1
                j += 1

        return ans if ans != float('inf') else -1
