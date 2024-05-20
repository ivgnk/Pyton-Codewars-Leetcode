"""
Done 20.05.2024.
3151. Special Array I
https://leetcode.com/problems/special-array-i/description/

An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integers nums.
Return true if nums is a special array, otherwise, return false.

Example 1:
Input: nums = [1]
Output: true
Explanation:
There is only one element. So the answer is true.

Example 2:
Input: nums = [2,1,4]
Output: true
Explanation:
There is only two pairs: (2,1) and (1,4), and both of them contain numbers with different parity. So the answer is true.

Example 3:
Input: nums = [4,3,1,6]
Output: false
Explanation:
nums[1] and nums[2] are both odd. So the answer is false.
"""

# Runtime 36 ms Beats 100.00% of users with Python
# Memory 11.71 MB Beats 100.00% of users with Python

def isArraySpecial(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    ll=len(nums)
    if ll==1: return True
    if nums[0] % 2==0:
        print('even')
        ne=all([nums[i]%2==0 for i in range(0,ll,2)])
        no=all([nums[i]%2!=0 for i in range(1,ll,2)])
    else:
        ne=all([nums[i]%2==0 for i in range(1,ll,2)])
        no=all([nums[i]%2!=0 for i in range(0,ll,2)])
    print(ne)
    print(no)
    return ne and no

print(isArraySpecial([4,3,1,6]))