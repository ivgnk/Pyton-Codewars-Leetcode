'''
1991. Find the Middle Index in Array

Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).
A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].
If middleIndex == 0, the left side sum is considered to be 0. Similarly, if middleIndex == nums.length - 1, the right side sum is considered to be 0.
Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.

Example 1:
Input: nums = [2,3,-1,8,4]
Output: 3
Explanation: The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
The sum of the numbers after index 3 is: 4 = 4

Example 2:
Input: nums = [1,-1,4]
Output: 2
Explanation: The sum of the numbers before index 2 is: 1 + -1 = 0
The sum of the numbers after index 2 is: 0

Example 3:
Input: nums = [2,5]
Output: -1
Explanation: There is no valid middleIndex.
'''

# Runtime 22 ms   Beats 61.35% of users with Python
# Memory 11.73 MB Beats 7.36% of users with Python

def findMiddleIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    llen = len(nums)
    if llen == 1 or all(v is 0 for v in nums): return 0
    if llen == 2 and nums[0] == -nums[1]: return -1
    if llen == 3 and nums[0] == -nums[2] and nums[2] != 0: return -1
    if sum(nums[1:]) == 0: return 0
    for i in range(llen):
        sl = sum(nums[0:i + 1])
        sr = sum(nums[i + 2:])
        if sl == sr: return i + 1
    return -1


print(findMiddleIndex([2,3,-1,8,4]))
print(findMiddleIndex([1,-1,4]))
print(findMiddleIndex([2,5]))

