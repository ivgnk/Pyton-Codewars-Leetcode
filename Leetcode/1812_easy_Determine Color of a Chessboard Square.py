'''
ReDone 02.09.2024.
1812. Determine Color of a Chessboard Square
https://leetcode.com/problems/determine-color-of-a-chessboard-square/description/

You are given coordinates, a string that represents the coordinates of a square of the chessboard.
Return true if the square is white, and false if the square is black.
The coordinate will always represent a valid chessboard square.
The coordinate will always have the letter first, and the number second.

Example 1:
Input: coordinates = "a1"
Output: false
Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.

Example 2:
Input: coordinates = "h3"
Output: true
Explanation: From the chessboard above, the square with coordinates "h3" is white, so return true.

Example 3:
Input: coordinates = "c7"
Output: false

Constraints:
coordinates.length == 2
'a' <= coordinates[0] <= 'h'
'1' <= coordinates[1] <= '8'

Hint 1
Convert the coordinates to (x, y) - that is, "a1" is (1, 1), "d7" is (4, 7).
Hint 2
Try add the numbers together and look for a pattern.

Hint 1 from 3274. Check if Two Chessboard Squares Have the Same Color
The color of the chessboard is black the sum of row coordinates and column coordinates is even.
Otherwise, it's white.
'''

# Runtime 12 ms Beats 66.40%
# Memory 11.63 MB Beats 65.60%

w={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
def squareIsWhite(coo):
    return (w[coo[0]] + int(coo[1])) %2 == 0

# Runtime 12 ms Beats 66.30% of users with Python
# Memory 11.82 MB Beats 5.52% of users with Python
def squareIsWhite2(coordinates):
    """
    :type coordinates: str
    :rtype: bool
    """
    l1 = [False, True, False, True, False, True, False, True]
    l2 = [True, False, True, False, True, False, True, False]
    n = ord(coordinates[0])-ord('a')
    if int(coordinates[1]) % 2 == 0:
        return l2[n]
    else: return l1[n]

