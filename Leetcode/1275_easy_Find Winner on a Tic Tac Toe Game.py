"""
Done 06.09.2024. Topics: Array, Matrix
1275. Find Winner on a Tic Tac Toe Game
https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game

Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:
Players take turns placing characters into empty squares ' '.
The first player A always places 'X' characters, while the second player B always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never on filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

Example 1:
Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: A wins, they always play first.

Example 2:
Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: B wins.

Example 3:
Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.

Constraints:
1 <= moves.length <= 9
moves[i].length == 2
0 <= rowi, coli <= 2
There are no repeated elements on moves.
moves follow the rules of tic tac toe.

Hint 1
It's straightforward to check if A or B won or not,
check for each row/column/diag if all the three are the same.
Hint 2
Then if no one wins, the game is a draw iff the board is full,
i.e. moves.length = 9 otherwise is pending.

✏️ A smart and lazy decision with numpy, but not a quick
Intuition
Why use clever tricks that won't be useful anywhere.
It is better to upgrade your numpy skills, which gives you all the functions to solve the problem.

Approach
1) np.full - filling the matrix with values so that numpy summation functions work
2) Line selection is the same as with lists
3) tbl.diagonal() - selection the main diagonal
3) np.fliplr(tbl).diagonal(0) - selection the additional diagonal
fliplr - flips the entries in each row in the left/right direction
"""

# Runtime 42 ms Beats 8.33%
# Memory 23.20 MB Beats 14.58%
import numpy as np
def tictactoe(moves):
    """
    :type moves: List[List[int]]
    :rtype: str
    """
    r3=range(3)
    tbl=np.full((3, 3), -10)
    for i in range(len(moves)):
        r,c=moves[i]
        if i%2==0:
            tbl[r][c]=1
        else:
            tbl[r][c]=0

    # print(tbl)
    # row control
    for s in tbl:
        ssum=np.sum(s)
        if ssum==3: return "A"
        elif ssum==0: return "B"
    # col control
    for i in r3:
        ssum = np.sum(tbl[:,i])
        if ssum==3: return "A"
        elif ssum==0: return "B"
    # main diagonal
    ssum = np.sum(tbl.diagonal())
    if ssum == 3: return "A"
    elif ssum == 0: return "B"
    # second diagonal
    # stackoverflow.com/questions/20164685/reverse-diagonal-on-numpy-python
    rev_diag=np.fliplr(tbl).diagonal(0)
    ssum = np.sum(rev_diag)
    if ssum == 3: return "A"
    elif ssum == 0: return "B"
    if len(moves)==9: return "Draw"
    else: return "Pending"

print(tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]),'\n') # A
print(tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]),'\n') # B
print(tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]),'\n') # Draw
print(tictactoe([[0,0],[1,1]])) # "Pending"