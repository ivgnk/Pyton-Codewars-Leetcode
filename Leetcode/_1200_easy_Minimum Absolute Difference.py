'''
1200. Minimum Absolute Difference
https://leetcode.com/problems/minimum-absolute-difference/description/

Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr

Example 1:
Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

Example 2:
Input: arr = [1,3,6,10,15]
Output: [[1,3]]

Example 3:
Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
'''

# Memory Limit Exceeded     33 / 38 testcases passed

from itertools import permutations
def minimumAbsDifference(arr):
    """
    :type arr: List[int]
    :rtype: List[List[int]]
    """
    res1=[]
    perm = list(permutations(arr, 2))
    razn=1000000

    for dat in perm:
        if dat[1]>dat[0]:
            r=dat[1]-dat[0]
            if r<razn: razn=r
            res1.append(dat)
    res2=[]
    for dat in res1:
        if dat[1]-dat[0]==razn:
            res2.append(dat)
    res3=sorted(res2)
    return res3


print(minimumAbsDifference(arr = [4,2,1,3]))