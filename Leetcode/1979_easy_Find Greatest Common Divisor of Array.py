"""
Done 19.06.2024. Topics: Math
1979. Find Greatest Common Divisor of Array
Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.
The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

Example 1:
Input: nums = [2,5,6,9,10]
Output: 2
Explanation:
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.

Example 2:
Input: nums = [7,5,6,8,3]
Output: 1
Explanation:
The smallest number in nums is 3.
The largest number in nums is 8.
The greatest common divisor of 3 and 8 is 1.

Example 3:
Input: nums = [3,3]
Output: 3
Explanation:
The smallest number in nums is 3.
The largest number in nums is 3.
The greatest common divisor of 3 and 3 is 3.

Hint 1
Find the minimum and maximum in one iteration. Let them be mn and mx.
Hint 2
Try all the numbers in the range [1, mn] and check the largest number which divides both of them.
"""

# Runtime 34 ms Beats 64.54%
# Memory 11.70 MB Beats 79.19%

def findGCD(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    mn=min(nums)
    mx=max(nums)
    for i in range(mn,0,-1):
        if mx%i==0 and mn%i==0: return i



