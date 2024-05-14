"""
Done 14.05.2024. Topics: Array, Hash Table
2610. Convert an Array Into a 2D Array With Conditions
https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/

You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.

Example 1:
Input: nums = [1,3,4,1,2,3,1]
Output: [[1,3,4,2],[1,3],[1]]
Explanation: We can create a 2D array that contains the following rows:
- 1,3,4,2
- 1,3
- 1
All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
It can be shown that we cannot have less than 3 rows in a valid array.

Example 2:
Input: nums = [1,2,3,4]
Output: [[4,3,2,1]]
Explanation: All elements of the array are distinct, so we can keep all of them in the first row of the 2D array.
"""

#  Wrong Answer -- 861 / 1035 testcases passed
from collections import Counter
def findMatrix2(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ll=len(nums); res=[[]];  j=0
    for i in range(ll):
        if nums[i] not in res[j]:
            res[j].append(nums[i])
        else:
            j=j+1
            res=res+[[nums[i]]]
    return res

# Runtime 33 ms Beats 56.38% of users with Python
# Memory 11.69 MB Beats 57.98% of users with Python
def findMatrix3(nums):
    dd=dict(Counter(nums))
    lst=sorted([[v,k] for k,v in dd.items()], reverse=True)
    nm=lst[0][0]; d=lst[0][1]; ll=len(lst)
    res=[[d]]*nm
    for i in range(1,ll):
        nm = lst[i][0]
        d = lst[i][1]
        for j in range(nm):
            res[j]=res[j]+[d]
    return res

# Runtime 31 ms Beats 70.21% of users with Python
# Memory 11.68 MB Beats 57.98% of users with Python
def findMatrix(nums):
    dd=dict(Counter(nums))
    lst=sorted([[v,k] for k,v in dd.items()], reverse=True)
    ll=len(lst)
    res=[[lst[0][1]]]*lst[0][0]
    for i in range(1,ll):
        nm = lst[i][0]
        d = lst[i][1]
        for j in range(nm):
            res[j]=res[j]+[d]
    return res


print(findMatrix([8,8,8,8,2,4,4,2,4]))