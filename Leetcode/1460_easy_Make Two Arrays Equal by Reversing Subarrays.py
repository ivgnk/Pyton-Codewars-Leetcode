'''
1460. Make Two Arrays Equal by Reversing Subarrays
https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/description/

You are given two integer arrays of equal length target and arr.
In one step, you can select any non-empty subarray of arr and reverse it.
You are allowed to make any number of steps.
Return true if you can make arr equal to target or false otherwise.
'''

# Runtime 56 ms Beats 55.88% of users with Python
# Memory 11.94 MB Beats 20.10% of users with Python

def canBeEqual(target, arr):
    """
    :type target: List[int]
    :type arr: List[int]
    :rtype: bool
    """
    return sorted(target) == sorted(arr)