class Solution(object):
    def twoSum(self, nums, target):
        # nums: List[int], target: int,   rtype: List[int]
        n = len(nums)
        res =[]
        for i in range(n):
            for j in range(i+1,n):
                if (nums[i]+nums[j]==target):
                    res.append(i); res.append(j)
                    return res
