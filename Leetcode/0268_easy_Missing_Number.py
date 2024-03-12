def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    llen = len(nums)
    mmax = max(nums)
    if llen == mmax + 1: return mmax + 1
    seti = set(nums)
    setf = set([i for i in range(mmax+1)])
    n = list(setf-seti)
    return n[0]

print(missingNumber([3,0,1]))