"""
Done 06.05.2024
Wrong Answer -- 219 / 227 testcases passed
2133. Check if Every Row and Column Contains All Numbers
https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/description/

An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).
Given an n x n integer matrix, return true if the matrix is valid. Otherwise, return false.

Example 1:
Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
Output: true
Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
Hence, we return true.

Example 2:
Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
Output: false
Explanation: In this case, n = 3, but the first row and the first column do not contain the numbers 2 or 3.
Hence, we return false.
"""

import numpy as np
def checkValid2(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: bool
    """
    ll=len(matrix)
    r = range(1,ll+1)
    d = sum(r)
    b = np.array(matrix)
    if len(set(b.flatten()))<ll: return False
    b0=b.sum(axis=0)
    b1=b.sum(axis=1)
    if not all(b0==b1):
        return False
    elif not all([i==d for i in b0]):
        return False
    elif not all([i==d for i in b1]):
        return False
    return True

# Runtime 653 ms Beats 25.45% of users with Python
# Memory 23.16 MB Beats 5.45% of users with Python

def checkValid(matrix):
    ll = len(matrix)
    rng = range(ll)
    b = np.array(matrix)
    if not all([len(set(b[row, :])) == ll for row in rng]):
        return False
    elif not all([len(set(b[:, col])) == ll for col in rng]):
        return False
    else:
        return True


# print(checkValid( [[1,2,3],[3,1,2],[2,3,1]]))
print(checkValid([[1,1,1],[1,2,3],[1,2,3]] ))