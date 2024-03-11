'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
'''

import numpy as np

def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    print(f'{matrix=}\n')
    a = np.array(matrix)
    print(f'{a=}\n')
    b = np.rot90(a,-1)
    print(f'{b=}\n')
    return b.tolist()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))
