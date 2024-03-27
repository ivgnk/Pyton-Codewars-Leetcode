'''
645. Set Mismatch
https://leetcode.com/problems/set-mismatch/description/

You have a set of integers s, which originally contains all the numbers from 1 to n.
Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set,
which results in repetition of one number and loss of another number.
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Example 2:
Input: nums = [1,1]
Output: [1,2]
'''

from collections import Counter

# Runtime 165 ms Beats 39.05% of users with Python
# Memory 14.76 MB Beats 5.39% of users with Python
  
def findErrorNums(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ddict = dict(Counter(nums))
    res = [key for key, value in ddict.items() if value == 2]
    llen = len(nums)
    ms = set([i + 1 for i in range(llen)])
    ws = set(nums)
    dat = list(ms - ws)
    res.append(dat[0])
    return res

print(findErrorNums([1,2,2,4]))