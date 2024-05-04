'''
Re-solution 04.05.2024
Given a non-empty array of integers nums,
every element appears twice except for one.
Find that single one.
You must implement a solution with a linear runtime complexity
and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
'''

# Runtime 99 ms Beats 49.51% of users with Python
# Memory 15.09 MB Beats 7.39% of users with Python
# Runtime 95 ms Beats 64.50% of users with Python
# Memory 15.00 MB Beats 7.39% of users with Python
# Runtime 81 ms Beats 99.29% of users with Python
# Memory 14.89 MB Beats 7.39% of users with Python

from collections import Counter
def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:    return nums[0]
    elif len(nums) == 0:  return []
    aset = set(nums)
    # www.geeksforgeeks.org/python-convert-a-set-into-dictionary/
    bdict = dict.fromkeys(aset, 0)
    for i in nums:
        bdict[i]=bdict[i]+1
    for key,value in bdict.items():
        if value==1: return key

# Runtime 112 ms Beats 30.42% of users with Python
# Memory 15.30 MB Beats 7.39%# of users with Python
# Runtime 102 ms Beats 40.90% of users with Python
# Memory 15.28 MB Beats 7.39% of users with Python
def singleNumber2(nums):
    dd=dict(Counter(nums))
    for k,v in dd.items():
        if v == 1: return k


print(singleNumber([4,1,2,1,2]))