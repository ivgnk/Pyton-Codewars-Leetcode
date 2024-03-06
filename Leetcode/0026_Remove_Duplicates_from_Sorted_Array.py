'''
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.
Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k,
to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain
the unique elements in the order they were present in nums initially.
The remaining elements of nums are not important as well as the size of nums.
Return k.
'''

from copy import deepcopy

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sset = list(set(nums)); llen = len(sset)
    print(sset,'  ',type(sset))
    sset.sort()
    for i in range(llen):
        nums[i] = sset[i]
    return len(sset)

# print(removeDuplicates([1,1,2]))
c = [3,0,-1,0,3,0,0]
# a = deepcopy(c)
# b1 = sorted(a); c.sort()
# print(b1); print(c)
print(removeDuplicates(c))

