"""
Done 04.06.2024. Topics: Array, Binary Search, Sorting, Heap (Priority Queue)

Matrix
1337. The K Weakest Rows in a Matrix
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/

You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians).
The soldiers are positioned in front of the civilians.
That is, all the 1's will appear to the left of all the 0's in each row.
A row i is weaker than a row j if one of the following is true:
The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

Example 1:
Input: mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3

Output: [2,0,3]
Explanation:
The number of soldiers in each row is:
- Row 0: 2
- Row 1: 4
- Row 2: 1
- Row 3: 2
- Row 4: 5
The rows ordered from weakest to strongest are [2,0,3,1,4].

Example 2:
Input: mat =
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],
k = 2
Output: [0,2]
Explanation:
The number of soldiers in each row is:
- Row 0: 1
- Row 1: 4
- Row 2: 1
- Row 3: 1
The rows ordered from weakest to strongest are [0,2,3,1].
"""

# Runtime 75 ms Beats 66.67% of users with Python
# Memory 11.87 MB Beats 80.89% of users with Python
# Runtime 59 ms Beats 100.00% of users with Python
# Memory 12.00 MB Beats 46.34% of users with Python

def kWeakestRows(mat, k):
    """
    :type mat: List[List[int]]
    :type k: int
    :rtype: List[int]
    """
    ll=len(mat)
    ind = [(sum(mat[i]),i) for i in range(ll)]
    ind = sorted(ind)
    return [dat[1] for dat in ind][:k]

print(kWeakestRows(mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], k = 3))

