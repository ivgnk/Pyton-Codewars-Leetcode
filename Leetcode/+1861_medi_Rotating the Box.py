"""
23.11.2024. Topics: Matrix
1861. Rotating the Box
https://leetcode.com/problems/rotating-the-box/editorial

You are given an m x n matrix of characters box representing a side-view of a box.
Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity.
Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box.
Gravity does not affect the obstacles' positions, and the inertia from the box's rotation
does not affect the stones' horizontal positions.

It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.

Example 1:
Input: box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]

Example 2:
Input: box = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]

Example 3:
Input: box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]

Constraints:
m == box.length
n == box[i].length
1 <= m, n <= 500
box[i][j] is either '#', '*', or '.'.

Hint 1
Rotate the box using the relation rotatedBox[i][j] = box[m - 1 - j][i].
Hint 2
Start iterating from the bottom of the box and
for each empty cell check if there is any stone above it with no obstacles between them.
"""


from collections import deque
from typing import List


def rotateTheBox(box):
    """
    :type box: List[List[str]]
    :rtype: List[List[str]]
    """


    row=len(box); col=len(box[0])
    newm=[[' ']*row for i in range(col)]
    rown, coln= col, row
    for i in range(rown):
        for j in range(coln):
            newm[i][j]=box[row - 1 - j][i]
    print(box)
    print(newm)
    for i in range(coln):
        for i in range(rown,-1,-1):
            if newm[i][j]=='.':
                # i1,j1 =
                pass

# print(rotateTheBox([["#",".","#"]]))

# Runtime 1834 ms Beats 50.00%
# Memory 66.88 MB Beats 62.00%
# https://leetcode.com/problems/rotating-the-box/solutions/6074650/python-solution-with-deque/
class Solution1:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m , n = len(box) , len(box[0])
        for row in box:
            space = deque()
            for i in range(len(row) - 1 , -1 , -1):
                if row[i] == '.':
                    space.append(i)
                elif row[i] == '#' and space:
                    ind = space.popleft()
                    row[ind] = '#'
                    row[i] = '.'
                    space.append(i)
                else:
                    space = deque()


        rotated_box = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                rotated_box[i][j] = box[m-1-j][i]
        return rotated_box

s=Solution1()
print(s.rotateTheBox([["#",".","#"]]))

