"""
Done 04.07.2024. Topics: Array, Math, Geometry, Sorting, Matrix

1030. Matrix Cells in Distance Order
You are given four integers row, cols, rCenter, and cCenter.
There is a rows x cols matrix and you are on the cell with the coordinates (rCenter, cCenter).

Return the coordinates of all cells in the matrix, sorted by their distance from
(rCenter, cCenter) from the smallest distance to the largest distance.
You may return the answer in any order that satisfies this condition.

The distance between two cells (r1, c1) and (r2, c2) is |r1 - r2| + |c1 - c2|.

Example 1:
Input: rows = 1, cols = 2, rCenter = 0, cCenter = 0
Output: [[0,0],[0,1]]
Explanation: The distances from (0, 0) to other cells are: [0,1]

Example 2:
Input: rows = 2, cols = 2, rCenter = 0, cCenter = 1
Output: [[0,1],[0,0],[1,1],[1,0]]
Explanation: The distances from (0, 1) to other cells are: [0,1,1,2]
The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.

Example 3:
Input: rows = 2, cols = 3, rCenter = 1, cCenter = 2
Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
Explanation: The distances from (1, 2) to other cells are: [0,1,1,2,2,3]
There are other answers that would also be accepted as correct, such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].

Constraints:

1 <= rows, cols <= 100
0 <= rCenter < rows
0 <= cCenter < cols
"""


# Runtime 118 ms Beats 25.81%
# Memory 15.80 MB Beats 11.29%
# Runtime 114 ms Beats 33.87%
# Memory 15.76 MB Beats 11.29%
def allCellsDistOrder3(rows, cols, rCenter, cCenter):
    """
    :type rows: int
    :type cols: int
    :type rCenter: int
    :type cCenter: int
    :rtype: List[List[int]]
    """
    lst=list()
    for i in range(rows):
        for j in range(cols):
            r = abs(i - rCenter) + abs(j - cCenter)
            lst.append([r, [i, j]])
    lst=sorted(lst)
    return [lst[i][1] for i in range(len(lst))]

# Runtime 112 ms Beats 37.10%
# Memory 15.78 MB Beats 11.29%
def allCellsDistOrder2(rows, cols, rCenter, cCenter):
    """
    :type rows: int
    :type cols: int
    :type rCenter: int
    :type cCenter: int
    :rtype: List[List[int]]
    """
    lst=list()
    for i in range(rows):
        for j in range(cols):
            lst.append([abs(i - rCenter) + abs(j - cCenter), [i, j]])
    lst=sorted(lst)
    return [lst[i][1] for i in range(len(lst))]


# Runtime 109 ms Beats 40.32%
# Memory 15.70 MB Beats 11.29%
# Runtime 96 ms Beats 82.26%
# Memory 15.81 MB Beats 11.29%
def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
    """
    :type rows: int
    :type cols: int
    :type rCenter: int
    :type cCenter: int
    :rtype: List[List[int]]
    """

    lst = [[abs(i - rCenter) + abs(j - cCenter), [i, j]] for i in range(rows) for j in range(cols)]
    lst.sort()
    return [lst[i][1] for i in range(len(lst))]

print(allCellsDistOrder(rows = 1, cols = 2, rCenter = 0, cCenter = 0))

