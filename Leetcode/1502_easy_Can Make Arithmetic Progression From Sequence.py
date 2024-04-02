'''
1502. Can Make Arithmetic Progression From Sequence
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/description/

A sequence of numbers is called an arithmetic progression
if the difference between any two consecutive elements is the same.
Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression.
Otherwise, return false.
'''

# Runtime 17 ms Beats 83.49% of users with Python
# Memory 11.90 MB Beats 13.65% of users with Python

def canMakeArithmeticProgression(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    arr2 = sorted(arr)
    ll = len(arr)
    llen = [arr2[i] - arr2[i - 1] for i in range(1, ll)]
    return len(set(llen)) == 1