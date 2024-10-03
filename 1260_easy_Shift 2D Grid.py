"""
Done 03.10.2024. Topics: Array, Matrix
1260. Shift 2D Grid
https://leetcode.com/problems/shift-2d-grid/description/

Given a 2D grid of size m x n and an integer k.
You need to shift the grid k times.
In one shift operation:
Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

Example 1:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]

Example 2:
Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

Example 3:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]

Constraints:
m == grid.length
n == grid[i].length
1 <= m <= 50
1 <= n <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100


Hint 1
Simulate step by step. move grid[i][j] to grid[i][j+1].
handle last column of the grid.
Hint 2
Put the matrix row by row to a vector. take k % vector.length
and move last k of the vector to the beginning.
put the vector to the matrix back the same way.

My solution
"""

import numpy as np

def shiftGrid2(grid, k):
    """
    :type grid: List[List[int]]
    :type k: int
    :rtype: List[List[int]]
    """
    row=len(grid)
    col=len(grid[0])
    m=np.array(grid).flatten()
    m=np.roll(m, k)
    m1=m.tolist()
    n=0
    for i in range(row):
        for j in range(col):
            grid[i][j]=m1[n]
            n+=1
    return grid

def shiftGrid3(grid, k):
    row=len(grid)
    col=len(grid[0])
    m=np.array(grid).flatten()
    m=np.roll(m, k)
    m=m.reshape((row,col))
    return m.tolist()

# Runtime 144 ms Beats 13.89%
# Memory 22.96 MB Beats 5.56%
def shiftGrid4(grid, k):
    m = np.array(grid).flatten()
    m = np.roll(m, k)
    m = m.reshape((len(grid), len(grid[0])))
    return m.tolist()

# Runtime 140 ms Beats 13.89%
# Memory 22.96 MB Beats 5.56%
def shiftGrid(grid, k):
    m = np.roll(np.array(grid).flatten(), k)
    return m.reshape((len(grid), len(grid[0]))).tolist()


print(shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1))