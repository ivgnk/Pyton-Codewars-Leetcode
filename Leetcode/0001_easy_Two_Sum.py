"""
Re-solution 03.05.2024
1. Two Sum

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

# Runtime 2111 ms Beats 44.53% of users with Python
# Memory 12.55 MB Beats 49.61% of users with Python

def twoSum(nums, target):
    n = len(nums)
    res =[]
    for i in range(n):
        for j in range(i+1,n):
            if (nums[i]+nums[j]==target):
                res.append(i); res.append(j)
                return res


# Runtime 1396 ms Beats 48.56% of users with Python
# Memory 12.50 MB Beats 77.70% of users with Python
def twoSum2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    n = len(nums)
    res = []
    # mmap= [False if i>target else True for i in nums]
    for i in range(n):
        tt = target - nums[i]
        for j in range(i + 1, n):
            if nums[j] == tt:
                res.append(i);  res.append(j)
                return res

# Runtime 33 ms Beats 91.15% of users with Python
# Memory 12.51 MB Beats 49.61% of users with Python
def twoSum3(nums, target):
    seen={}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen:
            print(seen)
            return [seen[diff],i]
        else:
            seen[nums[i]] = i

# Runtime 43 ms Beats 62.81% of users with Python
# Memory 13.20 MB Beats 6.77% of users with Python
# Runtime 35 ms Beats 86.31% of users with Python
# Memory 13.05 MB Beats 6.77% of users with Python
def twoSum4(nums, target):
    ll=len(nums)
    n2=sorted([[nums[i],i] for i in range(ll)])
    i=0;j=ll-1
    while i<j:
       if n2[i][0]+n2[j][0]==target: return [n2[i][1],n2[j][1]]
       elif n2[i][0]+n2[j][0]>target: j=j-1
       else: i=i+1


# print(twoSum3(nums = [2,7,11,15], target = 9))
print(twoSum4(nums = [2,7,11,15], target = 9))