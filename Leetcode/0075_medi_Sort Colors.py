'''
Done 12.06.2024. Topics: Array, Two Pointers, Sorting
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

Hint 1
A rather straight forward solution is a two-pass algorithm using counting sort.
Hint 2
Iterate the array counting number of 0's, 1's, and 2's.
Hint 3
Overwrite array with the total number of 0's, then 1's and followed by 2's.
'''

# Runtime 37 ms Beats 57.63% of users with Python3
# Memory 16.46 MB Beats 79.02% of users with Python3

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

    for i in range(n0):  nums[i] = 0
    for i in range(n0, n0 + n1):  nums[i] = 1
    for i in range(n0 + n1, n0 + n1 + n2):  nums[i] = 2
    # return a

print(sortColors([2,0,2,1,1,0]))
print(sortColors([2,0,1]))