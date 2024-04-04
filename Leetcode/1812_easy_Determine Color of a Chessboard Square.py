'''
1812. Determine Color of a Chessboard Square
https://leetcode.com/problems/determine-color-of-a-chessboard-square/description/

You are given coordinates, a string that represents the coordinates of a square of the chessboard.
Return true if the square is white, and false if the square is black.
The coordinate will always represent a valid chessboard square.
The coordinate will always have the letter first, and the number second.
'''

# Runtime 12 ms Beats 66.30% of users with Python
# Memory 11.82 MB Beats 5.52% of users with Python

def squareIsWhite(self, coordinates):
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
