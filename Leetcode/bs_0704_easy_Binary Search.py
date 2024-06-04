"""

704. Binary Search
https://leetcode.com/problems/binary-search/description/

Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""

# Runtime 178 ms Beats 61.52% of users with Python
# Memory 12.98 MB Beats 22.89% of users with Python

def search(nums, target):
    if target in nums:
        ll=len(nums)
        if ll==1: return 0
        i,j=0,ll-1
        while i<j:
            if target==nums[i]: return i
            elif target==nums[j]: return j
            else:
                mid=(i+j)//2
                nn=nums[mid]
                if target==nn: return mid
                elif nn>target:
                    j=mid
                else: i=mid
    else:
        return -1

# print(search(nums = [-1,0,3,5,9,12], target = 2))
# print(search(nums = [-1,0,3,5,9,12], target = 9))
print(search(nums = [-1,0,3,5,9,12], target = 9))

# Runtime 166 ms Beats 98.77% of users with Python
# Memory 12.88 MB Beats 55.66% of users with Python
def search3(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    return nums.index(target) if target in nums else -1

# Runtime 180 ms Beats 48.03% of users with Python
# Memory 12.81 MB Beats 55.66% of users with Python

def search3(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if target in nums:
        return nums.index(target)
    else:
        return -1


