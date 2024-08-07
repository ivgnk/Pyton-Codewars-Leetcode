"""
Done 07.08.2024. Topics: Array, Hash Table, Sorting
594. Longest Harmonious Subsequence
https://leetcode.com/problems/longest-harmonious-subsequence/description/

We define a harmonious array as an array where the difference between
its maximum value and its minimum value is exactly 1.
Given an integer array nums, return the length of its longest harmonious subsequence
among all its possible subsequences.
A subsequence of array is a sequence that can be derived from the array by deleting
some or no elements without changing the order of the remaining elements.

Example 1:
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].

Example 2:
Input: nums = [1,2,3,4]
Output: 2

Example 3:
Input: nums = [1,1,1,1]
Output: 0

Constraints:
1 <= nums.length <= 2 * 10**4
-10**9 <= nums[i] <= 10**9

intuition
Two important points:
1) The subsequence
2) the members of the subsequence differ by no more than 1

Approach
Use dictionary and sorting
"""

# Runtime 253 ms Beats 46.42%
# Time Complexity O(Nlogn)
# Memory 15.26 MB Beats 7.17%
# Space Complexity O(N)

from icecream import ic
def findLHS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dd=dict()
    for i in range(len(nums)):
        if nums[i] in dd:
            dd[nums[i]]=dd[nums[i]]+1
        else:
            dd[nums[i]] = 1
    dd2=sorted([(k,v) for k,v in dd.items()])
    n=-10_000_000_000
    for i in range(1,len(dd2)):
        if dd2[i][0]-dd2[i-1][0]==1:
            n=max(n,dd2[i][1]+dd2[i-1][1])
    if n>=0: return n
    else: return 0
ic(findLHS([1,3,2,2,5,2,3,7]))
ic(findLHS([1,2,3,4]))
ic(findLHS([1,1,1,1]))



# [1,3,2,2,5,2,3,7]
#  0 1 2 3 4 5 6 7
