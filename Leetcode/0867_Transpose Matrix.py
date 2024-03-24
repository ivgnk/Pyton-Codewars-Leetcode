'''
867. Transpose Matrix
https://leetcode.com/problems/transpose-matrix/description/

Given a 2D integer array matrix, return the transpose of matrix.
The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
'''

import numpy as np

# Runtime 75 ms
# Beats 10.62% of users with Python
# Memory 23.50 MB
# Beats 5.84% of users with Python

def transpose(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    d = np.array(matrix)
    r = d.transpose()
    return r.tolist()

print(transpose([[1,2,3],[4,5,6],[7,8,9]]))
