"""
Done 02.09.2024.
3274. Check if Two Chessboard Squares Have the Same Color
https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/description/

You are given two strings, coordinate1 and coordinate2, representing the coordinates of a square
on an 8 x 8 chessboard.

Return true if these two squares have the same color and false otherwise.

The coordinate will always represent a valid chessboard square.
The coordinate will always have the letter first (indicating its column),
and the number second (indicating its row).

Example 1:
Input: coordinate1 = "a1", coordinate2 = "c3"
Output: true
Explanation:
Both squares are black.

Example 2:
Input: coordinate1 = "a1", coordinate2 = "h3"
Output: false
Explanation:
Square "a1" is black and "h3" is white.


Constraints:
coordinate1.length == coordinate2.length == 2
'a' <= coordinate1[0], coordinate2[0] <= 'h'
'1' <= coordinate1[1], coordinate2[1] <= '8'

Hint 1
The color of the chessboard is black the sum of row coordinates and column coordinates is even.
Otherwise, it's white.

Solution
✏️ Easy Python solution based on hint

Intuition
The color of the chessboard is black the sum of row coordinates and column coordinates is even.
Otherwise, it's white.

# Approach
Use dictionary for convenience
"""

# Runtime 11 ms Beats 100.00%
# Memory 11.75 MB Beats 100.00%
w={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}

def checkTwoChessboards(c1, c2):
    """
    :type coordinate1: str
    :type coordinate2: str
    :rtype: bool
    """
    return (w[c1[0]]+int(c1[1]))%2==(w[c2[0]]+int(c2[1]))%2

print(checkTwoChessboards("a1", "c3"))
print(checkTwoChessboards("a1", "h3"))