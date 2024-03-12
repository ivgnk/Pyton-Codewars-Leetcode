def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    while True:
        nnum = len(nums) // 2
        major = max(nums)
        num1 = nums.count(major)
        if num1>nnum:
            return major
        else:
            nums = [x for x in nums if x != major]

print(majorityElement([2,2,1,1,1,2,2]))