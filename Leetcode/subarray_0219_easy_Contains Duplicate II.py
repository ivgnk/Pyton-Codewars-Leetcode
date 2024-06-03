'''
Done 04.06.2024. Topics: Array, Hash Table, Sliding Window
219. Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/description/

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

from icecream import ic
from collections import Counter


# Runtime 464 ms Beats 80.42% of users with Python
# Memory 23.04 MB Beats 35.97% of users with Python

def containsNearbyDuplicate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    dd = dict()
    for i in range(len(nums)):
        if nums[i] in dd and abs(i - dd[nums[i]]) <= k:
            return True
        dd[nums[i]] = i
    return False


# Runtime 498 ms Beats 11.96% of users with Python3
# Memory 34.49 MB Beats 11.08% of users with Python3
# Runtime 489 ms Beats 14.49% of users with Python3
# Memory 34.62 MB Beats 9.37% of users with Python3

def containsNearbyDuplicate5(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    if k==0: return False
    ll = len(nums)

    if ll == 1: return False
    elif ll==2 and nums[0]==nums[1]: return True
    elif nums[ll - 1] == nums[ll - 2]: return True
    dd = dict()
    # rll=
    no_double=True
    for i in range(ll):
        if nums[i] in dd:
            dd[nums[i]].append(i)
            no_double = False
        else:
            dd[nums[i]]=[i]
    if no_double: return False

    lst=[v for k,v in dd.items() if len(v)>1 ]
    ll2=len(lst)
    for i in range(ll2):
        lst2=lst[i]
        llst2=len(lst2)
        for j in range(llst2):
            for k1 in range(j+1,llst2):
                if lst2[k1]-lst2[j]<=k: return True
    return False



ic(containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))

# Runtime 546 ms Beats 5.41% of users with Python3
# Memory 33.13 MB Beats 11.59% of users with Python3

def containsNearbyDuplicate3(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    if k==0: return False
    ll = len(nums)

    if ll == 1: return False
    elif ll==2 and nums[0]==nums[1]: return True
    elif nums[ll - 1] == nums[ll - 2]: return True

    # if ll < k: return False

    dd=dict(Counter(nums))
    arr=sorted([(v,k) for k,v in dd.items()],reverse=True)
    if arr[0][0]==1: return False

    if arr[0][0] == ll and k > 1: return True

    rll=range(ll)
    ll3=len(arr)
    i=0
    while arr[i][0]>1 and i<ll3-1:
        arr2=[j for j in rll if nums[j]==arr[i][1]]
        ll2=len(arr2)
        if ll2==2:
           if arr2[-1]-arr2[0]<=k: return True
        else:
            for j in range(ll2):
                for k in range(j+1,ll2):
                    if arr2[k]-arr2[j]<=k:
                        return True
        i=i+1

    return False

# print(containsNearbyDuplicate(nums = [1,2,2,3], k = 3))

# Time Limit Exceeded -- 20 / 58 testcases passed
def containsNearbyDuplicate2(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    if k==0: return False
    ll = len(nums)

    if ll == 1: return False
    elif ll==2 and nums[0]==nums[1]: return True
    elif nums[ll - 1] == nums[ll - 2]: return True

    for i in range(ll - k):
        for j in range(i+1, i + k + 1):
            print(i,j)
            if nums[i] == nums[j]:
                print(i,j)
                return True
    return False
