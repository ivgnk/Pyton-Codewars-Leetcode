"""
Done 17.07.2024. Topics: Array, Hash Table
2815. Max Pair Sum in an Array
https://leetcode.com/problems/max-pair-sum-in-an-array/description/

You are given an integer array nums.
You have to find the maximum sum of a pair of numbers from nums
such that the largest digit in both numbers is equal.

For example, 2373 is made up of three distinct digits: 2, 3, and 7,
where 7 is the largest among them.
Return the maximum sum or -1 if no such pair exists.

Example 1:
Input: nums = [112,131,411]
Output: -1
Explanation:
Each numbers largest digit in order is [2,3,4].

Example 2:
Input: nums = [2536,1613,3366,162]
Output: 5902
Explanation:
All the numbers have 6 as their largest digit, so the answer is 2536 + 3366 = 5902.

Example 3:
Input: nums = [51,71,17,24,42]
Output: 88
Explanation:
Each number's largest digit in order is [5,7,7,4,4].
So we have only two possible pairs, 71 + 17 = 88 and 24 + 42 = 66.

Constraints:
2 <= nums.length <= 100
1 <= nums[i] <= 10**4

Hint 1
Find the largest and second largest element with maximum digits equal to x where 1<=x<=9.
"""

# Wrong Answer -  2370 / 3008 testcases passed
# nums = [31,25,72,79,74] - choose second largest element
from icecream import ic
from math import inf
def maxSum2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll = len(nums)
    if ll == 1: return -1
    ns = [str(i) for i in nums]
    nss = [[int(s1) for s1 in s] for s in ns]
    nm = [max(n) for n in nss]
    if any([nm[i] == nm[i - 1] for i in range(1, ll)]):
        ssum = -1000000000
        for i in range(ll):
            for j in range(i + 1, ll):
                if nm[i] == nm[j]:
                    ssum = max(ssum, nums[i] + nums[j])
        return ssum
    else:
        return -1

# Runtime 151 ms Beats 30.00%
# Time Complexity O(N**2)
# Memory 16.63 MB Beats 18.38%
# Space Complexity O(N)

def maxSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll = len(nums)
    if ll==1: return -1
    ns=[str(i) for i in nums]
    nss=[[int(s1) for s1 in s] for s in ns]
    # ic(nums);    ic(ns);    ic(nss);
    maxd=[max(d) for d in nss]
    # ic(maxd)
    ssum = -inf
    for i in range(ll):
        for j in range(i+1, ll):
            if maxd[i]==maxd[j]:
                        ssum=max(ssum,nums[i]+nums[j])
                        # ic(i,j,nums[i],nums[j],nums[i]+nums[j])
    if ssum==-inf:
        return -1
    else: return ssum



# ic(maxSum([112,131,411]))  #-1
# ic(maxSum([2536,1613,3366,162])) # 5902
# ic(maxSum([51,71,17,24,42])) # 88
# ic(maxSum([31,25,72,79,74])) # 146
# ic(maxSum([84,91,18,59,27,9,81,33,17,58])) # 165
