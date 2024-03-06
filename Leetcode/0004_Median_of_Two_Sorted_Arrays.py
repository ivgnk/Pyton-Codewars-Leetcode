import numpy as np

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    n = nums1+nums2
    a = np.array(n)
    return np.median(a)

print(findMedianSortedArrays([1,3],[2]))