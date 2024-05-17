"""
Done 17.05.2024. Topics: Array, Matrix, Simulation
2482. Difference Between Ones and Zeros in Row and Column
https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/description/

You are given a 0-indexed m x n binary matrix grid.

A 0-indexed m x n difference matrix diff is created with the following procedure:
Let the number of ones in the ith row be onesRowi.
Let the number of ones in the jth column be onesColj.
Let the number of zeros in the ith row be zerosRowi.
Let the number of zeros in the jth column be zerosColj.
diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
Return the difference matrix diff.

Example 1:
Input: grid = [[0,1,1],[1,0,1],[0,0,1]]
Output: [[0,0,4],[0,0,4],[-2,-2,2]]
Explanation:
- diff[0][0] = onesRow0 + onesCol0 - zerosRow0 - zerosCol0 = 2 + 1 - 1 - 2 = 0
- diff[0][1] = onesRow0 + onesCol1 - zerosRow0 - zerosCol1 = 2 + 1 - 1 - 2 = 0
- diff[0][2] = onesRow0 + onesCol2 - zerosRow0 - zerosCol2 = 2 + 3 - 1 - 0 = 4
- diff[1][0] = onesRow1 + onesCol0 - zerosRow1 - zerosCol0 = 2 + 1 - 1 - 2 = 0
- diff[1][1] = onesRow1 + onesCol1 - zerosRow1 - zerosCol1 = 2 + 1 - 1 - 2 = 0
- diff[1][2] = onesRow1 + onesCol2 - zerosRow1 - zerosCol2 = 2 + 3 - 1 - 0 = 4
- diff[2][0] = onesRow2 + onesCol0 - zerosRow2 - zerosCol0 = 1 + 1 - 2 - 2 = -2
- diff[2][1] = onesRow2 + onesCol1 - zerosRow2 - zerosCol1 = 1 + 1 - 2 - 2 = -2
- diff[2][2] = onesRow2 + onesCol2 - zerosRow2 - zerosCol2 = 1 + 3 - 2 - 0 = 2

Example 2:
Input: grid = [[1,1,1],[1,1,1]]
Output: [[5,5,5],[5,5,5]]
Explanation:
- diff[0][0] = onesRow0 + onesCol0 - zerosRow0 - zerosCol0 = 3 + 2 - 0 - 0 = 5
- diff[0][1] = onesRow0 + onesCol1 - zerosRow0 - zerosCol1 = 3 + 2 - 0 - 0 = 5
- diff[0][2] = onesRow0 + onesCol2 - zerosRow0 - zerosCol2 = 3 + 2 - 0 - 0 = 5
- diff[1][0] = onesRow1 + onesCol0 - zerosRow1 - zerosCol0 = 3 + 2 - 0 - 0 = 5
- diff[1][1] = onesRow1 + onesCol1 - zerosRow1 - zerosCol1 = 3 + 2 - 0 - 0 = 5
- diff[1][2] = onesRow1 + onesCol2 - zerosRow1 - zerosCol2 = 3 + 2 - 0 - 0 = 5

Hint 1
You need to reuse information about a row or a column many times.
Try storing it to avoid computing it multiple times.
Hint 2
Use an array to store the number of 1’s in each row and another array to store the number of 1’s in each column.
Once you know the number of 1’s in each row or column, you can also easily calculate the number of 0’s.
"""

# Runtime 1213 ms Beats 72.99% of users with Python
# Memory 42.72 MB Beats 98.54% of users with Python

def onesMinusZeros(grid):
    """
    :type grid: List[List[int]]
    :rtype: List[List[int]]
    """
    nr=len(grid)
    nc=len(grid[0])
    onesRow = [0] * nr; onesCol=[0]*nc
    zerosRow = [nc] * nr; zerosCol = [nr] * nc
    for i in range(nr):
        onesRow[i]=grid[i].count(1)
        zerosRow[i]=zerosRow[i]-onesRow[i]
    for j in range(nc):
        for i in range(nr):
            if grid[i][j]==1:
                onesCol[j]=onesCol[j]+1
        zerosCol[j]=zerosCol[j]-onesCol[j]
    for i in range(nr):
        for j in range(nc):
            grid[i][j]=onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]
    return grid

print(onesMinusZeros([[0,1,1],[1,0,1],[0,0,1]]))