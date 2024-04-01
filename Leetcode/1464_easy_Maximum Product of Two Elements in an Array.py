'''
1464. Maximum Product of Two Elements in an Array
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/

Given the array of integers nums, you will choose two different indices i and j of that array.
Return the maximum value of (nums[i]-1)*(nums[j]-1).
'''


def maxProduct2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll=len(nums)
    if ll==2: return (nums[0]-1)*(nums[1]-1)
    mmax=-10000
    for i in range(ll):
        for j in range(1,ll):
            if i!=j:
                pr=(nums[i]-1)*(nums[j]-1)
                if pr>mmax: mmax=pr
    return mmax

from itertools import permutations, combinations

def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    p1 = list(combinations(nums, 2))
    mmax = -1000
    ss = [(p2[0] - 1) * (p2[1] - 1) for p2 in p1]
    return max(ss)


print(maxProduct([1,5,4,5]))