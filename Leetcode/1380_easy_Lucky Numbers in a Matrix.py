"""
1380. Lucky Numbers in a Matrix
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

Example 1:
Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 2:
Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
"""
import numpy as np

# Runtime 283 ms Beats 5.09% of users with Python3
# Memory 37.24 MB Beats 9.54% of users with Python3

def luckyNumbers (matrix):
    a=np.array(matrix)
    row=a.shape[0]
    col=a.shape[1]
    res=[]
    for i in range(row):
        for j in range(col):
            if a[i,j]==a[i].min() and a[i,j]==a[:,j].max():
                res.append(a[i,j])
    return res

# print(luckyNumbers(matrix = [[3,7,8],[9,11,13],[15,16,17]]))
# print(luckyNumbers(matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]))
print(luckyNumbers(matrix =  [[7,8],[1,2]]))