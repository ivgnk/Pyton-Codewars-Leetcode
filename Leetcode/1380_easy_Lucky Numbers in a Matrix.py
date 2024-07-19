"""
Redone 19.07.2024. Topics: Array, Matrix
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

Constraints:
m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 105.
All elements in the matrix are distinct.

Hint 1
Find out and save the minimum of each row and maximum of each column in two lists.
Hint 2
Then scan through the whole matrix to identify the elements that satisfy the criteria.
"""
import numpy as np

# Runtime 283 ms Beats 5.09% of users with Python3
# Memory 37.24 MB Beats 9.54% of users with Python3

def luckyNumbers2(matrix):
    a=np.array(matrix)
    row=a.shape[0]
    col=a.shape[1]
    res=[]
    for i in range(row):
        for j in range(col):
            if a[i,j]==a[i].min() and a[i,j]==a[:,j].max():
                res.append(a[i,j])
    return res

# Runtime 91 ms Beats 64.57%
# Time Complexity O(N∗M)
# Memory 12.00 MB Beats 22.05%
# Space Complexity O(N+M)
def luckyNumbers (matrix):
    ll=len(matrix); rll=range(ll)
    ll1=len(matrix[0]); rll1=range(ll1)
    mi_r=[min(matrix[row]) for row in rll]
    ma_c=[max([matrix[row][col] for row in rll]) for col in rll1]
    return [matrix[i][j] for i in rll
                              for j in rll1
                                    if matrix[i][j]==mi_r[i]==ma_c[j]]


# print(luckyNumbers(matrix = [[3,7,8],[9,11,13],[15,16,17]]))
# print(luckyNumbers(matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]))
print(luckyNumbers(matrix =  [[7,8],[1,2]]))