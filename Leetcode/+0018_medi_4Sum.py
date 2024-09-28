'''
28.09.2024. Array, Two Pointers, Sorting
0018. 4Sum
https://leetcode.com/problems/4sum/description/

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
'''

# Runtime 691 ms Beats 31.02%
# Memory 11.54 MB Beats 79.83%
# Runtime 665 ms Beats 32.24%
# Memory 11.52 MB Beats 79.83%
def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    nums.sort()
    s = set(); ll=len(nums); ll1=ll-1
    for i in range(ll):
        for j in range(i + 1, ll):
            l = j + 1
            r = ll1
            s2=nums[i] + nums[j]
            while l < r:
                s22=nums[l] + nums[r]
                sss=s2+s22
                if sss < target:
                    l += 1
                elif sss > target:
                    r -= 1
                elif sss == target:
                    s.add((nums[i], nums[j], nums[l], nums[r]))
                    l += 1
                    r -= 1
    return list(s)

# 144, 162 235 271? 762, 916 - skip double,
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(fourSum(nums = [1,0,-1,0,-2,2], target = 0))
# print(fourSum(nums = [2,2,2,2,2], target =8))



#  Time Limit Exceeded -- 275 / 294 testcases passed

def fourSum2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    ll = len(nums)
    res=[]
    for i in range(ll):
        for j in range(i+1, ll):
            for k in range(j+1, ll):
                for l in range(k + 1, ll):
                    if i != j:
                        if j != k:
                            if k != l:
                                if i != k:
                                    if i != l:
                                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                                            res.append(sorted([nums[i], nums[j], nums[k], nums[l]]))
    # https://stackoverflow.com/questions/3724551/uniqueness-for-list-of-lists
    res = [list(x) for x in set(tuple(x) for x in res)]
    return res

# not work because nit change i,j,k,l
def fourSum333(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    res=[]
    ll = len(nums); nums=sorted(nums)
    i=0; j=ll-1
    while i<j:
        s1=nums[i]+nums[j]
        k=0; l=ll-1
        while k<l:
            s2 = nums[k] + nums[l]
            if j != k:
                if k != l:
                    if i != k:
                        if i != l:
                            if j != l:
                                if s1+s2==target:
                                    res.append(sorted([nums[i], nums[j], nums[k], nums[l]]))
    res = [list(x) for x in set(tuple(x) for x in res)]
    return res

# Time Limit Exceeded - 282 / 294 testcases passed
def fourSum3(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    ll = len(nums)
    res = []
    for i in range(ll):
        for j in range(i + 1, ll):
            if i != j:
                ss = nums[i] + nums[j]
                for k in range(j + 1, ll):
                    if j != k:
                        tt = ss + nums[k]
                        for l in range(k + 1, ll):
                            if k != l:
                                if i != k:
                                    if i != l:
                                        uu = tt + nums[l]
                                        if uu == target:
                                            res.append(sorted([nums[i], nums[j], nums[k], nums[l]]))
    # https://stackoverflow.com/questions/3724551/uniqueness-for-list-of-lists
    res = [list(x) for x in set(tuple(x) for x in res)]
    return res

import sys
def fourSum555(nums, target):
    ll = len(nums)
    sums = []; res=[]
    for i in range(ll):
        for j in range(i + 1, ll):
            sums.append( ( nums[i] + nums[j], (i, j) ) )
            print(i, j ,'   ',nums[i],nums[j])
    sums.sort()
    print(sums)
    sys.exit()
    lsum=len(sums)
    i=0; j=lsum-1
    while i<j:
        ssss=sums[i][0]+sums[j][0]
        if ssss==target:
            n1=sums[i][1][0]
            n2=sums[i][1][1]
            n3=sums[j][1][0]
            n4=sums[j][1][1]
            ss={n1,n2,n3,n4}
            if len(ss)==4:
                res.append([nums[n1], nums[n2], nums[n3], nums[n4]])
            i += 1
        elif ssss>target:
            j-=1
        else: i+=1
    ss=set()
    for i,d in enumerate(res):
        s=tuple(sorted(d))
        # print(i,d,s)
        ss.add(s)
    return list(ss)



