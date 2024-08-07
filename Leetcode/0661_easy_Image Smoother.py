"""
07.08.2024. Topics: Array, Matrix
661. Image Smoother
https://leetcode.com/problems/image-smoother/description/

An image smoother is a filter of the size 3 x 3 that can be applied to each cell
of an image by rounding down the average of the cell and the eight surrounding cells
(i.e., the average of the nine cells in the blue smoother).
If one or more of the surrounding cells of a cell is not present,
we do not consider it in the average (i.e., the average of the four cells in the red smoother).

Given an m x n integer matrix img representing the grayscale of an image,
return the image after applying the smoother on each cell of it.

Example 1:
Input: img = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[0,0,0],[0,0,0],[0,0,0]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0

Example 2:
Input: img = [[100,200,100],[200,50,200],[100,200,100]]
Output: [[137,141,137],[141,138,141],[137,141,137]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138

Constraints:
m == img.length
n == img[i].length
1 <= m, n <= 200
0 <= img[i][j] <= 255
"""

# on the base of
# https://leetcode.com/problems/image-smoother/solutions/4424122/python-easy/

# Runtime 353 ms Beats 85.26%
# Memory 17.36 MB Beats 21.92%

from icecream import ic
from math import floor
def imageSmoother(img):
    """
    :type img: List[List[int]]
    :rtype: List[List[int]]
    """
    ind=[-1,0,1]
    ll= len(img)
    ll1=len(img[0])
    res = [[0] * ll1 for _ in range(ll)]
    for i in range(ll): # ll
        for j in range(ll1): # ll1
            ss=0
            nn=0
            for x in ind:
                for y in ind:
                    a=i+x
                    b=j+y
                    if a<0 or b<0 or a>=ll or b>=ll1:
                        continue
                    ss += img[a][b]
                    nn += 1
            res[i][j]=floor(ss/nn)
    return res


def imageSmoother2(img):
    move_horizontal_vertical = [-1, 0, 1]
    m = len(img)
    n = len(img[0])
    res = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            cnt = 0
            val = 0
            for a in move_horizontal_vertical:
                for b in move_horizontal_vertical:
                    x = i + a
                    y = j + b
                    if x < 0 or x >= m or y < 0 or y >= n:
                        continue
                    cnt += 1
                    val += img[x][y]
            res[i][j] = val // cnt
    return res


ic(imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))
ic(imageSmoother([[100,200,100],[200,50,200],[100,200,100]]))
ic('--------------')
ic(imageSmoother2([[100,200,100],[200,50,200],[100,200,100]]))
ic([[137,141,137],[141,138,141],[137,141,137]])

# Input: img =
# Output: [[137,141,137],[141,138,141],[137,141,137]]
