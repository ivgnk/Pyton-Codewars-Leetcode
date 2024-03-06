import numpy as np

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    a = np.array(nums1+nums2)
    return np.median(a)

print(findMedianSortedArrays([1,3],[2]))