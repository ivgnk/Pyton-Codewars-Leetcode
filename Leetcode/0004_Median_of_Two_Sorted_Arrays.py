"""
Redone 29.10.2024. Topics: Array, Binary Search, Divide and Conquer
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""
import numpy as np

def findMedianSortedArrays2(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    a = np.array(nums1+nums2)
    return np.median(a)

# Runtime 3 ms Beats 53.18%
# Memory 16.72 MB Beats 93.68%
def findMedianSortedArrays(nums1, nums2):
    a = sorted(nums1 + nums2)
    if (ll:=len(a)) == 1: return a[0]
    ll2 = ll // 2
    if len(a) % 2 == 0:
        return (a[ll2 - 1] + a[ll2]) / 2
    else:
        return float(a[ll2])

# print(findMedianSortedArrays([1,3],[2]))
print(findMedianSortedArrays(nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10,11,12,13,14,15,16,17]))