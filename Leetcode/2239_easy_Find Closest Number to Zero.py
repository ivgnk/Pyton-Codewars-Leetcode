'''
2239. Find Closest Number to Zero
https://leetcode.com/problems/find-closest-number-to-zero/description/

Given an integer array nums of size n, return the number with the value closest to 0 in nums.
If there are multiple answers, return the number with the largest value.

Example 1:
Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.
Example 2:

Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
'''


def findClosestNumber2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1: return nums[0]
    if len(nums) == 2 and nums[0] == nums[1]: return nums[0]
    if 0 in nums: return 0

    mi = [i for i in nums if i < 0]
    mib = mi != []
    print(mi,mib)
    if mib:  mmin = sorted(mi, reverse=True)

    ma = [i for i in nums if i > 0]
    mab = ma != []
    print(ma,mab)
    if mab:  mmax = sorted(ma)

    if not mib: return mmax[0]
    if not mab: return mmin[0]

    if abs(mmin[0]) < abs(mmax[0]):
        return mmin[0]
    else:
        return mmax[0]

# Runtime 102 ms Beats 92.00% of users with Python
# Memory 11.86 MB Beats 44.57% of users with Python

def findClosestNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll=len(nums)
    if ll == 1: return nums[0]
    if ll == 2 and nums[0] == nums[1]: return nums[0]
    if 0 in nums: return 0
    mmin=nums[0]; sabs=abs(nums[0])
    for i in range(1,ll):
        j=abs(nums[i])
        if sabs>j:
            sabs = j
            mmin = nums[i]
    if mmin<0 and sabs in nums:
        return sabs
    else: return mmin

print(findClosestNumber([-4,-2,1,4,8]))
# print(findClosestNumber([2,-1,1]))
# print(findClosestNumber([-10,-12,-54,-12,-544,-10000]))