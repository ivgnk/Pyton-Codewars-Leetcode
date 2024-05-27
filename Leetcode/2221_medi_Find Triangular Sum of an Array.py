"""
Done 27.05.2024. Topics: Array, Math
2221. Find Triangular Sum of an Array
https://leetcode.com/problems/find-triangular-sum-of-an-array/description/

You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).

The triangular sum of nums is the value of the only element present in nums after the following process terminates:

Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n - 1.
For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes modulo operator.
Replace the array nums with newNums.
Repeat the entire process starting from step 1.
Return the triangular sum of nums.

Input: nums = [1,2,3,4,5]
Output: 8
Explanation:
The above diagram depicts the process from which we obtain the triangular sum of the array.

Example 2:
Input: nums = [5]
Output: 5
Explanation:
Since there is only one element in nums, the triangular sum is the value of that element itself.

Hint 1
Try simulating the entire process.
Hint 2
To reduce space,
use a temporary array to update nums in every step instead of creating a new array at each step.
"""

# https://leetcode.com/problems/find-triangular-sum-of-an-array/solutions/1907012/python-3-intuitive-brute-force-optimal/
# Runtime 1700 ms Beats 76.86% of users with Python
# Memory 11.61 MB Beats 95.04% of users with Python
def triangularSum(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    while n > 0:
        for i in range(n - 1):
            nums[i] = (nums[i] + nums[i + 1]) % 10
        n -= 1
    return nums[0]


# Runtime 2067 ms Beats 46.28% of users with Python
# Memory 11.76 MB Beats 80.17% of users with Python
# Runtime 2044 ms Beats 47.11% of users with Python
# Memory 11.86 MB Beats 58.68% of users with Python

def triangularSum2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll=len(nums); t1=nums; t2=[]
    for i in range(ll-1):
        ll1=len(t1)
        for j in range(1,ll1):
            t2.append((t1[j]+t1[j-1])%10)
        t1=t2
        t2=[]
    return t1[0]

print(triangularSum([1,2,3,4,5]))

