"""
Done 06.05.2024. Topics: Array, Prefix Sum
2574. Left and Right Sum Differences
https://leetcode.com/problems/left-and-right-sum-differences/description/

Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:
answer.length == nums.length.
answer[i] = |leftSum[i] - rightSum[i]|.
Where:
leftSum[i] is the sum of elements to the left of the index i in the array nums.
If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums.
If there is no such element, rightSum[i] = 0.
Return the array answer.

Example 1:
Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

Example 2:
Input: nums = [1]
Output: [0]
Explanation: The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].
"""

# https://leetcode.com/problems/left-and-right-sum-differences/solutions/4357424/very-easy-solution-python/
# Runtime 62 ms Beats 74.72% of users with Python3
# Memory 16.82 MB Beats 68.99% of users with Python3
from itertools import accumulate

def leftRightDifference(nums):
    left = list(accumulate(nums, initial=0))
    right = list(accumulate(nums[::-1], initial=0))[:-1][::-1]
    for i in range(len(nums)):
        nums[i] = abs(left[i] - right[i])
    return nums



# Runtime 133 ms Beats 36.20% of users with Python
# Memory 11.82 MB Beats 82.00% of users with Python

def leftRightDifference2(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ll = len(nums)
    res=[]
    leftSum=[sum(nums[:i]) for i in range(ll)]
    rightSum=[sum(nums[i+1:]) for i in range(ll)]
    for i in range(ll):
        res.append(abs(leftSum[i]-rightSum[i]))
    return res

# Runtime 90 ms Beats 48.00% of users with Python
# Memory 12.26 MB Beats 5.40% of users with Python
def leftRightDifference3(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ll = len(nums)
    res=[]; total=sum(nums)
    leftSum=[sum(nums[:i]) for i in range(ll)]
    rightSum=[total-nums[i]-leftSum[i] for i in range(ll)]
    for i in range(ll):
        res.append(abs(leftSum[i]-rightSum[i]))
    return res


print(leftRightDifference3([10,4,8,3]))