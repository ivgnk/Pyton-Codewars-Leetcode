'''
1207. Unique Number of Occurrences
https://leetcode.com/problems/unique-number-of-occurrences/description/

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
'''

# Runtime 20 ms Beats 58.17% of users with Python
# Memory 11.84 MB Beats 21.82% of users with Python

from collections import Counter

def uniqueOccurrences(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    ddict= dict(Counter(arr))
    llen =len(ddict)
    sset=set([v for v in ddict.values()])
    return llen==len(sset)

print(uniqueOccurrences([1,2,2,1,1,3]))
print(uniqueOccurrences([1,2]))
print(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))