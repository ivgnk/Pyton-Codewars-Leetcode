"""
01.11.2024. Topics: Array, Dynamic Programming, Stack, Matrix, Monotonic Stack
85. Maximal Rectangle
Given a rows x cols binary matrix filled with 0's and 1's,
find the largest rectangle containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],
                 ["1","0","1","1","1"],
                 ["1","1","1","1","1"],
                 ["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:
Input: matrix = [["0"]]
Output: 0

Example 3:
Input: matrix = [["1"]]
Output: 1

Constraints:
rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
"""
from typing import List
from icecream import ic

import numpy as np
import sys
# Time Limit Exceeded - 68 / 74 testcases passed
def maximalRectangle4(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    ll = len(matrix)
    ll0 = len(matrix[0])
    matrix = np.array(matrix).astype(int)
    mmax = 0
    if matrix.size == matrix.sum(): return matrix.size
    for i in range(ll):
        for j in range(ll0):
            for ii in range(ll, i, -1):
                for jj in range(ll0, j, -1):
                    Z = matrix[i:ii:1, j:jj:1]
                    if Z.size == Z.sum():
                        mmax = max(mmax, Z.sum())
    return mmax

# Time Limit Exceeded - 68 / 74 testcases passed
def maximalRectangle3(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    ll=len(matrix)
    ll0=len(matrix[0])
    matrix=np.array(matrix).astype(int)
    mmax=0
    if matrix.size == matrix.sum(): return matrix.size
    for i in range(ll):
        for j in range(ll0):
            for ii in range(ll,-1,-1):
                for jj in range(ll0,-1,-1):
                    if ii>i and jj>j:
                        Z = matrix[i:ii:1, j:jj:1]
                        if Z.size==Z.sum():
                            mmax=max(mmax,Z.sum())
    return mmax

def maximalRectangle2( matrix: List[List[str]]) -> int:
    if not matrix or not matrix[0]:  return 0
    dp=[0]*(len(matrix[0])+1)
    res=0
    for j in range (len(matrix)):
        for i in range (len(matrix[0])):
            dp[i]+=int(matrix[j][i])
    for i in range (len(dp)-1):
        res=max(res,dp[i]+dp[i+1])
    return res

# Runtime 2019 ms Beats 5.26%
# Memory 28.35 MB Beats 5.47%
from pprint import pp, pprint
# https://leetcode.com/problems/maximal-rectangle/solutions/1353800/python-dp/
def maximalRectangle(matrix):
    if len(matrix)==0: return 0
    rows=len(matrix)
    cols=len(matrix[0])
    matrix=[[int(matrix[i][j]) for j in range(cols)] for i in range(rows)]
    dp=[[0 for j in range(cols+1)] for i in range(rows+1)]
    max_area=-1
    for i in range(rows):
        for j in range(cols):
            if i == 0: # начальный
                dp[i][j] = matrix[i][j]
            else:
                if matrix[i][j]==0: # если ноль, то сверху не тянем
                    dp[i][j] = matrix[i][j]
                else:  # если не ноль, то сверху тянем
                    dp[i][j]=matrix[i][j]+dp[i - 1][j]

    # pp('dp='); pp(dp)

    for i in range(rows):
        for j in range(cols): # от начала колонок
            current_height = dp[i][j] # текущая высота
            for k in range(j, cols): # от текущей колонки
                current_height = min(current_height, dp[i][k])
                max_area = max(max_area, current_height * (k-j+1)) # k-j+1 -как бы ширина
    return max_area


def tst_01():
    Y = np.arange(16).reshape(4, 4)
    print(Y)
    Z = Y[np.ix_(list(range(0, 2)), list(range(0, 2)))]
    print(Z, Z.sum())
    # array([[0, 3],
    #        [12, 15]])
if __name__=="__main__":
    # tst_01()
    print(maximalRectangle(matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
