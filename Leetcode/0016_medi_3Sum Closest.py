"""
Done 19.07.2024. Topics: Two Pointers, Sorting
16. 3Sum Closest
https://leetcode.com/problems/3sum-closest/description/

Given an integer array nums of length n and an integer target,
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0)
"""
from icecream import ic

# Runtime 362 ms Beats 96.39%
# Memory 11.72 MB Beats 21.69%
def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    ll = len(nums);    nu = sorted(nums)
    mmin = 10000;    si = (0, 1, 2)
    for i in range(ll - 2):
        s = target - nu[i]
        j = i + 1;        k = ll - 1
        while j < k:
            njks = nu[j] + nu[k] - s
            mm = abs(njks)
            if mm < mmin:
                mmin = mm;                si = (i, j, k)
            if njks > 0:
                k = k - 1
            elif njks < 0:
                j = j + 1
            else:
                return nu[i] + nu[j] + nu[k]
    return nu[si[0]] + nu[si[1]] + nu[si[2]]


# Runtime 393 ms Beats 94.23%
# Memory 11.65 MB Beats 54.16%
def threeSumClosest(nums, target):
    ll = len(nums);    nu = sorted(nums)
    mmin = 10000;    si = (0, 1, 2)
    for i in range(ll - 2):
        s = target - nu[i]
        j = i + 1;  k = ll - 1
        while j < k:
            njk = nu[j] + nu[k]
            mm = abs(njk - s)
            if mm < mmin:
                mmin = mm;   si = (i, j, k)
            if njk - s > 0:
                k = k - 1
            elif njk - s < 0:
                j = j + 1
            else:
                return nu[i] + nu[j] + nu[k]
    return nu[si[0]] + nu[si[1]] + nu[si[2]]

ic(threeSumClosest(nums = [4,0,5,-5,3,3,0,-4,-5], target = -2))

# nums =
# [4,0,5,-5,3,3,0,-4,-5]


# print(threeSumClosest(nums = [-1,2,1,-4], target = 1))
# print(threeSumClosest(nums = [0,0,0], target = 1))
# print(threeSumClosest([4,0,5,-5,3,3,0,-4,-5],-2))
# print(threeSumClosest(nums = [1,1,1,0], target = -100))


# Time Limit Exceeded - 67 / 102 testcases passed
def threeSumClosest6(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    ll = len(nums)
    mmin = 10000
    for i in range(ll):
        for j in range(i + 1, ll):
            nij = nums[i] + nums[j]
            for k in range(j + 1, ll):
                nk = nums[k] - target
                if abs(nij + nk) < mmin:
                    mmin = abs(nij + nk)
                    sav = nij + nums[k]
    return sav

# 68 / 102 testcases passed
def threeSumClosest5(nums, target):
    # numss=sorted(nums)
    # i=0; j=len(target)
    ll=len(nums)
    mmin=10000
    res=[]
    for i in range(ll):
        for j in range(i + 1,ll):
            nij=nums[i] + nums[j]
            for k in range(j + 1, ll):
                if abs(nij + nums[k] - target) < mmin:
                    mmin = abs(nij + nums[k] - target)
                    sav = nij + nums[k]
                    res.append((nums[i], nums[j], nums[k], sav))
    ic(res)
    return sav


# Time Limit Exceeded - 60 / 102 testcases passed
# nums = [4,0,5,-5,3,3,0,-4,-5] target = -2 Expected = -2
def threeSumClosest4(nums, target):
    ll=len(nums)
    mmin=10000; sav=-131313
    res=[]
    for i in range(ll):
        for j in range(i + 1,ll):
            for k in range(j + 1, ll):
                if abs(nums[i] + nums[j] + nums[k] - target) < mmin:
                    mmin = abs(nums[i] + nums[j] + nums[k] - target)
                    sav = nums[i] + nums[j] + nums[k]
                    res.append((nums[i], nums[j], nums[k], sav))
    ic(res)
    return sav


# Wrong Answer -  73 / 102 testcases passed
def threeSumClosest1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    lst = []
    n = 1
    while n <= 3:
        print(n, nums)
        mmin = min(nums, key=lambda x: abs(x - target))
        lst.append(mmin)
        nums.remove(mmin)
        print(n, nums, lst, mmin)
        n = n + 1
    return sum(lst)

# print(threeSumClosest(nums = [4,0,5,-5,3,3,0,-4,-5], target = -2))


# Time Limit Exceeded -- 46 / 102 testcases passed
from itertools import permutations, combinations
def threeSumClosest3(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    r=1e38
    perm=list(combinations(nums,3))
    ll=len(perm)
    for i in range(ll):
        s=sum(perm[i])
        r1=abs(s-target)
        if r1<r:
            r=r1
            mmin=s
        # print(i, perm[i], s,r1,mmin)
    return mmin

def threeSumClosest2(nums, target):
    llen = len(nums)
    if llen<100:
        lst=[]
        n=1
        while n<=3:
            print(n,nums)
            mmin=min(nums, key=lambda x: abs(x - target))
            lst.append(mmin)
            nums.remove(mmin)
            print(n,nums,lst,mmin)
            n=n+1
            return sum(lst)
    else:
        r = 1e38
        perm = list(combinations(nums, 3))
        ll = len(perm)
        for i in range(ll):
            s = sum(perm[i])
            r1 = abs(s - target)
            if r1 < r:
                r = r1
                mmin = s
        return mmin

