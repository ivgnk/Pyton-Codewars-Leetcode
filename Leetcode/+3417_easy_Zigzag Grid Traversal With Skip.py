"""
13.01.2025
3417. Zigzag Grid Traversal With Skip
https://leetcode.com/problems/zigzag-grid-traversal-with-skip/description/

You are given an m x n 2D array grid of positive integers.
Your task is to traverse grid in a zigzag pattern while skipping every alternate cell.
Zigzag pattern traversal is defined as following the below actions:
Start at the top-left cell (0, 0).
Move right within a row until the end of the row is reached.
Drop down to the next row, then traverse left until the beginning of the row is reached.
Continue alternating between right and left traversal until every row has been traversed.
Note that you must skip every alternate cell during the traversal.

Return an array of integers result containing, in order, the value of the cells visited during the zigzag traversal with skips.

Example 1:
Input: grid = [[1,2],[3,4]]
Output: [1,4]

Example 2:
Input: grid = [[2,1],[2,1],[2,1]]
Output: [2,1,2]

Example 3:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,3,5,7,9]

Constraints:

2 <= n == grid.length <= 50
2 <= m == grid[i].length <= 50
1 <= grid[i][j] <= 2500
"""
from typing import List


# Wrong Answer - 342 / 840 testcases passed
def zigzagTraversal(grid):
    """
    :type grid: List[List[int]]
    :rtype: List[int]
    """
    return[grid[i][j] for i in range(len(grid)) for j in range(len(grid[0])) if  (i + j) % 2 == 0]

print(zigzagTraversal(grid = [[1,2],[3,4]]))
print(zigzagTraversal(grid = [[2,1],[2,1],[2,1]]))
print(zigzagTraversal(grid = [[1,2,3],[4,5,6],[7,8,9]]))

# https://leetcode.com/problems/zigzag-grid-traversal-with-skip/solutions/6267315/python-code-by-gopigaurav-wlh9/
# Runtime 4 ms Beats 100.00%
# Memory 18.39 MB Beats 100.00%
class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        res = []
        rows = len(grid)

        if rows == 0:
            return []
        cols = len(grid[0])

        for i in range(rows):
            if i % 2 == 0:
                for j in range(cols):
                    if (i + j) % 2 == 0:  # diagonal numbers
                        res.append(grid[i][j])
            else:
                for j in range(cols - 1, -1, -1):
                    if (i + j) % 2 == 0:
                        res.append(grid[i][j])
        return res


# https://leetcode.com/problems/zigzag-grid-traversal-with-skip/solutions/6267320/easy-solution-in-python-by-jarizaga-htwh/
class Solution2:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:

        # Transform the grid into a list
        grid_list = []
        for i, l in enumerate(grid):
            if i % 2 == 0:
                grid_list.extend(l)
            else:
                grid_list.extend(l[::-1])

        # Go over the new list, appending only alternate elements
        final_list = []
        for i, elem in enumerate(grid_list):
            if i % 2 == 0:
                final_list.append(elem)

        return final_list

