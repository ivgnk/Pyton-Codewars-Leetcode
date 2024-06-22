"""
Done 22.06.2024. Topics: Array, Sorting
2500. Delete Greatest Value in Each Row
https://leetcode.com/problems/delete-greatest-value-in-each-row/description/

You are given an m x n matrix grid consisting of positive integers.
Perform the following operation until grid becomes empty:

Delete the element with the greatest value from each row.
If multiple such elements exist, delete any of them.
Add the maximum of deleted elements to the answer.
Note that the number of columns decreases by one after each operation.
Return the answer after performing the operations described above.

Example 1:
Input: grid = [[1,2,4],[3,3,1]]
Output: 8
Explanation: The diagram above shows the removed values in each step.
- In the first operation, we remove 4 from the first row and 3 from the second row (notice that, there are two cells with value 3 and we can remove any of them). We add 4 to the answer.
- In the second operation, we remove 2 from the first row and 3 from the second row. We add 3 to the answer.
- In the third operation, we remove 1 from the first row and 1 from the second row. We add 1 to the answer.
The final answer = 4 + 3 + 1 = 8.

Example 2:
Input: grid = [[10]]
Output: 10
Explanation: The diagram above shows the removed values in each step.
- In the first operation, we remove 10 from the first row. We add 10 to the answer.
The final answer = 10.


Hint 1
Iterate from the first to the last row and if there exist some unmarked cells, take a maximum from them and mark that cell as visited.
Hint 2
Add a maximum of newly marked cells to answer and repeat that operation until the whole matrix becomes marked.
"""


# Runtime 79 ms Beats 61.94%
# Memory 11.48 MB Beats 99.35%
# Runtime 74 ms Beats 72.26%
# Memory 11.63 MB Beats 70.97%
def deleteGreatestValue(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    row = len(grid);  res = 0;   rr = range(row)
    while len(grid[0]) > 0:
        res1 = []
        for i in rr:
            mmax = max(grid[i])
            res1.append(mmax)
            grid[i].remove(mmax)
        res = res + max(res1)
    return res


# Runtime 80 ms Beats 58.71%
# Memory 11.64 MB Beats 70.97%
def deleteGreatestValue2(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    row=len(grid); res=0
    while len(grid[0])>0:
        res1=[]
        for i in range(row):
            mmax=max(grid[i])
            res1.append(mmax)
            grid[i].remove(mmax)
        res=res+max(res1)
    return res

print(deleteGreatestValue([[1,2,4],[3,3,1]]))