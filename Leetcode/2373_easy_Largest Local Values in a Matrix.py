"""
Done 16.05.2024. Topics: Array, Matrix
2373. Largest Local Values in a Matrix
https://leetcode.com/problems/largest-local-values-in-a-matrix/description/

Topics: Array, Matrix
You are given an n x n integer matrix grid.
Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix.

Example 1:
Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
Output: [[9,9],[8,6]]
Explanation: The diagram above shows the original matrix and the generated matrix.
Notice that each value in the generated matrix corresponds to the largest value of a contiguous 3 x 3 matrix in grid.

Example 2:
Input: grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
Output: [[2,2,2],[2,2,2],[2,2,2]]
Explanation: Notice that the 2 is contained within every contiguous 3 x 3 matrix in grid.

Hint 1
Use nested loops to run through all possible 3 x 3 windows in the matrix.
Hint 2
For each 3 x 3 window, iterate through the values to get the maximum value within the window.
"""

# Runtime 273 ms Beats 5.19% of users with Python3
# Memory 37.62 MB Beats 8.51% of users with Python3

import numpy as np
def largestLocal2(grid):
    """
    :type grid: List[List[int]]
    :rtype: List[List[int]]
    """
    n = len(grid)
    arr=np.array(grid)
    if n == 3: return [[np.max(arr)]]
    res=np.zeros((n-2,n-2),dtype=int)
    r = range(n)
    for i in r:
        for j in r:
            res[i,j]=np.max(arr[i:i+3,j:j+3])
    return res.tolist()

# Runtime 129 ms Beats 66.80% of users with Python3
# Memory 17.12 MB Beats 25.11% of users with Python3
def largestLocal(grid):
    """
    :type grid: List[List[int]]
    :rtype: List[List[int]]
    """
    n = len(grid)
    if n == 3: return [[max(c for r in grid for c in r)]]
    n2=n-2; r2=range(n2)
    arr=[[0 for i in r2] for i in r2]
    res=np.zeros((n-2,n-2),dtype=int)
    for i in r2:
        for j in r2:
            arr[i][j]=max([grid[k][l] for k in range(i,i+3) for l in range(j,j+3)])
    return arr


# print(largestLocal(grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))
# print(largestLocal(grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]))
print(largestLocal([[20,8,20,6,16,16,7,16,8,10],[12,15,13,10,20,9,6,18,17,6],[12,4,10,13,20,11,15,5,17,1],
                    [7,10,14,14,16,5,1,7,3,11],[16,2,9,15,9,8,6,1,7,15],[18,15,18,8,12,17,19,7,7,8],
                    [19,11,15,16,1,3,7,4,7,11],[11,6,5,14,12,18,3,20,14,6],[4,4,19,6,17,12,8,8,18,8],
                    [19,15,14,11,11,13,12,6,16,19]]))