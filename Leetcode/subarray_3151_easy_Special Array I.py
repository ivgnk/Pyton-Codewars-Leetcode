"""
01.02.2025. Topics: Array
3151. Special Array I
https://leetcode.com/problems/special-array-i/description

An array is considered special if every pair of its adjacent elements
contains two numbers with different parity.

You are given an array of integers nums. Return true if nums is a special array,
otherwise, return false.

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

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100

Hint 1
Try to check the parity of each element and its previous element.
"""

def isArraySpecial(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    par=[n%2==0 for n in nums]
    return all(par[i]!=par[i-1] for i in range(1,len(nums)))

print(isArraySpecial(nums = [1]))
print(isArraySpecial([2,1,4]))
print(isArraySpecial([4,3,1,6]))
