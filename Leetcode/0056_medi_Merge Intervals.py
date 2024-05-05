"""
Done 05.05.2024
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/description/

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

# Runtime 100 ms Beats 63.24% of users with Python
# Memory 16.48 MB Beats 97.96% of users with Python

from copy import deepcopy
def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    i = 1;  n = 0
    intervals = sorted(intervals)
    if len(intervals) == 1: return intervals;
    while True:
        # print(i,intervals)
        if intervals[i - 1][1] >= intervals[i][0]:
            intervals[i - 1][1] = max(intervals[i - 1][1], intervals[i][1])
            del intervals[i];   n = n + 1
        else:
            i = i + 1
        if i > len(intervals) - 1:
            if n == 0:
                break
            else:
                n = 0; i = 1
        if len(intervals) == 1: break
    return intervals

# print(merge([[1,3],[2,6],[8,10],[15,18]]))
# print(merge([[1,4],[4,5]]))
# print(merge([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]))
print(merge([[1,3],[4,6],[5,7]]))