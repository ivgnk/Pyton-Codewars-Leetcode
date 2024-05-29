"""
Done 30.05.2024. Topics: Array, Depth-First Search, Matrix
419. Battleships in a Board
https://leetcode.com/problems/battleships-in-a-board/description/

Given an m x n matrix board where each cell is a battleship 'X' or empty '.',
return the number of the battleships on board.
Battleships can only be placed horizontally or vertically on board. In other words,
they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column),
where k can be of any size. At least one horizontal or vertical cell separates between two battleships
(i.e., there are no adjacent battleships).

Example 1:
Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2

Example 2:
Input: board = [["."]]
Output: 0

Follow up: Could you do it in one-pass, using only O(1) extra memory and without modifying the values board?
"""

# Runtime 46 ms Beats 48.90% of users with Python
# Memory 15.13 MB Beats 45.05% of users with Python
# Runtime 44 ms Beats 59.34% of users with Python
# Memory 15.09 MB Beats 65.38% of users with Python
# Runtime 43 ms Beats 68.13% of users with Python
# Memory 15.18 MB Beats 45.05% of users with Python

from icecream import ic
def countBattleships(board):
    """
    :type board: List[List[str]]
    :rtype: int
    """

    ll=len(board)
    ll1 = len(board[0])

    n=0
    fl = [[False for j in range(ll1)] for i in range(ll)]
    print(fl)
    print(board); print()
    for i in range(ll):
        for j in range(ll1):
            print(i, 'j=',j, fl, n)
            if not fl[i][j]:
                if board[i][j]=='X':
                    n=n+1
                    fl[i][j]=True
                    nn=j+1
                    while nn<ll1:
                        if board[i][nn]=='X':
                            fl[i][nn] = True
                        else:
                            print('br1')
                            break
                        nn=nn+1
                    nn=i+1

                    while nn<ll:
                        if board[nn][j]=='X':
                            fl[nn][j] = True
                        else:
                            print('br2')
                            break
                        nn=nn+1
        print(i,fl,n); print()
    return n

def tst_cnv():
    def extract(s):
        s=''.join(s).replace('.',' ').strip()
        s=s.split(' ')
        s=[s1 for s1 in s if s1!='']
        if len(s)==1: return 1
        else: return s.count('X')
    s=[".","X",".",".","X","."]
    print(s,'  ',extract(s))
    s=[".","X",".",".",".","."]
    print(s,'  ',extract(s))
    s=[".","X",".",".",".","."]
    print(s,'  ',extract(s))
    s=[".","X","X",".",".","."]
    print(s,'  ',extract(s))
    s=["X",".","X",".","X","."]
    print(s,'  ',extract(s))
    s=["X",".","X",".",".","X","."]
    print(s,'  ',extract(s))

# print(tst_cnv())

# print('res=',countBattleships([["X","X",".","X"],[".",".",".","."],[".",".",".","X"]]))
# print('res=',countBattleships([["X",".",".","X"],["X",".",".","."],[".",".","X","."]]))
# print('res=',countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]))
print('res=',countBattleships([[".",".","."]]))
# print('res=',countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]))
# ic(countBattleships(["X"]))
# ic(countBattleships(["X",".",".","X"]))
# ic(countBattleships([".",".","X","."]))
# ic(countBattleships([".",".",".","X","."]))
# ic(countBattleships([".","X",".","X","."]))
# ic(countBattleships([["."]]))

