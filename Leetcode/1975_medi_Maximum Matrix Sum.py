"""
Done 24.11.2024. Topics: Matrix
1975. Maximum Matrix Sum
https://leetcode.com/problems/maximum-matrix-sum/

ou are given an n x n integer matrix. You can do the following operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements.
Return the maximum sum of the matrix's elements using the operation mentioned above.

Example 1:
Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.

Example 2:
Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Explanation: We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.

Constraints:
n == matrix.length == matrix[i].length
2 <= n <= 250
-105 <= matrix[i][j] <= 105

Hint 1
Try to use the operation so that each row has only one negative number.
Hint 2
If you have only one negative element you cannot convert it to positive.

My solution https://leetcode.com/problems/maximum-matrix-sum/solutions/6079572/easy-python-solution-for-problem-1975-based-on-1-5-hints-and-common-mathematical-sense/
✏️ Easy Python solution for Problem 1975 based on 1.5 hints and common mathematical sense

Intuition
- If there are an even number of negative numbers, then the matrix can be made non-negative.
- If there are an odd number of negative numbers, then there will be one negative number in the matrix.
--This negative number must be the smallest modulo.
"""

# Wrong Answer - 81 / 98 testcases passed
# Input matrix = [[2,9,3],[5,4,-4],[1,7,1]]
# Output 28
# Expected 34
def maxMatrixSum2(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    ll = len(matrix);  rll = range(ll)
    sp, sn = 0, 0
    nn = 0;   maxn = -10 ** 6
    for i in rll:
        for j in rll:
            if matrix[i][j] > 0:
                sp += matrix[i][j]
            else:
                sn += matrix[i][j]
                nn += 1
                if matrix[i][j] > maxn:
                    maxn = matrix[i][j]
    if nn % 2 == 0:
        return sp - sn
    else:
        sn -= maxn
        return sp - sn + maxn

# Runtime 71 ms Beats 82.35%
# Memory 17.69 MB Beats 70.83%
# Runtime 65 ms Beats 100.00%
# Memory 17.84 MB Beats 33.33%
# Time Complexity O(N**2)
# Space Complexity O(1)
def maxMatrixSum(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    ll=len(matrix); rll=range(ll)
    summ = 0; minabs = float('inf')
    nn=0
    for i in rll:
        for j in rll:
            if matrix[i][j]>0:
                dat=matrix[i][j]
            else:
                dat =abs(matrix[i][j])
                nn+=1
            summ+=dat
            if dat<minabs: minabs=dat
    if nn%2==0:
        return summ
    else:
        return summ - 2*minabs

print(maxMatrixSum([[1,-1],[-1,1]]))
print(maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]]))
print(maxMatrixSum([[2,9,3],[5,4,-4],[1,7,1]]))

