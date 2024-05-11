"""
Done 12.05.2024. Topics: Array
941. Valid Mountain Array
https://leetcode.com/problems/valid-mountain-array/description/

Given an array of integers arr, return true if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:
arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:
Input: arr = [2,1]
Output: false

Example 2:
Input: arr = [3,5,5]
Output: false

Example 3:
Input: arr = [0,3,2,1]
Output: true

Hint 1
It's very easy to keep track of a monotonically increasing or decreasing ordering of elements.
You just need to be able to determine the start of the valley in the mountain and from that point onwards,
it should be a valley i.e. no mini-hills after that.
Use this information in regards to the values in the array and
you will be able to come up with a straightforward solution.
"""

from collections import Counter

# Runtime 189 ms Beats 5.21% of users with Python
# Memory 14.76 MB Beats 6.40% of users with Python
def validMountainArray2(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    ll=len(arr)
    if ll<3: return False
    elif ll==3: return arr[0]<arr[1]>arr[2]

    dd=dict(Counter(arr))
    n2=[v<3 for k,v in dd.items()]
    if not all(n2): return False
    uniq=[arr[i] != arr[i-1] for i in range(1,ll)]
    if arr == sorted(arr) and all(uniq): return False
    if arr == sorted(arr, reverse=True) and all(uniq): return False

    mmax=max(arr)
    if arr.count(mmax)>1: return False
    ind=arr.index(mmax)
    l=arr[:ind+1]
    r=arr[ind:]
    ul = [l[i] != l[i - 1] for i in range(1,len(l))]
    ur = [r[i] != r[i - 1] for i in range(1, len(r))]
    if not(all(ul)) or not(all(ur)): return False

    return l==sorted(l) and r==sorted(r, reverse=True)

# Runtime 198 ms Beats 5.21% of users with Python
# Memory 14.84 MB Beats 6.40% of users with Python

def validMountainArray3(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    ll=len(arr)
    if ll<3: return False
    elif ll==3: return arr[0]<arr[1]>arr[2]

    dd=dict(Counter(arr))
    n2=[v<3 for k,v in dd.items()]
    if not all(n2): return False
    uniq=[arr[i] != arr[i-1] for i in range(1,ll)]
    if arr == sorted(arr) and all(uniq): return False
    if arr == sorted(arr, reverse=True) and all(uniq): return False

    mmax=max(arr)
    if arr.count(mmax)>1: return False
    ind=arr.index(mmax)
    l=arr[:ind+1]
    r=arr[ind:]
    ul = [l[i] > l[i - 1] for i in range(1,len(l))]
    ur = [r[i] < r[i - 1] for i in range(1, len(r))]
    if not(all(ul)) or not(all(ur)): return False
    return True

# Runtime 145 ms Beats 70.14% of users with Python
# Memory 12.91 MB Beats 52.37% of users with Python

def validMountainArray(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    ll=len(arr)
    if ll<3: return False
    elif ll==3: return arr[0]<arr[1]>arr[2]

    mmax=max(arr)
    if arr.count(mmax)>1: return False
    ind=arr.index(mmax)
    if ind == 0 or ind == ll - 1: return False
    l=arr[:ind+1]
    r=arr[ind:]
    ul = [l[i] > l[i - 1] for i in range(1,len(l))]
    ur = [r[i] < r[i - 1] for i in range(1, len(r))]
    if not(all(ul)) or not(all(ur)): return False
    return True



print(validMountainArray([6,7,7,8,6]))
# s=[1,2,3,4,4,1, 0]
# mmax=max(s)
# print(s.count(mmax)>1)