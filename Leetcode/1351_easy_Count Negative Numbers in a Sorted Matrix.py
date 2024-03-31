'''
1351. Count Negative Numbers in a Sorted Matrix
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/

Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:
Input: grid = [[3,2],[1,0]]
Output: 0
'''

# Runtime 88 ms Beats 45.36% of users with Python
# Memory 12.79 MB Beats 63.24% of users with Python

import numpy as np
def countNegatives2(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    gr2 = np.array(grid)
    return len(gr2[gr2 < 0])

def countNegatives(grid):
    # https://ru.stackoverflow.com/questions/1188480
    i=0
    for dat in grid:
        for dat2 in dat:
            if dat2<0:
                i = i+1
    return i

print(countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))