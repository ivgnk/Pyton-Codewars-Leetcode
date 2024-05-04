"""
Done 04.06.2024
2006. Count Number of Pairs With Absolute Difference K
https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/description/

Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.
The value of |x| is defined as:
x if x >= 0.
-x if x < 0.

Example 1:
Input: nums = [1,2,2,1], k = 1
Output: 4
Explanation: The pairs with an absolute difference of 1 are:
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]

Example 2:
Input: nums = [1,3], k = 3
Output: 0
Explanation: There are no pairs with an absolute difference of 3.

Example 3:
Input: nums = [3,2,1,5,4], k = 2
Output: 3
Explanation: The pairs with an absolute difference of 2 are:
- [3,2,1,5,4]
- [3,2,1,5,4]
- [3,2,1,5,4]
"""

from collections import Counter
from icecream import ic

def countKDifference2(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # Runtime 138 ms Beats 52.62% of users with Python
    # Memory 11.56 MB Beats 75.31% of users with Python
    # ll=len(nums); n=0
    # for i in range(ll):
    #     for j in range(i+1,ll):
    #         if abs(nums[i]-nums[j])==k: n=n+1
    # return n

    # Runtime 140 ms Beats 47.38% of users with Python
    # Memory 11.74 MB Beats 12.22% of users with Python
    # ll=len(nums)
    # return sum(1 for i in range(ll)
    #              for j in range(i+1,ll)
    #                if abs(nums[i]-nums[j])==k )

    # Runtime 178 ms Beats 15.71% of users with Python
    # Memory 11.48 MB Beats 95.01% of users with Python
    ll=len(nums)
    return sum(abs(nums[i]-nums[j])==k for i in range(ll)
                 for j in range(i+1,ll))


# https://github.com/doocs/leetcode/blob/main/solution/2000-2099/2006.Count%20Number%20of%20Pairs%20With%20Absolute%20Difference%20K/README_EN.md
# Runtime 55 ms Beats 67.08% of users with Python
# Memory 11.50 MB Beats 75.31% of users with Python
def countKDifference(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    ans = 0
    cnt = Counter()
    for num in nums:
        ans += cnt[num - k] + cnt[num + k]
        cnt[num] += 1
        # ic(num,cnt,ans)
    return ans

ic(countKDifference(nums = [1,2,2,1], k = 1))