"""
Done 30.05.2024. Topics: Array
2016. Maximum Difference Between Increasing Elements
https://leetcode.com/problems/maximum-difference-between-increasing-elements/description/

Given a 0-indexed integer array nums of size n,
find the maximum difference between nums[i] and nums[j]
(i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].
Return the maximum difference. If no such i and j exists, return -1.

Example 1:
Input: nums = [7,1,5,4]
Output: 4
Explanation:
The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.

Example 2:
Input: nums = [9,4,3,2]
Output: -1
Explanation:
There is no i and j such that i < j and nums[i] < nums[j].

Example 3:
Input: nums = [1,5,2,10]
Output: 9
Explanation:
The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.

Hint 1
Could you keep track of the minimum element visited while traversing?
Hint 2
We have a potential candidate for the answer if the prefix min is lesser than nums[i].
"""

# Runtime 31 ms Beats 60.93% of users with Python
# Memory 11.62 MB Beats 82.12% of users with Python
# Runtime 27 ms Beats 68.87% of users with Python
# Memory 11.72 MB Beats 55.63% of users with Python
# Runtime 24 ms Beats 76.16% of users with Python
# Memory 11.71 MB Beats 55.63% of users with Python

def maximumDifference(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n1=sorted(nums,reverse=True)
    if n1==nums: return -1
    mmax=max(nums)
    mmin=min(nums)
    if nums.index(mmax)>nums.index(mmin): return mmax-mmin

    ll=len(nums)
    i=0; j=1
    mmax = -1
    while j<ll-1:
        if nums[j]>nums[i]:
            mmax=max(mmax,nums[j]-nums[i])
            j=j+1
        else:
            i=i+1; j=i+1
    return  mmax

print(maximumDifference([7,1,5,4]))
print(maximumDifference([9,4,3,2]))
print(maximumDifference([1,5,2,10]))


