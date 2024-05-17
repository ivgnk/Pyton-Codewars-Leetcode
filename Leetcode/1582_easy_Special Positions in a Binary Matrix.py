"""
Done 17.05.2024. Topics: Array, Matrix
1582. Special Positions in a Binary Matrix
https://leetcode.com/problems/special-positions-in-a-binary-matrix/description/
see also 2482. Difference Between Ones and Zeros in Row and Column


Given an m x n binary matrix mat, return the number of special positions in mat.
A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

Example 1:
Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

Example 2:
Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1) and (2, 2) are special positions.

Hint 1
Keep track of 1s in each row and in each column. Then while iterating over matrix,
if the current position is 1 and current row as well as current column contains exactly one occurrence of 1.
"""

# Runtime 112 ms Beats 95.48% of users with Python
# Memory 11.92 MB Beats 34.46% of users with Python

from icecream import ic
def numSpecial(mat):
    """
    :type mat: List[List[int]]
    :rtype: int
    """
    nr=len(mat)
    nc=len(mat[0])
    onesRow = [0] * nr; onesCol=[0]*nc
    for i in range(nr):
        onesRow[i]=mat[i].count(1)
    for j in range(nc):
        for i in range(nr):
            if mat[i][j]==1:
                onesCol[j]=onesCol[j]+1

    return sum([1 for i in range(nr) for j in range(nc) if onesRow[i]==1 and onesCol[j]==1 and mat[i][j]==1])


ic(numSpecial([[1,0,0],[0,0,1],[1,0,0]]))