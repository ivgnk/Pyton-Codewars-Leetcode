"""
Done 12.09.2024. Topics: Array, Matrix
3127. Make a Square with the Same Color
https://leetcode.com/problems/make-a-square-with-the-same-color/description/

You are given a 2D matrix grid of size 3 x 3 consisting only of characters 'B' and 'W'.
Character 'W' represents the white color, and character 'B' represents the black color.

Your task is to change the color of at most one cell so that the matrix has
a 2 x 2 square where all cells are of the same color.

Return true if it is possible to create a 2 x 2 square of the same color, otherwise, return false.

Example 1:
Input: grid = [["B","W","B"],["B","W","W"],["B","W","B"]]
Output: true
Explanation:
It can be done by changing the color of the grid[0][2].

Example 2:
Input: grid = [["B","W","B"],["W","B","W"],["B","W","B"]]
Output: false
Explanation:
It cannot be done by changing at most one cell.

Example 3:
Input: grid = [["B","W","B"],["B","W","W"],["B","W","W"]]
Output: true
Explanation:
The grid already contains a 2 x 2 square of the same color.

Hint 1
It is impossible to create 2 x 2 square with the same color
by changing the color of at most one cell
when the number of ‘W' or 'B’ in all squares is 2.
"""

# Runtime 40 ms Beats 77.78%
# Memory 16.56 MB Beats 35.50%

def canMakeSquare(grid):
    """
    :type grid: List[List[str]]
    :rtype: bool
    """
    s1=grid[0][0]+grid[0][1]+grid[1][0]+grid[1][1]
    if s1.count('B')!=2: return True
    s2=grid[0][1]+grid[0][2]+grid[1][1]+grid[1][2]
    if s2.count('B')!=2: return True
    s3=grid[1][0]+grid[1][1]+grid[2][0]+grid[2][1]
    if s3.count('B')!=2: return True
    s4=grid[1][1]+grid[1][2]+grid[2][1]+grid[2][2]
    if s4.count('B')!=2: return True
    return False

print(canMakeSquare([["B","B","B"],["W","W","W"],["B","B","B"]]))
# print(canMakeSquare([["B","B","B"],["B","B","B"],["B","B","B"]]))
# print(canMakeSquare([["B","B","B"],["W","B","B"],["B","B","B"]]))
# print(canMakeSquare([["W","W","W"],
#                      ["W","B","B"],
#                      ["B","B","B"]]))

def canMakeSquare2(grid):
    """
    :type grid: List[List[str]]
    :rtype: bool
    """
    r2=range(2)
    srow=[gr[0]==gr[1]==gr[2] for gr in grid]
    if grid[0][0] == 'B' and srow[0]==srow[1]==True: return True
    if grid[1][0] == 'B' and srow[1]==srow[2]==True: return True

    scol=[grid[0][j]==grid[1][j]==grid[2][j] for j in range(3)]
    if grid[0][0] == 'B' and scol[0]==scol[1]==True: return True
    if grid[0][1] == 'B' and scol[1]==scol[2]==True: return True



    for gr in grid:
        print(f'{gr[0]=},{gr[1]=},{gr[2]=}')
    for i in r2:
        for j in r2:
            s=grid[i][j]+grid[i+1][j]+grid[i+1][j]+grid[i+1][j+1]
            if not (s.count('B')==2 and s.count('W')==2) and not srow[i] and not srow[i+1]:
                print(s)
                return True
    else: return False

