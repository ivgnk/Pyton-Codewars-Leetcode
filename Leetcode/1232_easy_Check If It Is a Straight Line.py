'''
1232. Check If It Is a Straight Line
https://leetcode.com/problems/check-if-it-is-a-straight-line/description/

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
Check if these points make a straight line in the XY plane.

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Hint 1 - If there're only 2 points, return true.
Hint 2 - Check if all other points lie on the line defined by the first 2 points.
'''

# Runtime 35 ms Beats 83.01% of users with Python
# Memory 12.04 MB Beats 81.05% of users with Python

import matplotlib.pyplot as plt
def checkStraightLine(coo):
    """
    :type coordinates: List[List[int]]
    :rtype: bool
    """
    x=[]; y=[]
    for i in range(len(coo)):
        x.append(coo[i][0])
        y.append(coo[i][1])
    plt.plot(x,y); plt.grid(); plt.show()


    lc= len(coo)
    if lc < 2: return False
    if lc == 2: return True

    ssumx = sum([1 for i in range(1,lc) if coo[i][0]==coo[i-1][0]])
    if ssumx+1==lc: return True
    ssumx = sum([1 for i in range(1,lc) if coo[i][1]==coo[i-1][1]])
    if ssumx+1==lc: return True

    top = coo[1][1] - coo[0][1]
    bot = coo[1][0] - coo[0][0]
    if bot==0: return False
    k = top / bot

    for i in range(1,lc):
        bot = coo[i][0] - coo[i-1][0]
        if bot == 0: return False
        k2 = (coo[i][1] - coo[i-1][1]) / bot
        if abs(k2-k)> 1e-10:
            return False
    return True

# print(checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
# print(checkStraightLine([[0,0],[0,1],[0,-1]]))
print(checkStraightLine([[1,1],[2,2],[2,0]]))