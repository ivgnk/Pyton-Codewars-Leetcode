"""
Done 22.06.2024. Topics: Array, Hash Table

2352. Equal Row and Column Pairs
https://leetcode.com/problems/equal-row-and-column-pairs/

Given a 0-indexed n x n integer matrix grid,
return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if
they contain the same elements in the same order (i.e., an equal array).

Example 1:
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Example 2:
Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]

Hint 1
We can use nested loops to compare every row against every column.
Hint 2
Another loop is necessary to compare the row and column element by element.
Hint 3
It is also possible to hash the arrays and compare the hashed values instead.
"""

# Runtime 4663 ms Beats 5.06%
# Memory 27.24 MB Beats 5.06%
import numpy as np
def equalPairs2(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    row=len(grid)
    col=len(grid[0])
    gr=np.array(grid)
    n=0
    rc=range(row); rr=range(col)
    for i in rc:
        for j in rr:
            if list(gr[i,:])==list(gr[:,j]):
                n=n+1
    return n

# Runtime 430 ms Beats 66.78%
# Memory 26.98 MB Beats 5.06%
# Runtime 425 ms Beats 67.99%
# Memory 26.93 MB Beats 5.06%
def equalPairs(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    row=len(grid)
    col=len(grid[0])

    rrow=range(row); rcol=range(col)
    nr=dict()
    for i in rrow:
        tr=tuple(grid[i])
        if tr in nr:
            nr[tr]=nr[tr]+1
        else:
            nr[tr] = 1

    nc = dict()
    for j in rcol:
        res=[]
        for i in rrow:
            res.append(grid[i][j])
        tc=tuple(res)
        if tc in nc:
            nc[tc]=nc[tc]+1
        else:
            nc[tc] = 1

    n=0
    for kr,vr in nr.items():
        for kc,vc in nc.items():
            if kr==kc:
                n=n+vr*vc
    return n

# print(equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
print(equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))


