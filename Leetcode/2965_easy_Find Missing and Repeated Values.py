"""
Done 08.05.2024. Topics: Array, Hash Table, Math, Matrix
2965. Find Missing and Repeated Values
You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2].
Each integer appears exactly once except a which appears twice and b which is missing.
The task is to find the repeating and missing numbers a and b.
Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

Example 1:
Input: grid = [[1,3],[2,2]]
Output: [2,4]
Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].

Example 2:
Input: grid = [[9,1,7],[8,9,2],[3,4,6]]
Output: [9,5]
Explanation: Number 9 is repeated and number 5 is missing so the answer is [9,5].
"""

# Runtime 117 ms Beats 52.27% of users with Python
# Memory 12.23 MB Beats 13.26% of users with Python
# Runtime 115 ms Beats 54.55% of users with Python
# Memory 12.12 MB Beats 28.41% of users with Python
# Runtime 99 ms Beats 81.82% of users with Python
# Memory 12.12 MB Beats 28.41% of users with Python

from collections import Counter
def findMissingAndRepeatedValues(grid):
    """
    :type grid: List[List[int]]
    :rtype: List[int]
    """
    gr=[z for d in grid for z in d]
    dd=dict(Counter(gr))
    lst=[k for k,v in dd.items() if v!=1]
    r=set(list(range(1,len(gr)+1)))
    nou=list(r-set(gr))
    return [lst[0],nou[0]]

print(findMissingAndRepeatedValues([[1,3],[2,2]]))