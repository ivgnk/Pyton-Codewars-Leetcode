"""
Re-solution 11.05.2024. Topics: Array, Sorting
1200. Minimum Absolute Difference
https://leetcode.com/problems/minimum-absolute-difference/description/

Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr

Example 1:
Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

Example 2:
Input: arr = [1,3,6,10,15]
Output: [[1,3]]

Example 3:
Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]

Hint 1
Find the minimum absolute difference between two elements in the array.
Hint 2
The minimum absolute difference must be a difference between two consecutive elements in the sorted array.
"""

# Runtime 264 ms Beats 48.39% of users with Python3
# Memory 31.11 MB Beats 60.33% of users with Python3
# Runtime 255 ms Beats 70.62% of users with Python3
# Memory 31.10 MB Beats 82.48% of users with Python3
# Runtime 248 ms Beats 86.25% of users with Python3
# Memory 31.21 MB Beats 43.91% of users with Python3
def minimumAbsDifference(arr):
    """
    :type arr: List[int]
    :rtype: List[List[int]]
    """
    arr=sorted(arr); ll1=len(arr)-1
    rr=[abs(arr[i]-arr[i+1]) for i in range(ll1) ]
    mm=min(rr)
    return [[arr[i],arr[i+1]] for i,r2 in enumerate(rr) if r2[1]==mm]



# Runtime 315 ms Beats 7.78% of users with Python3
# Memory 47.24 MB Beats 5.03% of users with Python3
def minimumAbsDifference3(arr):
    """
    :type arr: List[int]
    :rtype: List[List[int]]
    """
    arr=sorted(arr); ll1=len(arr)-1; mmin =1e38
    r1=[]
    i=0
    rr=[abs(arr[i]-arr[i+1]) for i in range(ll1) ]
    while i<ll1:
        mmin = min(mmin,rr[i])
        r1.append([[arr[i],arr[i+1]],rr[i]])
        i=i+1
    return [r2[0] for r2 in r1 if r2[1]==mmin]


# Runtime 363 ms Beats 9.62% of users with Python
# Memory 43.92 MB Beats 5.35% of users with Python
def minimumAbsDifference2(arr):
    """
    :type arr: List[int]
    :rtype: List[List[int]]
    """
    arr=sorted(arr); ll=len(arr); mmin =1e38
    r1=[]
    for i in range(ll-1):
        s=abs(arr[i]-arr[i+1])
        mmin = min(mmin,s)
        r1.append([[arr[i],arr[i+1]],s])
    return [r2[0] for r2 in r1 if r2==mmin]


# print(minimumAbsDifference([4,2,1,3]))
# print(minimumAbsDifference([1,3,6,10,15]))
print(minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))