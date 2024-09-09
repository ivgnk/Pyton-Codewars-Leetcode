"""
Done 09.09.2024. Topics: Array, Matrix
999. Available Captures for Rook
https://leetcode.com/problems/available-captures-for-rook/description/

You are given an 8 x 8 matrix representing a chessboard.
There is exactly one white rook represented by 'R', some number of white bishops 'B',
and some number of black pawns 'p'. Empty squares are represented by '.'.

A rook can move any number of squares horizontally or vertically (up, down, left, right)
until it reaches another piece or the edge of the board.
A rook is attacking a pawn if it can move to the pawn's square in one move.

Note: A rook cannot move through other pieces, such as bishops or pawns.
This means a rook cannot attack a pawn if there is another piece blocking the path.

Return the number of pawns the white rook is attacking.

Example 1:
Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation:
In this example, the rook is attacking all the pawns.

Example 2:
Input: board = [[".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 0
Explanation:
The bishops are blocking the rook from attacking any of the pawns.

Example 3:
Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation:
The rook is attacking the pawns at positions b5, d6, and f5.

Constraints:
board.length == 8
board[i].length == 8
board[i][j] is either 'R', '.', 'B', or 'p'
There is exactly one cell with board[i][j] == 'R'
"""
import numpy as np
from icecream import ic
# https://leetcode.com/problems/available-captures-for-rook/description/comments/2172289
# Tip
# -- Locate your rook on the grid, store it's position in a var(rook_position = [y,x].
# -- Now move your rook in all 4 directions.
# -- For each direction(up(y-1), down(y+1), left(x-1), right(x+1))...
# keep going in the direction upon encounter a bishop(end the loop),
# pawn(answer += 1, end the loop) or out of bounds(index of -1 or 8 depending on the direction, end the loop).
# -- Return your answer.

# Runtime 12 ms Beats 80.22%
# Memory 11.70 MB Beats 64.84%
# Time Complexity O(1)
# Space Complexity O(1)
def numRookCaptures(b):
    """
    :type board: List[List[str]]
    :rtype: int
    """
    for i in range(8):
        for j in range(8):
            if b[i][j]=='R':
                row,col=i,j
                break
    # ic(row,col)
    n=0
    # to right
    for i in range(col+1,8):
        if b[row][i]=='p':
            n+=1; break
        elif b[row][i]=='B': break
    # ic('right = ',n)
    # to left
    for i in range(col-1,-1,-1):
        if b[row][i]=='p':
            n+=1; break
        elif b[row][i]=='B': break
    # ic('left = ',n)

    # to bot
    for i in range(row+1,8):
        if b[i][col]=='p':
            n+=1; break
        elif b[i][col]=='B': break
    # ic('bot = ',n)

    # to top
    for i in range(row-1,-1,-1):
        if b[i][col]=='p':
            n+=1; break
        elif b[i][col]=='B': break
    return n

# Runtime 37 ms Beats 7.69%
# Memory 23.04 MB Beats 21.98%
def numRookCaptures2(board):
    """
    :type board: List[List[str]]
    :rtype: int
    """
    b=np.array(board)
    c=np.where(b == 'R') # row col
    row=c[0][0]
    col=c[1][0]
    # ic(row,col)
    n=0
    # to right
    for i in range(col+1,8):
        if b[row,i]=='p':
            n+=1; break
        elif b[row,i]=='B': break
    # ic('right = ',n)
    # to left
    for i in range(col-1,-1,-1):
        if b[row,i]=='p':
            n+=1; break
        elif b[row,i]=='B': break
    # ic('left = ',n)

    # to bot
    for i in range(row+1,8):
        if b[i,col]=='p':
            n+=1; break
        elif b[i,col]=='B': break
    # ic('bot = ',n)

    # to top
    for i in range(row-1,-1,-1):
        if b[i,col]=='p':
            n+=1; break
        elif b[i,col]=='B': break
    return n

ic(numRookCaptures([[".",".",".",".",".",".",".","."],
                       [".",".",".","p",".",".",".","."],
                       [".",".",".","R",".",".",".","p"],
                       [".",".",".",".",".",".",".","."],
                       [".",".",".",".",".",".",".","."],
                       [".",".",".","p",".",".",".","."],
                       [".",".",".",".",".",".",".","."],
                       [".",".",".",".",".",".",".","."]])) # 3
ic(numRookCaptures([[".",".",".",".",".",".",".","."],
                    [".",".",".",".",".",".",".","."],
                    [".",".",".",".",".",".",".","."],
                    [".",".",".","R",".",".",".","."],
                    [".",".",".",".",".",".",".","."],
                    [".",".",".",".",".",".",".","."],
                    [".",".",".",".",".",".",".","."],
                    [".",".",".",".",".",".",".","."]]))