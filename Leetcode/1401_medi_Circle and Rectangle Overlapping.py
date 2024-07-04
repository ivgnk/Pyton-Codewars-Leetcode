"""
Done 04.07.2024. Topics: Math, Geometry

1401. Circle and Rectangle Overlapping
https://leetcode.com/problems/circle-and-rectangle-overlapping/description/

You are given a circle represented as (radius, xCenter, yCenter) and an axis-aligned rectangle represented
as (x1, y1, x2, y2), where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are
the coordinates of the top-right corner of the rectangle.

Return true if the circle and rectangle are overlapped otherwise return false.
In other words, check if there is any point (xi, yi) that belongs
to the circle and the rectangle at the same time.

Example 1:
Input: radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
Output: true
Explanation: Circle and rectangle share the point (1,0).

Example 2:
Input: radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
Output: false

Example 3:
Input: radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
Output: true

Constraints:
1 <= radius <= 2000

Hint 1
Locate the closest point of the square to the circle, 
you can then find the distance from this point to the center of the circle and check 
if this is less than or equal to the radius.
"""

# Runtime 12 ms Beats 50.00%
# Memory 11.64 MB Beats 50.00%
# Runtime 11 ms Beats 50.00%
# Memory 11.56 MB Beats 83.33%
# Runtime 8 ms Beats 66.67%
# Memory 11.75 MB Beats 50.00%

from icecream import ic
from math import sqrt
def checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2):
    """
    :type radius: int
    :type xCenter: int
    :type yCenter: int
    :type x1: int
    :type y1: int
    :type x2: int
    :type y2: int
    :rtype: bool
    """
    if x1<xCenter<x2 and y1<yCenter<y2: return True
    elif y1 - radius > yCenter: return False
    elif x1 - radius > xCenter: return False
    xcr=(x1+x2)/2
    ycr=(y1+y2)/2
    diag = sqrt((xcr - x2) ** 2 + (ycr - y2) ** 2)
    return sqrt((xcr-xCenter)**2+(ycr-yCenter)**2)<=radius+diag

# ic(checkOverlap(radius = 4, xCenter = 102, yCenter = 50, x1 = 0, y1 = 0, x2 = 100, y2 = 100))
ic(checkOverlap(radius = 1, xCenter = 5, yCenter = -2, x1 = 0, y1 = 0, x2 = 10, y2 = 2))