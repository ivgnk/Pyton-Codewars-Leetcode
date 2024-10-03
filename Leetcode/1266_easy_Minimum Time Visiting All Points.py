"""
Done 03.10.2024. Topics: Math, Geometry
1266. Minimum Time Visiting All Points
https://leetcode.com/problems/minimum-time-visiting-all-points/description/

On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi].
Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:
In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.

Example 1:
Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]
Time from [1,1] to [3,4] = 3 seconds
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds

Example 2:
Input: points = [[3,2],[-2,2]]
Output: 5

Constraints:
points.length == n
1 <= n <= 100
points[i].length == 2
-1000 <= points[i][0], points[i][1] <= 1000

Hint 1
To walk from point A to point B there will be an optimal strategy to walk ?
Hint 2
Advance in diagonal as possible then after that go in straight line.
Hint 3
Repeat the process until visiting all the points.

My solution
https://leetcode.com/problems/minimum-time-visiting-all-points/solutions/5864643/single-line-python-solution-based-on-hint-2/
✏️ Single-line Python solution based on hint 2
# Intuition
"Hint 2: Advance in diagonal as possible then after that go in straight line"
Therefore, the task is reduced to integer calculations without calculating hypotenuses.

# Approach
Calculate the distance modules between pairs of points along the axes.
Then select the largest for each pair
"""

from icecream import ic

# Runtime 61 ms Beats 38.70%
# Memory 16.80 MB Beats 12.22%
# Runtime 56 ms Beats 71.39%
# Memory 16.61 MB Beats 12.22%
def minTimeToVisitAllPoints2(p):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    ll = len(p);  ssum = 0
    for i in range(1, ll):
        a = p[i][0] - p[i - 1][0]
        b = p[i][1] - p[i - 1][1]
        zv = max(abs(a), abs(b))
        ssum += zv
    return ssum

# Runtime 53 ms Beats 85.94%
# Memory 16.59 MB Beats 54.61%
def minTimeToVisitAllPoints(p):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    return sum(max(abs(p[i][0] - p[i - 1][0]), abs(p[i][1] - p[i - 1][1]))
                                                for i in range(1, len(p)))

# print(minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
# print(minTimeToVisitAllPoints( [[3,2],[-2,2]]))
ic(minTimeToVisitAllPoints([[559,511],[932,618],[-623,-443],[431,91],[838,-127],[773,-917],[-500,-910],[830,-417],[-870,73],
       [-864,-600],[450,535],[-479,-370],[856,573],[-549,369],[529,-462],[-839,-856],[-515,-447],[652,197],
       [-83,345],[-69,423],[310,-737],[78,-201],[443,958],[-311,988],[-477,30],[-376,-153],[-272,451],
       [322,-125],[-114,-214],[495,33],[371,-533],[-393,-224],[-405,-633],[-693,297],[504,210],[-427,-231],
       [315,27],[991,322],[811,-746],[252,373],[-737,-867],[-137,130],[507,380],[100,-638],[-296,700],[341,671],
       [-944,982],[937,-440],[40,-929],[-334,60],[-722,-92],[-35,-852],[25,-495],[185,671],[149,-452]]))
