"""
Done 11.08.2024
3248. Snake in Matrix
https://leetcode.com/problems/snake-in-matrix/description/

There is a snake in an n x n matrix grid and can move in four possible directions.
Each cell in the grid is identified by the position: grid[i][j] = (i * n) + j.

The snake starts at cell 0 and follows a sequence of commands.
You are given an integer n representing the size of the grid and an array of strings commands
where each command[i] is either "UP", "RIGHT", "DOWN", and "LEFT".
It's guaranteed that the snake will remain within the grid boundaries throughout its movement.
Return the position of the final cell where the snake ends up after executing commands.

Example 1:
Input: n = 2, commands = ["RIGHT","DOWN"]
Output: 3

Example 2:
Input: n = 3, commands = ["DOWN","RIGHT","UP"]
Output: 1

Constraints:

2 <= n <= 10
1 <= commands.length <= 100
commands consists only of "UP", "RIGHT", "DOWN", and "LEFT".
The input is generated such the snake will not move outside of the boundaries.

Hint 1
Try to update the row and column of the snake after each command.
"""

# Runtime 35 ms Beats 100.00%
# Time Complexity: O(N)
# Memory 11.73 MB Beats 100.00%
# Space Complexity O(1)


def finalPositionOfSnake(n, commands):
    """
    :type n: int
    :type commands: List[str]
    :rtype: int
    """
    row=col=0
    for k in range(n):
        if commands[k]=="UP": row -= 1
        elif commands[k]=="RIGHT": col += 1
        elif commands[k] =="DOWN": row += 1
        else: col -= 1
    return (row * n) + col

