"""
Done 16.10.2024. Topics: Array
90. Subsets II
https://leetcode.com/problems/subsets-ii/s
Given an integer array nums that may contain duplicates, return all possible
subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10

My solution https://leetcode.com/problems/subsets-ii/solutions/5920147/easy-python-solution-with-set-itertools-combinations-and-sorting/
✏️ Easy Python solution with set, itertools.combinations and sorting

Intuition
For a Python user the task is not difficult: use set and itertools.combinations
Approach
use itertools and sorting results
"""

# Runtime 14 ms Beats 88.03% Analyze Complexity
# Memory 11.89 MB Beats 38.03%

from itertools import combinations
def subsetsWithDup(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ss=set()
    ss.add(())
    ss.add(tuple(nums))
    ll=len(nums)
    # for i in range(ll):
    #     ss.add(tuple([nums[i]]))
    for i in range(1,ll):
        r=list(combinations(nums,i))
        for s1 in r:
            ss.add(tuple(sorted(s1)))

    nums2=list(ss)
    nums2.sort()
    return nums2

print(subsetsWithDup([1,2,2]))
print(subsetsWithDup([0]))
print(subsetsWithDup(nums = [4,4,4,1,4]))