"""
Done 13.05.2024
3142. Check if Grid Satisfies Conditions
https://leetcode.com/problems/check-if-grid-satisfies-conditions/description/

You are given a 2D matrix grid of size m x n. You need to check if each cell grid[i][j] is:
Equal to the cell below it, i.e. grid[i][j] == grid[i + 1][j] (if it exists).
Different from the cell to its right, i.e. grid[i][j] != grid[i][j + 1] (if it exists).
Return true if all the cells satisfy these conditions, otherwise, return false.

Example 1:
Input: grid = [[1,0,2],[1,0,2]]
Output: true
Explanation:
All the cells in the grid satisfy the conditions.

Example 2:
Input: grid = [[1,1,1],[0,0,0]]
Output: false
Explanation:
All cells in the first row are equal.

Example 3:
Input: grid = [[1],[2],[3]]
Output: false
Explanation:

Cells in the first column have different values.

Hint 1
Check if each column has same value in each cell.
Hint 2
If the previous condition is satisfied, we can simply check the first cells in adjacent columns.
"""

# Runtime 137 ms Beats 100.00% of users with Python
# Memory 23.02 MB Beats 100.00% of users with Python

import numpy as np
def satisfiesConditions(grid):
    """
    :type grid: List[List[int]]
    :rtype: bool
    """
    a=np.array(grid)
    nrow, ncol=a.shape
    for i in range(ncol):
        if not np.all([a[0, i]==a[j, i]  for j in range(1,nrow)]): return False
    if not  np.all([a[:, i]!=a[:, i-1] for i in range(1,ncol)]): return False
    return True

print(satisfiesConditions([[1,0,2],[1,0,2]]))