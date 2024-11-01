"""
Done 01.11.2024. Topics: Array, Math, Number Theory
3334. Find the Maximum Factor Score of Array
https://leetcode.com/problems/find-the-maximum-factor-score-of-array
You are given an integer array nums.
The factor score of an array is defined as the product of the LCM and GCD of all elements of that array.
Return the maximum factor score of nums after removing at most one element from it.
Note that both the LCM and GCD of a single number are the number itself, and the factor score of an empty array is 0.

Example 1:
Input: nums = [2,4,8,16]
Output: 64
Explanation:
On removing 2, the GCD of the rest of the elements is 4 while the LCM is 16,
which gives a maximum factor score of 4 * 16 = 64.

Example 2:
Input: nums = [1,2,3,4,5]
Output: 60
Explanation:
The maximum factor score of 60 can be obtained without removing any elements.

Example 3:
Input: nums = [3]
Output: 9

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 30

Hint 1
Use brute force approach with two loops.
Hint 2
Optimize using prefix and suffix arrays.

My solution https://leetcode.com/problems/find-the-maximum-factor-score-of-array/solutions/5994131/easy-and-fast-27-ms-python3-solution-for-problem-3334/

Easy and fast(27 ms) Python3 solution for Problem 3334
Intuition
There are enough descriptions and examples.
Note: In the task description, lcm and gcd refer to the entire list, not to individual items. Use these functions from the math module with the appropriate call for the list.

I didn't need any Hints in poblem description.
Both hints are not needed at all
"""

from icecream import ic
from math import lcm, gcd
from copy import copy

# Runtime 31 ms Beats 88.13%
# Memory 16.66 MB Beats 86.20%
# Runtime 29 ms Beats 88.93%
# Memory 16.51 MB Beats 97.62%
# Runtime 27 ms Beats 91.42%
# Memory 16.63 MB Beats 86.20%
def maxScore(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    lcml=lcm(*nums)
    gcdl=gcd(*nums)
    maxprod=lcml*gcdl
    for i in range(len(nums)):
        tmp=nums.copy()
        tmp.pop(i)
        maxprod=max(maxprod,lcm(*tmp)*gcd(*tmp))
    return maxprod


if __name__=="__main__":
    print(maxScore([2,4,8,16]))
    print(maxScore([1,2,3,4,5]))
    print(maxScore([3]))
