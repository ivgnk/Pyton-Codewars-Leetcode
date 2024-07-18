"""
Done 18.07.2024. Topics: Array, Matrix
74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/description/

You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10**4 <= matrix[i][j], target <= 10**4
"""

# Runtime 27 ms Beats 41.23%
# Analyze Complexity
# Memory 11.95 MB Beats 69.86%
# Runtime 23 ms Beats 72.80%
# Memory 12.27 MB Beats 8.39

def searchMatrix2(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    ll=len(matrix) # ll1=len(matrix[0])
    for i in range(ll):
        if target in matrix[i]:
            return True
    return False

# Runtime 18 ms Beats 94.01%
# Time Complexity O(M∗N)
# Memory 12.18 MB Beats 8.39%
# Space Complexity O(1)
def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    for i in range(len(matrix) ):
        if target in matrix[i]:
            return True
    return False

# Runtime 19 ms Beats 92.13%
# Memory 12.01 MB Beats 33.83%
# https://leetcode.com/problems/search-a-2d-matrix/solutions/5432551/simple-solution-in-3-line-runtime-o-m/
def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    for i in matrix:
        if target in i:
            return True
    return False
