"""
Done 13.06.2024. Topics, Array, Hash Table, Matrix
36. Valid Sudoku
https://leetcode.com/problems/valid-sudoku/description/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8.
Since there are two 8's in the top left 3x3 sub-box, it is invalid.
"""

import numpy as np
# Runtime 175 ms Beats 5.53%
# Memory 36.72 MB Beats 6.14%
# Runtime 172 ms Beats 5.53%
# Memory 36.71 MB Beats 6.14%
def isValidSudoku2(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    ll=9; rll=range(ll)
    a=np.full((ll,ll),None)
    for i in rll:
        for j in rll:
            if board[i][j] != '.':
                a[i][j]=int(board[i][j])
    #--- rows
    for i in rll:
        sset=set(); nnone=0
        for j in rll:
            if a[i][j] is None: nnone=nnone+1
            else: sset.add(a[i][j])
        if ll != nnone+len(sset): return False

    #--- cols
    for j in rll:
        sset=set(); nnone=0
        for i in rll:
            if a[i][j] is None: nnone = nnone + 1
            else: sset.add(a[i][j])
        if ll != nnone + len(sset): return False

    # sub square
    rll3=range(0,ll-2,3)
    for i in rll3:
        for j in rll3:
            nn=0
            sset = set(); nnone = 0
            for k in range(i,i+3):
                for l in range(j, j + 3):
                    nn = nn+1
                    if a[k][l] is None: nnone = nnone + 1
                    else: sset.add(a[k][l])
            if ll != nnone + len(sset):
                return False

    return True

# Runtime 137 ms Beats 5.53%
# Memory 36.71 MB Beats 6.14%
# Runtime 121 ms Beats 5.53%
# Memory 36.49 MB Beats# 6.14%
def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    ll=9; rll=range(ll)
    #--- rows
    for i in rll:
        sset=set(); nnone=0
        for j in rll:
            if board[i][j]=='.': nnone=nnone+1
            else: sset.add(int(board[i][j]))
        if ll != nnone+len(sset): return False

    #--- cols
    for j in rll:
        sset=set(); nnone=0
        for i in rll:
            if board[i][j]=='.': nnone=nnone+1
            else: sset.add(int(board[i][j]))
        if ll != nnone + len(sset): return False

    # sub square
    rll3=range(0,ll-2,3)
    for i in rll3:
        for j in rll3:
            nn=0
            sset = set(); nnone = 0
            for k in range(i,i+3):
                for l in range(j, j + 3):
                    nn = nn+1
                    if board[k][l]=='.': nnone = nnone + 1
                    else: sset.add(board[k][l])
            if ll != nnone + len(sset):
                return False

    return True


# print(np.isnan(a.astype(float)))
    # print(np.equal(a, None))
    # for i in rll:

# ic(isValidSudoku([
#     ["5","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]]))



print(isValidSudoku([
    [".",".",".",".",".",".","5",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    ["9","3",".",".","2",".","4",".","."],
    [".",".","7",".",".",".","3",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".","3","4",".",".",".","."],
    [".",".",".",".",".","3",".",".","."],
    [".",".",".",".",".","5","2",".","."]]))

