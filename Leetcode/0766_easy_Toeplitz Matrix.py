"""
766. Toeplitz Matrix. Topics: Array, Matrix
https://leetcode.com/problems/toeplitz-matrix/description/

Given an m x n matrix, return true if the matrix is Toeplitz.
Otherwise, return false.
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

Example 1:
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.

Example 2:
Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 20
0 <= matrix[i][j] <= 99

Follow up:
What if the matrix is stored on disk,
and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
What if the matrix is so large that you can only load up a partial row into the memory at once?
"""

# Runtime 113 ms Beats 12.68%
# Memory 11.67 MB Beats 49.48%
def isToeplitzMatrix(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: bool
    """
    # https://blog.finxter.com/5-best-ways-to-check-whether-a-given-matrix-is-toeplitz-in-python/
    rows, cols = len(matrix), len(matrix[0])
    for row in range(rows - 1):
        for col in range(cols - 1):
            if matrix[row][col] != matrix[row + 1][col + 1]:
                return False
    return True
