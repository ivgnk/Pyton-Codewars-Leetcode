def triangleType(nums):
    """
    :type nums: List[int]
    :rtype: str
    """
    if nums[0]+nums[1]>nums[2] and nums[1]+nums[2]>nums[0] and nums[0]+nums[2]>nums[1]:
        if nums[0]==nums[1] and nums[1]==nums[2]: return "equilateral"
        if nums[0]!=nums[1] and nums[0]!=nums[2] and nums[1]!=nums[2]: return "scalene"
        return "isosceles"
    else: return "none"