"""
Done 27.04.2024
350. Intersection of Two Arrays II
https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays
and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""
from collections import Counter

# Runtime 32 ms Beats 45.41% of users with Python
# Memory 12.18 MB Beats 10.24% of users with Python
# Runtime 27 ms Beats 71.45% of users with Python
# Memory 12.02 MB Beats 10.24% of users with Python

def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    nd1=dict(Counter(nums1));     nd2=dict(Counter(nums2))
    print(nd1, nd2)
    nd1l = sorted([[k,v] for k,v in nd1.items()]);     nd2l = sorted([[k,v] for k,v in nd2.items()])
    print(nd1l, nd2l)
    res=[]
    for k,v in nd1.items():
        if k in nd2:
          for j in range(min(nd1[k],nd2[k])):
              res.append(k)
    return res


# print(intersect(nums1 = [1,2,2,1], nums2 = [2,2]))
print(intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
