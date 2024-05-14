"""
Done 14.05.2024. Topics: Array, Hash Table, Matrix
73. Set Matrix Zeroes
https://leetcode.com/problems/set-matrix-zeroes/

Given an m x n integer matrix matrix,
if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


Hint 1
If any cell of the matrix has a zero we can record its row and column number using additional memory.
But if you don't want to use extra memory then you can manipulate the array instead.
i.e. simulating exactly what the question says.
Hint 2
Setting cell values to zero on the fly while iterating might lead to discrepancies.
What if you use some other integer value as your marker?
There is still a better approach for this problem with 0(1) space.
Hint 3
We could have used 2 sets to keep a record of rows/columns which need to be set to zero.
But for an O(1) space solution, you can use one of the rows and and one of the columns to keep track of this information.
Hint 4
We can use the first cell of every row and column as a flag.
This flag would determine whether a row or column has been set to zero.
"""

# Runtime 86 ms Beats 75.50% of users with Python
# Memory 11.99 MB Beats 99.96% of users with Python

def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    nr=len(matrix); nc=len(matrix[0])
    row0=[0]*nc
    n0 = [[i,j] for i in range(nr) for j in range(nc) if matrix[i][j]==0]
    sr = set([i[0] for i in n0])
    sc = sorted(set([i[1] for i in n0]))
    for i in range(nr):
        if i in sr: matrix[i]=row0
        else:
            for j in range(nc):
                if j in sc: matrix[i][j]=0




