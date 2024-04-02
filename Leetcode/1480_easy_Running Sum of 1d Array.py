'''
1480. Running Sum of 1d Array
https://leetcode.com/problems/running-sum-of-1d-array/description/

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
'''

def runningSum2(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ssum=nums[0]; res=[ssum]
    for i in range(1,len(nums)):
        ssum=ssum+nums[i]
        res.append(ssum)
    return res

# Runtime 27 ms Beats 19.24% of users with Python
# Memory 11.91 MB Beats 12.61% of users with Python
# https://lifewithdata.com/2023/08/26/leetcode-running-sum-of-1d-array-solution/
def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums

print(runningSum([1,2,3,4]))
print(runningSum([1,1,1,1,1]))