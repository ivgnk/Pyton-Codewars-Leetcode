"""
Done 27.05.2024. Topics: Array, Sorting
1637. Widest Vertical Area Between Two Points Containing No Points

Given n points on a 2D plane where points[i] = [xi, yi],
Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height).
The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.

Example 1:
Input: points = [[8,7],[9,9],[7,4],[9,7]]
Output: 1
Explanation: Both the red and the blue area are optimal.

Example 2:
Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
Output: 3

Hint 1
Try sorting the points
Hint 2
Think is the y-axis of a point relevant
"""

# Runtime 613 ms Beats 74.46% of users with Python
# Memory 57.69 MB Beats 99.03% of users with Python

def maxWidthOfVerticalArea(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    ll = len(points)
    p = sorted(points[i][0] for i in range(ll))
    return max([p[i] - p[i - 1] for i in range(1, ll)])


# Runtime 669 ms Beats 41.71% of users with Python
# Memory 57.81 MB Beats 79.14% of users with Python
# Runtime 663 ms Beats 43.47% of users with Python
# Memory 57.87 MB Beats 79.14% of users with Python

def maxWidthOfVerticalArea2(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    p=sorted(points); ll=len(points)
    return max([p[i][0]-p[i-1][0] for i in range(1,ll)])


