"""
60. Permutation Sequence
https://leetcode.com/problems/permutation-sequence/description/

The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
"""

from itertools import permutations
def getPermutation(n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    lst=[i+1 for i in range(n)]
    lst2=list(permutations(lst, n))
    r = lst2[k-1]
    return ''.join([str(i) for i in r])

print(getPermutation(3,3))