"""
Done 15.07.2024. Topics: Array
3128. Right Triangles
https://leetcode.com/problems/right-triangles/description/

You are given a 2D boolean matrix grid.
Return an integer that is the number of right triangles that
can be made with the 3 elements of grid such that all of them have a value of 1.

Note:
A collection of 3 elements of grid is a right triangle if one of its elements is in the same row with another
element and in the same column with the third element. The 3 elements do not have to be next to each other.

Example 1:
0	1	0
0	1	1
0	1	0
0	1	0
0	1	1
0	1	0
Input: grid = [[0,1,0],[0,1,1],[0,1,0]]
Output: 2
Explanation:
There are two right triangles.

Example 2:
1	0	0	0
0	1	0	1
1	0	0	0
Input: grid = [[1,0,0,0],[0,1,0,1],[1,0,0,0]]
Output: 0
Explanation:
There are no right triangles.

Example 3:
1	0	1
1	0	0
1	0	0
1	0	1
1	0	0
1	0	0
Input: grid = [[1,0,1],[1,0,0],[1,0,0]]

Output: 2
Explanation:
There are two right triangles.

Constraints:
1 <= grid.length <= 1000
1 <= grid[i].length <= 1000
0 <= grid[i][j] <= 1

Hint 1
If grid[x][y] is 1, it can form a right triangle with an element of grid with value 1 in the same row and an element of grid with value 1 in the same column.
Hint 2
So we just need to count the number of 1s in each row and column.
Hint 3
For each x, y with grid[x][y] = 1 if there are row[x] 1s in the row x and col[y] 1s in column y, the answer should be added by (row[x] - 1) * (col[y] - 1).
"""

# Runtime 2400 ms Beats 75.76%
# Memory 61.52 MB Beats 6.06%

from icecream import ic
def numberOfRightTriangles2(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    nrow=len(grid);    ncol=len(grid[0])
    rn=[0]*nrow;    cn=[0]*ncol
    for i in range(nrow):
        rn[i]=sum(grid[i])
    for i in range(ncol):
        for j in range(nrow):
            cn[i]=cn[i]+grid[j][i]

    ntr=[(rn[i] - 1) * (cn[j] - 1) for i in range(nrow)
                for j in range(ncol)
                    if  grid[i][j]==1]
    return sum(ntr)

# Runtime 2377 ms Beats 81.82%
# Time Complexity O(N**2)
# Memory 61.39 MB Beats 6.06%
# Space Complexity O(N+N**2)

def numberOfRightTriangles(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    nrow=len(grid);    ncol=len(grid[0])
    rn=[0]*nrow;    cn=[0]*ncol
    rr=range(nrow); rc=range(ncol)
    for i in rr:
        rn[i]=sum(grid[i])
    for i in rc:
        for j in rr:
            cn[i]=cn[i]+grid[j][i]

    return sum([(rn[i] - 1) * (cn[j] - 1) for i in rr
                for j in rc
                    if  grid[i][j]==1])

ic(numberOfRightTriangles([[0,1,0],[0,1,1],[0,1,0]]))
ic(numberOfRightTriangles([[1,0,0,0],[0,1,0,1],[1,0,0,0]]))
ic(numberOfRightTriangles([[1,0,1],[1,0,0],[1,0,0]]))



