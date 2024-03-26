'''
1122. Relative Sort Array
https://leetcode.com/problems/relative-sort-array/description/

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

Example 1:
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

Example 2:
Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]
'''

# Runtime 28 ms Beats 20.68%  of users with Python
# Memory 11.93 MB Beats 10.55% of users with Python

from collections import Counter
def relativeSortArray(arr1, arr2):
    """
    :type arr1: List[int]
    :type arr2: List[int]
    :rtype: List[int]
    """
    nlsst=[i for i in arr1 if i in arr2]
    ddict2 = dict(Counter(nlsst))
    res=[]
    for i in arr2:
        for j in range(ddict2[i]):
            res.append(i)
    res2 = [i for i in arr1 if i not in arr2]
    res2.sort()
    return res+res2

print(relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]))
