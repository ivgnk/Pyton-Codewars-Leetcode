"""
Done 14.07.2024. Topics: Array, Dynamic Programming
119. Pascal's Triangle II
https://leetcode.com/problems/pascals-triangle-ii/description/

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]
"""

# Runtime 11 ms Beats 80.84%
# Time Complexity O(N**2)
# Memory 11.42 MB Beats 90.13%
# Space Complexity O(N)

def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    if rowIndex == 0: return [1]
    if rowIndex == 1: return [1, 1]
    i = 3;    rows = [[1], [1, 1], [1, 2, 1]]
    n=1
    while i <= rowIndex:
        oldlen = len(rows[i - n])
        lst = []
        lst.append(rows[i - n][0])
        for j in range(1, oldlen):
            lst.append(rows[i - n][j] + rows[i - n][j - 1])
        lst.append(rows[i - n][oldlen - 1])
        rows.append(lst)
        i = i + 1
    return rows[-1]

print(getRow(3))