"""
Done 05.06.2024. Topics: Array, Sorting
378. Kth Smallest Element in a Sorted Matrix
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

Given an n x n matrix where each of the rows and columns is sorted in ascending order,
return the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.
You must find a solution with a memory complexity better than O(n2).

Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5
"""

# Runtime 145 ms Beats 67.26% of users with Python3
# Memory 21.44 MB Beats 12.38% of users with Python3
def kthSmallest(matrix, k):
    return sorted([a for lin in matrix for a in lin])[k - 1]

# -------------------------------
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/comments/1806931
# https://leetcode.com/u/Unnatimishra_123/
# Runtime 135 ms Beats 88.12% of users with Python3
# Memory 21.17 MB Beats 63.66% of users with Python3

import bisect
def kthSmallest2(matrix, k):
    n=len(matrix)
    l=float('inf')
    r=float('-inf')

    for i in range(n):
        l=min(l,matrix[i][0])
        r=max(r,matrix[i][n-1])


    while l < r:
        mid = (l + (r - l) //2)
        x=0
        for i in range(n):
            up=bisect.bisect_right(matrix[i],mid)
            x+=up

        if x < k:
            l = mid + 1
        else:
            r = mid
    return l