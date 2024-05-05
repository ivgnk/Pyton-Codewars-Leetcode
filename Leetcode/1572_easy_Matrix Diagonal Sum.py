"""
Done 05.05.2024
1572. Matrix Diagonal Sum
Given a square matrix mat, return the sum of the matrix diagonals.
Only include the sum of all the elements on the primary diagonal and
all the elements on the secondary diagonal that are not part of the primary diagonal.

Example 1:
Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.

Example 2:
Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8

Example 3:
Input: mat = [[5]]
Output: 5
"""

# Runtime 146 ms Beats 5.31% of users with Python
# Memory 23.17 MB Beats 13.66% of users with Python
# Runtime 103 ms Beats 5.31% of users with Python
# Memory 23.28 MB Beats 13.66% of users with Python
# Runtime 100 ms Beats 5.31% of users with Python
# Memory 23.21 MB Beats 13.66% of users with Python

import numpy as np
def diagonalSum(mat):
    """
    :type mat: List[List[int]]
    :rtype: int
    """
    b = np.array(mat)
    c = b.shape
    # if c[0]==1: return mat[0][0]
    a1 = np.trace(b)
    b = np.fliplr(b)
    d=np.trace(b) + a1
    if c[0]%2==0:
        return d
    else:
        return d - np.diag(b)[c[0]//2]

print(diagonalSum([[1,2,3], [4,5,6], [7,8,9]]))
# print(diagonalSum(mat = [[5]]))
