import numpy as np

def minOperations2(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    n1 = sorted(nums)
    nn1 = np.array(n1)
    n = nn1[nn1 < k]
    return len(n)

def minOperations1(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    n1 = sorted(nums)
    for i,s in enumerate(n1):
        if s>=k: return i

