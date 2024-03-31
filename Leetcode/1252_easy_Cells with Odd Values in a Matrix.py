'''
1252. Cells with Odd Values in a Matrix
https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/description/

There is an m x n matrix that is initialized to all 0's.
There is also a 2D array indices where each indices[i] = [ri, ci]
represents a 0-indexed location to perform some increment operations on the matrix.

For each location indices[i], do both of the following:
Increment all the cells on row ri.
Increment all the cells on column ci.
Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all locations in indices.

Example 1:
Input: m = 2, n = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix is [[1,3,1],[1,3,1]], which contains 6 odd numbers.

Example 2:
Input: m = 2, n = 2, indices = [[1,1],[0,0]]
Output: 0
Explanation: Final matrix = [[2,2],[2,2]]. There are no odd numbers in the final matrix.
'''

# Runtime 47 ms Beats 12.62%  of users with Python
# Memory 23.10 MB Beats 5.83% of users with Python

import numpy as np
def oddCells(m, n, indices):
    """
    :type m: int
    :type n: int
    :type indices: List[List[int]]
    :rtype: int
    """
    matr=np.zeros((m,n),dtype=int)
    # print(matr,'\n')
    for ind in indices:
        r=ind[0]
        c=ind[1]
        matr[r,:]=matr[r,:]+1
        matr[:,c] = matr[:,c] + 1
        # print(r,matr,'\n')
    #  stackoverflow.com/questions/65252626/how-to-count-even-numbers-and-odd-numbers-in-matrix-in-python
    return matr[matr%2 == 1].size
print(oddCells(m = 2, n = 3, indices = [[0,1],[1,1]]))
