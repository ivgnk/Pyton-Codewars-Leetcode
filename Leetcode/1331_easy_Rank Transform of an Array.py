'''
1331. Rank Transform of an Array
https://leetcode.com/problems/rank-transform-of-an-array/description/

Given an array of integers arr, replace each element with its rank.
The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.

Example 1:
Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.

Example 2:
Input: arr = [100,100,100]
Output: [1,1,1]
Explanation: Same elements share the same rank.
'''

# Runtime 242 ms Beats 72.14% of users with Python
# Memory 29.32 MB Beats 35.50% of users with Python

from collections import Counter
def arrayRankTransform(arr):
    """
    :type arr: List[int]
    :rtype: List[int]
    """
    sset=set(arr)
    llst=sorted(list(sset))
    sset={}
    for i,dat in enumerate(llst):
        sset[dat]=i
    res=[]
    for i,dat in enumerate(arr):
         res.append(sset[dat]+1)
    return(res)

print(arrayRankTransform([40,10,20,30]))
