"""
13.06.2024. Topics: Array, Math, Matrix
48. Rotate Image
https://leetcode.com/problems/rotate-image/description/

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""

# https://leetcode.com/problems/rotate-image/solutions/5297759/48-rotate-image/
# Runtime 19 ms Beats 49.56%
# Memory 11.56 MB Beats 75.22%
def rotate(matrix):
    n = len(matrix)
    rn = range(n)
    # print(matrix)
    for i in rn:
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # print(matrix)
    for i in rn:
        matrix[i].reverse()

    # return matrix

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
