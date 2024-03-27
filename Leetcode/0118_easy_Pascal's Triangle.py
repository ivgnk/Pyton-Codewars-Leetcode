'''
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
'''
import sys

# Runtime 10 ms Beats 93.35% of users with Python
# Memory 11.58 MB Beats 78.39% of users with Python

def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 1: return [[1]]
    if numRows == 2: return [[1], [1, 1]]
    i = 3;    rows = [[1], [1, 1]]
    while i <= numRows:
        oldlen = len(rows[i-2])
        lst=[]
        lst.append(rows[i-2][0])
        for j in range(1,oldlen):
            lst.append(rows[i-2][j]+rows[i-2][j-1])
        lst.append(rows[i-2][oldlen-1])
        rows.append(lst)
        i=i+1
    return rows

print(generate(3))