"""
Done 03.05.2024
2485. Find the Pivot Integer
https://leetcode.com/problems/find-the-pivot-integer/description/

Given a positive integer n, find the pivot integer x such that:
The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1.
It is guaranteed that there will be at most one pivot index for the given input.

Example 1:
Input: n = 8
Output: 6
Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

Example 2:
Input: n = 1
Output: 1
Explanation: 1 is the pivot integer since: 1 = 1.

Example 3:
Input: n = 4
Output: -1
Explanation: It can be proved that no such integer exist.
"""

# Runtime 34 ms Beats 35.58% of users with Python
# Memory 11.73 MB Beats 16.06% of users with Python
# Runtime 28 ms Beats 44.15% of users with Python
# Memory 11.69 MB Beats 46.00% of users with Python
# Runtime 27 ms Beats 45.96% of users with Python
# Memory 11.57 MB Beats 77.93% of users with Python

def pivotInteger(n):
    """
    :type n: int
    :rtype: int
    """
    if n==1: return n
    bigsum=(2+n-1)*n//2
    for i in range(n):
        bs2 = (2+i-1)*i//2
        if bs2==bigsum-bs2+i: return i
    return -1

print(pivotInteger(8))