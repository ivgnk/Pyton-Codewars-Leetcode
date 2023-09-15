'''
RankUp 012
Write a function that accepts a square matrix (N x N 2D array) and returns the determinant of the matrix.

https://www.codewars.com/kata/52a382ee44408cea2500074c/train/python
 '''
import numpy as np

def determinant(matrix):
    matr = np.array(matrix)
    # print(matr)
    det = round(np.linalg.det(matr))
    return det

def thetest_determinant():
    s = [[5]]
    print(determinant(s))
    s = [[4, 6], [3,8]]
    print(determinant(s))
    s =  [[2,4,2],[3,1,1],[1,2,0]]
    print(determinant(s))

thetest_determinant()