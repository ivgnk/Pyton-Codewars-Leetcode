"""
Done 12.05.2024. Topics: Array, Math, Geometry
1037. Valid Boomerang
Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane,
return true if these points are a boomerang.
A boomerang is a set of three points that are all distinct and not in a straight line.

Example 1:
Input: points = [[1,1],[2,3],[3,2]]
Output: true

Example 2:
Input: points = [[1,1],[2,2],[3,3]]
Output: false

Hint 1
3 points form a boomerang if and only if the triangle formed from them has non-zero area.

!!!! s = 1/2*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
s = 1/2*(x0*(y1-y2)+x1*(y2-y0)+x2*(y0-y1))
"""

# Runtime 20 ms Beats 11.84% of users with Python
# Memory 11.62 MB Beats 31.58% of users with Python
# Runtime 14 ms Beats 53.95% of users with Python
# Memory 11.63 MB Beats 31.58% of users with Python

def isBoomerang(points):
    """
    :type points: List[List[int]]
    :rtype: bool
    """
    ll=len(points)
    x =[points[i][0] for i in range(ll)]
    y =[points[i][1] for i in range(ll)]
    return x[0] * (y[1] - y[2]) + x[1] * (y[2] - y[0]) + x[2] * (y[0] - y[1]) != 0

print(isBoomerang([[1,1],[2,3],[3,2]]))