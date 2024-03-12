def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sss = [str(ss) for ss in nums]
    res = ''.join(sss)
    spl = res.split('0')
    llen = [len(ss) for ss in spl]
    return max(llen)
