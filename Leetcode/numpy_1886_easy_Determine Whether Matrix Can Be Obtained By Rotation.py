"""
Done 12.09.2024. Topics: Array, Matrix

1886. Determine Whether Matrix Can Be Obtained By Rotation
https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/description/

Given two n x n binary matrices mat and target, return true if it is possible to make mat equal
to target by rotating mat in 90-degree increments, or false otherwise.

Example 1:
Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.

Example 2:
Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.

Example 3:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.

Constraints:
n == mat.length == target.length
n == mat[i].length == target[i].length
1 <= n <= 10
mat[i][j] and target[i][j] are either 0 or 1.

Hint 1
What is the maximum number of rotations you have to check?
Hint 2
Is there a formula you can use to rotate a matrix 90 degrees?

Solution
✏️ Special super lazy Python solution

Intuition
Use NumPy !!!
Why reinvent the wheel when there are ready-made algorithms?

Approach
Use NumPy functions:
np.rot90 - for rotation
np.array_equal - for comparing
"""

# Runtime 70 ms Beats 6.09%
# Memory 22.71 MB Beats 8.70%

import numpy as np

def findRotation(mat, target):
    """
    :type mat: List[List[int]]
    :type target: List[List[int]]
    :rtype: bool
    """
    if mat==target: return True
    m=np.array(mat)
    t=np.array(target)
    # ------- 1
    m=np.rot90(m)
    b=np.array_equal(m,t)
    if b: return True
    # ------- 2
    m=np.rot90(m)
    b=np.array_equal(m,t)
    if b: return True
    # ------- 3
    m=np.rot90(m)
    return np.array_equal(m,t)

print(findRotation(mat = [[0,1],[1,0]], target = [[1,0],[0,1]]))
print(findRotation(mat = [[0,1],[1,1]], target = [[1,0],[0,1]]))
print(findRotation(mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]))