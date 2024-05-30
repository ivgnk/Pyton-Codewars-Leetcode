"""
Done 30.05.2024. Topics: Array, Greedy, Bit Manipulation, Matrix
861. Score After Flipping Matrix
https://leetcode.com/problems/score-after-flipping-matrix/description/

You are given an m x n binary matrix grid.
A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).
Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.
Return the highest possible score after making any number of moves (including zero moves).

Example 1:
Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

Example 2:
Input: grid = [[0]]
Output: 1


anwendeng Tip
Each row whose first digit is 0, flip it. Ensure it is bigger
Each column whose number for 1's is <=|row|/2, flip it. Ensure more numbers have digit 1 in this
https://leetcode.com/problems/score-after-flipping-matrix/description/comments/2397045
"""

# Runtime 19 ms Beats 69.10% of users with Python
# Memory 11.62 MB Beats# 48.36% of users with Python

def matrixScore(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    ll=len(grid)
    ll1=len(grid[0])
    if ll==1 and ll1==1: return 1
    for i in range(ll):
        if grid[i][0]==0:
            grid[i]=[1 if dat==0 else 0 for dat in grid[i]]

    for i in range(ll1):
        ssum=sum([grid[j][i] for j in range(ll)])
        if ssum<ll-ssum:
            for j in range(ll):
                grid[j][i] = 1 if grid[j][i]==0 else 0

    ssum = 0
    for i in range(ll):
        stri='0b'+''.join([str(grid[i][j]) for j in range(ll1)])
        ssum = ssum+int(stri,2)

    return ssum

print(matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))
