"""
Done 20.05.2024. Topics: Array, Binary Search, Matrix
1901. Find a Peak Element II
https://leetcode.com/problems/find-a-peak-element-ii/description/

A peak element in a 2D grid is an element that is strictly greater than all
of its adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal,
find any peak element mat[i][j] and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.
You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

Example 1:
Input: mat = [[1,4],[3,2]]
Output: [0,1]
Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.

Example 2:
Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
Output: [1,1]
Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.

Hint 1
Let's assume that the width of the array is bigger than the height, otherwise, we will split in another direction.
Hint 2
Split the array into three parts: central column left side and right side.
Hint 3
Go through the central column and two neighbor columns and look for maximum.
Hint 4
If it's in the central column - this is our peak.
Hint 5
If it's on the left side, run this algorithm on subarray left_side + central_column.
Hint 6
If it's on the right side, run this algorithm on subarray right_side + central_column
"""

# Runtime 983 ms Beats 7.84% of users with Python
# Memory 54.22 MB Beats 6.86% of users with Python

import numpy as np
def findPeakGrid(mat):
    """
    :type mat: List[List[int]]
    :rtype: List[int]
    """
    a=np.array(mat)
    return np.unravel_index(a.argmax(),a.shape)

print(findPeakGrid( [[1,4],[3,2]]))