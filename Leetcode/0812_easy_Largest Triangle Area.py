"""
Done 08.05.2024. Topics: Array, Math, Geometry
812. Largest Triangle Area
https://leetcode.com/problems/largest-triangle-area/description/

Given an array of points on the X-Y plane points where points[i] = [xi, yi],
return the area of the largest triangle that can be formed by any three different points.
Answers within 10-5 of the actual answer will be accepted.

Example 1:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000
Explanation: The five points are shown in the above figure. The red triangle is the largest.

Example 2:
Input: points = [[1,0],[0,0],[0,1]]
Output: 0.50000
"""


# Runtime 79 ms Beats 49.35% of users with Python
# Memory 13.57 MB Beats 12.99% of users with Python

from itertools import permutations, combinations
def largestTriangleArea(points):
    """
    :type points: List[List[int]]
    :rtype: float
    """
    comb = tuple(combinations(points,3))
    lst = [abs(d[0][0] * (d[1][1] - d[2][1]) + d[1][0] * (d[2][1] - d[0][1]) + d[2][0] * (d[0][1] - d[1][1]))
           for d in comb]
    return 0.5*max(lst)
    # lst=[]
    # for d in comb:
    #     #  (1/2) * |x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)|
    #     lst.append((0.5)*abs(d[0][0]*(d[1][1]-d[2][1]) + d[1][0]*(d[2][1] - d[0][1]) + d[2][0] * (d[0][1] - d[1][1])))
    # return max(lst)

print(largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))