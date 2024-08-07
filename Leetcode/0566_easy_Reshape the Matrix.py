"""
Done 07.08.2024. Topics: Array, Matrix,
566. Reshape the Matrix
https://leetcode.com/problems/reshape-the-matrix/description/

In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into
a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing
the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix
in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix;
Otherwise, output the original matrix.

Example 1:
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:
Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 100
-1000 <= mat[i][j] <= 1000
1 <= r, c <= 300

Hint 1
Do you know how 2d matrix is stored in 1d memory? Try to map 2-dimensions into one.
Hint 2
M[i][j]=M[n*i+j] , where n is the number of cols. This is the one way of converting 2-d indices into one 1-d index. Now, how will you convert 1-d index into 2-d indices?
Hint 3
Try to use division and modulus to convert 1-d index into 2-d indices.
Hint 4
M[i] => M[i/n][i%n] Will it result in right mapping? Take some example and check this formula.
"""

import numpy as np

# Runtime 55 ms Beats 79.92%
# Memory 12.56 MB Beats 12.45%
def matrixReshape(mat, r, c):
    row=len(mat)
    col=len(mat[0])
    if row * col != r * c: return mat
    res=[[0]*c for _ in range(r)]
    a=sum(mat, []); n=0
    for i in range(r):
        for j in range(c):
            res[i][j]=a[n]
            n=n+1
    return res

print(matrixReshape(mat = [[1,2],[3,4]], r = 1, c = 4))
print(matrixReshape( mat = [[1,2],[3,4]], r = 2, c = 4))


# Runtime 80 ms Beats 5.62%
# Memory 23.59 MB Beats 12.45%
def matrixReshape2(mat, r, c):
    """
    :type mat: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    if len(mat) * len(mat[0]) != r * c: return mat
    return np.reshape(np.array(mat), (r, c)).tolist()

# Runtime 101 ms Beats 5.22%
# Memory 23.54 MB Beats 12.45%
def matrixReshape(mat, r, c):
    """
    :type mat: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    if len(mat)*len(mat[0]) != r*c: return mat
    a = np.array(mat)
    a = np.reshape(a,(r, c))
    return a.tolist()



