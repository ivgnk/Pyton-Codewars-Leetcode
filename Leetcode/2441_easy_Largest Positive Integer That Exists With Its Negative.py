def findMaxK(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if 0 in nums: return -1
    nums.sort(reverse=True)
    # print(nums)
    for i in nums:
        if -i in nums: return i
    return -1

# print(findMaxK([-1,2,-3,3]))
print(findMaxK([-10,8,6,7,-2,-3]))