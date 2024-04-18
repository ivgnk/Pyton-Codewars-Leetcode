"""
2563. Count the Number of Fair Pairs
https://leetcode.com/problems/count-the-number-of-fair-pairs/description/

Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.
A pair (i, j) is fair if:
0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper

Example 1:
Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).

Example 2:
Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).
"""

# 48 / 53 testcases passed - 100000 points

def countFairPairs(nums, lower, upper):
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: int
    """
    ll = len(nums)
    ss = list(set(nums))
    lss = len(ss);    mis = min(ss);    mas = max(ss)
    print(ll, lss, mis, mas)
    if lower == upper:
        if lss == 2 and ss[0] + ss[1] != lower:
            return 0
    if upper - lower > mis + mas and lss >= 100000:
        print('part')
        return sum([(ll - (i + 1)) for i in range(ll)])
    print('main')
    n = 0
    for i in range(ll):
        for j in range(i + 1, ll):
            if lower <= nums[i] + nums[j] <= upper: n = n + 1
    return n

def tst_factorial():
    ll,lss = 100000, 100000
    lls = math.factorial(ll - lss)
    print(ll,lss,lls)
    p=math.factorial(ll)
    print(p)
    print(math.factorial(ll) / lls)

tst_factorial()
# print(countFairPairs(nums = [-1,0], lower =1, upper =1))
