'''
1287. Element Appearing More Than 25% In Sorted Array
https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/description/

Given an integer array sorted in non-decreasing order,
there is exactly one integer in the array that occurs
more than 25% of the time, return that integer.

Example 1:
Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

Example 2:
Input: arr = [1,1]
Output: 1
'''

#  60 ms Beats 83.33% of users with Python
#  Memory 13.75 MB Beats 9.77% of users with Python

from collections import Counter
def findSpecialInteger(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    ddict = dict(Counter(arr))
    return max(ddict, key=ddict.get)