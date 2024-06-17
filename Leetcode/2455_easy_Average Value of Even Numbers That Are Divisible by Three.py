"""
Done 17.06.2024. Topics: Array, Math
2455. Average Value of Even Numbers That Are Divisible by Three
https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.
Note that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.

Example 1:
Input: nums = [1,3,6,10,12,15]
Output: 9
Explanation: 6 and 12 are even numbers that are divisible by 3. (6 + 12) / 2 = 9.

Example 2:
Input: nums = [1,2,4,7,10]
Output: 0
Explanation: There is no single number that satisfies the requirement, so return 0.

Hint 1
What is the property of a number if it is divisible by both 2 and 3 at the same time?
Hint 2
It is equivalent to finding all the numbers that are divisible by 6.
"""

# Runtime 55 ms Beats 43.92%
# Memory 11.72 MB Beats 58.11%
# Runtime 50 ms Beats 78.38%
# Memory 11.66 MB Beats 82.43%

def averageValue(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nn = [n for n in nums if n % 6 == 0]
    ll = len(nn)
    if ll == 0: return 0
    else: return sum(nn) // ll