"""
Done 05.05.2024
2319. Check if Matrix Is X-Matrix
A square matrix is said to be an X-Matrix if both of the following conditions hold:
- All the elements in the diagonals of the matrix are non-zero.
- All other elements are 0.
Given a 2D integer array grid of size n x n representing a square matrix, return true if grid is an X-Matrix. Otherwise, return false.

Example 1:
Input: grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
Output: true
Explanation: Refer to the diagram above.
An X-Matrix should have the green elements (diagonals) be non-zero and the red elements be 0.
Thus, grid is an X-Matrix.

Example 2:
Input: grid = [[5,7,0],[0,3,1],[0,5,0]]
Output: false
Explanation: Refer to the diagram above.
An X-Matrix should have the green elements (diagonals) be non-zero and the red elements be 0.
Thus, grid is not an X-Matrix.
"""

# Runtime 237 ms Beats 7.21% of users with Python
# Memory 23.74 MB Beats 8.11% of users with Python

import numpy as np
from icecream import ic
def checkXMatrix(grid):
    """
    :type grid: List[List[int]]
    :rtype: bool
    """
    ll=len(grid)
    b = np.array(grid)

    # Преобразование массива в булев
    bool_arr = (b == 0)
    # Подсчет количества искомых элементов
    count = np.count_nonzero(bool_arr)

    if 0 in b.diagonal(): print(1); return False
    b = np.fliplr(b)
    if 0 in b.diagonal(): print(2); return False
    nn = ll*ll-2*ll; print(nn,count)
    if ll%2==0:
        return nn==count
    else:
        return nn+1 == count



print(checkXMatrix([[5,0,20],[0,5,0],[6,0,2]]))
# print(checkXMatrix([[5,7,0],[0,3,1],[0,5,0]]))