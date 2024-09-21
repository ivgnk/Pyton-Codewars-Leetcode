"""
21.09.2024. Topics: Math, Geometry
836. Rectangle Overlap
https://leetcode.com/problems/rectangle-overlap/description/

An axis-aligned rectangle is represented as a list [x1, y1, x2, y2],
where (x1, y1) is the coordinate of its bottom-left corner,
and (x2, y2) is the coordinate of its top-right corner.
Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is positive.
To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.

Example 1:
Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true

Example 2:
Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false

Example 3:
Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
Output: false

Constraints:
rec1.length == 4
rec2.length == 4
-109 <= rec1[i], rec2[i] <= 109
rec1 and rec2 represent a valid rectangle with a non-zero area.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from icecream import ic
# Wrong Answer - 30 / 40 testcases passed
# rec1 = [5,15,8,18]
# rec2 = [0,3,7,9]
# Output - true
# Expected - false
def isRectangleOverlap2(r1, r2):
    """
    :type rec1: List[int]
    :type rec2: List[int]
    :rtype: bool
    """
    return (r2[0] - r1[2]) < 0 and (r2[1] - r1[3]) < 0

# [x1, y1, x2, y2]
# (x1, y1) is the coordinate of its bottom-left corner,
# (x2, y2) is the coordinate of its top-right corner.


def plt_rect(r1,r2):
    fig, ax = plt.subplots()
    ax.plot([-10, -10], [10, 10])
    ax.add_patch(Rectangle((r1[0], r1[1]), r1[2]-r1[0], r1[3]-r1[1], edgecolor='b', facecolor='b',alpha=0.5))
    ax.add_patch(Rectangle((r2[0], r2[1]), r2[2]-r2[0], r2[3]-r2[1], edgecolor='r', facecolor='r',alpha=0.5))
    plt.show()

def sgn(x):
    return (x > 0) - (x < 0)

# Wrong Answer - 36 / 40 testcases passed
# rec1 = [-9,6,-3,10]
# rec2 = [-8,-10,-5,-4]
# Output true
# Expected false

# Wrong Answer - 33 / 40 testcases passed
# rec1 = [-7,-3,10,5]
# rec2 = [-6,-5,5,10]
# Output false
# Expected true
def isRectangleOverlap6(r1, r2):
    if r1 > r2: r1, r2 = r2, r1
    ic(r1,r2)
    x1bl,y1bl,x1tr,y1tr=r1
    x2bl,y2bl,x2tr,y2tr=r2
    if (x2bl - x1tr)<0:
        if (y2bl - y1tr) < 0:
            res= sgn(y2bl)==sgn(y1tr)
        else: return False
    else: return False
    ic(res)
    plt_rect(r1,r2)
    return res

# Runtime 13 ms Beats 58.60%
# Memory 11.63 MB Beats 27.44%
# https://leetcode.com/problems/rectangle-overlap/solutions/5803521/fck-i-totally-can-t-do-it-if-i-do-it-with-myself/
def isRectangleOverlap(r1, r2):
    x1bl,y1bl,x1tr,y1tr=r1
    x2bl,y2bl,x2tr,y2tr=r2

    # Check for no horizontal overlap
    if x1tr <= x2bl or x2tr <= x1bl:
        return False
    # Check for no vertical overlap
    if y1tr <= y2bl or y2tr <= y1bl:
        return False

    # If neither no-overlap condition is met, the rectangles intersect
    return True

# ic(isRectangleOverlap([-9,6,-3,10],[-8,-10,-5,-4])) # False
ic(isRectangleOverlap([-7,-3,10,5],[-6,-5,5,10]))
# ic(sgn(-0))
# ic(sgn(10))
# ic(sgn(-10))
