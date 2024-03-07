'''
Given an unsorted integer array nums.
Return the smallest positive integer that is not present in nums.
You must implement an algorithm that runs in O(n)
time and uses O(1) auxiliary space.

Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
'''


def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    def func(elem):
        return elem>0

    nums.sort(); nnums=len(nums)
    if (nnums==1):
        if (nums[0]<1) or (nums[0]>1): return 1
        else: return 2

    if (nums[nnums-1]<0) or (nums[0]>1): return 1
    if nums[0]<1:
        arr = list(filter(func, nums))
        arr.sort(); narr = len(arr)
        print(arr)
        if (arr[0] > 1): return 1

        if (narr==2):
            if (arr[1]-arr[0])==1:
                return arr[1]+1
            else:
                return arr[0]+1

        for i in range(1,narr-1):
            if (arr[i]-arr[i-1])>1: return arr[i-1]+1
        return arr[narr-1]+1

    if nums[0]>0:
        if (nnums==2):
            if (nums[1]-nums[0])==1:
                return nums[1]+1
            else:
                return nums[0]+1

        for i in range(1,nnums):
            if (nums[i]-nums[i-1])>1: return nums[i-1]+1
        return nums[nnums-1]+1


print(firstMissingPositive([0,-1,3,1]))