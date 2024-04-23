"""
1365. How Many Numbers Are Smaller Than the Current Number
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.

Example 1:
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]

Example 2:
Input: nums = [6,5,4,8]
Output: [2,1,0,3]

Example 3:
Input: nums = [7,7,7,7]
Output: [0,0,0,0]
"""

# Runtime 167 ms Beats 56.29% of users with Python
# Memory 11.62 MB Beats 72.00% of users with Python

def smallerNumbersThanCurrent(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # ------1
    # if len(set(nums)) == 1: return [0] * len(nums)
    # res=[]
    # for i in nums:
    #     res.append(sum(1 for j in nums if i>j))
    # return res

    # ------2
    # if len(set(nums))==1: return [0]*len(nums)
    # res=[]
    # for i in nums:
    #     res.append(sum(1 for j in nums if i>j))

    # ------3
    return [sum(1 for j in nums if i > j) for i in nums]

print(smallerNumbersThanCurrent([8,1,2,2,3]))