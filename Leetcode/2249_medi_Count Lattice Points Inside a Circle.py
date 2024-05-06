"""
Done 06.05.2024
2249. Count Lattice Points Inside a Circle
https://leetcode.com/problems/count-lattice-points-inside-a-circle/description/

Given a 2D integer array circles where circles[i] = [xi, yi, ri] represents the center (xi, yi) and radius ri of the ith circle drawn on a grid, return the number of lattice points that are present inside at least one circle.

Note:
A lattice point is a point with integer coordinates.
Points that lie on the circumference of a circle are also considered to be inside it.

Example 1:
Input: circles = [[2,2,1]]
Output: 5
Explanation:
The figure above shows the given circle.
The lattice points present inside the circle are (1, 2), (2, 1), (2, 2), (2, 3), and (3, 2) and are shown in green.
Other points such as (1, 1) and (1, 3), which are shown in red, are not considered inside the circle.
Hence, the number of lattice points present inside at least one circle is 5.

Example 2:
Input: circles = [[2,2,2],[3,4,1]]
Output: 16
Explanation:
The figure above shows the given circles.
There are exactly 16 lattice points which are present inside at least one circle.
Some of them are (0, 2), (2, 0), (2, 4), (3, 2), and (4, 4).
"""

# Runtime 1366 ms Beats 100.00% of users with Python
# Memory 16.66 MB Beats 42.86% of users with Python

def countLatticePoints(circles):
    """
    :type circles: List[List[int]]
    :rtype: int
    """
    ss = set()
    for c in circles:
        x_c=c[0]; y_c=c[1]; r2=c[2]**2
        for x in range(x_c-c[2],x_c+c[2]+1):
            for y in range(c[1]-c[2], c[1] + c[2] + 1):
                if (x - x_c)** 2 + (y - y_c)**2 <= r2:
                    ss.add((x,y))
    return len(ss)

print(countLatticePoints(circles = [[2,2,2],[3,4,1]]))

