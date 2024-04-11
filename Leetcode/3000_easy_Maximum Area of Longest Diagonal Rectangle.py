"""
3000. Maximum Area of Longest Diagonal Rectangle
https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/description/

You are given a 2D 0-indexed integer array dimensions.
For all indices i, 0 <= i < dimensions.length,
dimensions[i][0] represents the length and
dimensions[i][1] represents the width of the rectangle i.

Return the area of the rectangle having the longest diagonal.
If there are multiple rectangles with the longest diagonal,
return the area of the rectangle having the maximum area.

Example 1:
Input: dimensions = [[9,3],[8,6]]
Output: 48
Explanation:
For index = 0, length = 9 and width = 3. Diagonal length = sqrt(9 * 9 + 3 * 3) = sqrt(90) ≈ 9.487.
For index = 1, length = 8 and width = 6. Diagonal length = sqrt(8 * 8 + 6 * 6) = sqrt(100) = 10.
So, the rectangle at index 1 has a greater diagonal length therefore we return area = 8 * 6 = 48.

Example 2:
Input: dimensions = [[3,4],[4,3]]
Output: 12
Explanation: Length of diagonal is the same for both which is 5, so maximum area = 12.
"""

# Runtime 51 ms Beats 66.30% of users with Python
# Memory 11.50 MB Beats 96.74% of users with Python

import math
from math import hypot
def areaOfMaxDiagonal(dimensions):
    """
    :type dimensions: List[List[int]]
    :rtype: int
    """
    mh=-1.0; area=0
    for i in range(len(dimensions)):
        print(i,dimensions[i][0]*dimensions[i][1])
        diag=math.hypot(dimensions[i][0],dimensions[i][1])
        if diag>=mh:
            if diag>mh:
                mh=diag
                area=dimensions[i][0]*dimensions[i][1]
            else:
                area1=dimensions[i][0]*dimensions[i][1]
                area=max(area,area1)
    return area

dat=[[4,7],[8,9],[5,3],[6,10],[2,9],[3,10],[2,2],[5,8],[5,10],[5,6],[8,9],
     [10,7],[8,9],[3,7],[2,6],[5,1],[7,4],[1,10],[1,7],[6,9],[3,3],[4,6],
     [8,2],[10,6],[7,9],[9,2],[1,2],[3,8],[10,2],[4,1],[9,7],[10,3],[6,9],
     [9,8],[7,7],[5,7],[5,4],[6,5],[1,8],[2,3],[7,10],[3,9],[5,7],[2,4],[5,6],
     [9,5],[8,8],[8,10],[6,8],[5,1],[10,8],[7,4],[2,1],[2,7],[10,3],[2,5],[7,6],
     [10,5],[10,9],[5,7],[10,6],[4,3],[10,4],[1,5],[8,9],[3,1],[2,5],[9,10],[6,6],
     [5,10],[10,2],[6,10],[1,1],[8,6],[1,7],[6,3],[9,3],[1,4],[1,1],[10,4],[7,9],
     [4,5],[2,8],[7,9],[7,3],[4,9],[2,8],[4,6],[9,1],[8,4],[2,4],[7,8],[3,5],[7,6],
     [8,6],[4,7],[25,60],[39,52],[16,63],[33,56]]
print(areaOfMaxDiagonal(dat))