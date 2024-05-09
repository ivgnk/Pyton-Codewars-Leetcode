"""
Done 10.05.2024. Topics: Array, Matrix
2639. Find the Width of Columns of a Grid
https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/description/

You are given a 0-indexed m x n integer matrix grid. The width of a column is the maximum length of its integers.
For example, if grid = [[-10], [3], [12]], the width of the only column is 3 since -10 is of length 3.
Return an integer array ans of size n where ans[i] is the width of the ith column.
The length of an integer x with len digits is equal to len if x is non-negative, and len + 1 otherwise.

Example 1:
Input: grid = [[1],[22],[333]]
Output: [3]
Explanation: In the 0th column, 333 is of length 3.

Example 2:
Input: grid = [[-15,1,3],[15,7,12],[5,6,-2]]
Output: [3,1,2]
Explanation:
In the 0th column, only -15 is of length 3.
In the 1st column, all integers are of length 1.
In the 2nd column, both 12 and -2 are of length 2.
"""

# Runtime 87 ms Beats 34.15% of users with Python
# Memory 13.04 MB Beats 60.98% of users with Python
# Runtime 76 ms Beats 87.81% of users with Python
# Memory 12.87 MB Beats 100.00% of users with Python

def findColumnWidth(grid):
    """
    :type grid: List[List[int]]
    :rtype: List[int]
    """
    ll=len(grid)
    lg0=len(grid[0])
    if lg0==1:
        return [max([len(str(d[0])) for d in grid])]
    else:
        res=[0]*lg0
        for i in range(ll):
            for j in range(lg0):
                res[j]=max(len(str(grid[i][j])),res[j])
        return res


# print(findColumnWidth([[1],[22],[333]]))
print(findColumnWidth([[93,-20,-4],[6,-20,-19]]))
# lst=list(range(2))
# print(lst)
