"""
Done 08.05.2024. Topics: Array, Math, Greedy, Sorting
976. Largest Perimeter Triangle
https://leetcode.com/problems/largest-perimeter-triangle/description/

Given an integer array nums,
return the largest perimeter of a triangle with a non-zero area,
formed from three of these lengths.
If it is impossible to form any triangle of a non-zero area, return 0.

Example 1:
Input: nums = [2,1,2]
Output: 5
Explanation: You can form a triangle with three side lengths: 1, 2, and 2.

Example 2:
Input: nums = [1,2,1,10]
Output: 0
Explanation:
You cannot use the side lengths 1, 1, and 2 to form a triangle.
You cannot use the side lengths 1, 1, and 10 to form a triangle.
You cannot use the side lengths 1, 2, and 10 to form a triangle.
As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.
"""

from itertools import combinations
from collections import Counter

# Wrong Answer
# 54 / 84 testcases passed
# def largestPerimeter(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     if len(nums)>1000:
#         nums=list(set(nums))
#     comb = list(combinations(nums, 3))
#     lst=[s[0]+s[1]+s[2] for s in comb if s[0]+s[1]>s[2] and s[2]+s[1]>s[0] and s[0]+s[2]>s[1]]
#     if lst==[]: return 0
#     else: return max(lst)

# Runtime 146 ms Beats 57.40% of users with Python
# Memory 12.87 MB Beats 71.60% of users with Python
# Runtime 143 ms Beats 73.96% of users with Python
# Memory 12.80 MB Beats 89.35% of users with Python
# Runtime 141 ms Beats 86.39% of users with Python
# Memory 12.89 MB Beats 71.60% of users with Python

def largestPerimeter(nums):
    s=sorted(nums,reverse=True)
    i=0
    while i < len(s)-2:
        if s[i] + s[i+1] > s[i+2] and s[i+2] + s[i+1] > s[i+0] and s[i+0] + s[i+2] > s[i+1]:
            return s[i] + s[i+1] + s[i+2]
        i=i+1
    return 0


print(largestPerimeter([1,2,1,10]))
