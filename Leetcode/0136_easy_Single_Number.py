'''
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

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 2: return nums
    aset = set(nums)
    # www.geeksforgeeks.org/python-convert-a-set-into-dictionary/
    bdict = dict.fromkeys(aset, 0)
    for i in nums:
        bdict[i]=bdict[i]+1
    for key,value in bdict.items():
        if value==1: return key

print(singleNumber([4,1,2,1,2]))