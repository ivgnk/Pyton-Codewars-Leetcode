'''
https://leetcode.com/problems/sort-colors/description/
Given an array nums with n objects colored red, white, or blue, sort them in-place
so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
'''
from copy import deepcopy

def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    a = []
    n0 = 0;    n1 = 0;    n2 = 0
    for i in nums:
        # if i==0: n0 += 1
        # if i==1: n1 += 1
        # if i==2: n2 += 1
        match i:
            case 0: n0 += 1
            case 1: n1 += 1
            case 2: n2 += 1

    for i in range(n0):  a.append(0)
    for i in range(n0,n0+n1):  a.append(1)
    for i in range(n0+n1,n0+n1+n2):  a.append(2)
    return a

print(sortColors([2,0,2,1,1,0]))
print(sortColors([2,0,1]))