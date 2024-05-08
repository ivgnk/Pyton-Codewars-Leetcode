"""
Done 08.05.2024. Topics: Array, Math, Divide and Conquer, Geometry, Sorting, Heap (Priority Queue), Quickselect
973. K Closest Points to Origin
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane
is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order.
The answer is guaranteed to be unique (except for the order that it is in).

Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
"""

# Runtime 574 ms Beats 65.99% of users with Python
# Memory 17.48 MB Beats 97.50% of users with Python
# Runtime 553 ms Beats 83.55% of users with Python
# Memory 17.57 MB Beats 94.71% of users with Python

def kClosest(points, k):
    """
    :type points: List[List[int]]
    :type k: int
    :rtype: List[List[int]]
    """
    lst = [[d[0]**2+d[1]**2,d] for d in points]
    lst = sorted(lst)
    return [lst[i][1] for i in range(k)]

print(kClosest(points = [[1,3],[-2,2]], k = 1))