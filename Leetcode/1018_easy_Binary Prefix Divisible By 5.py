"""
Done 17.06.2024. Topics: Array, Bit Manipulation
1018. Binary Prefix Divisible By 5
You are given a binary array nums (0-indexed).
We define xi as the number whose binary representation is the subarray nums[0..i]
(from most-significant-bit to least-significant-bit).
For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
Return an array of booleans answer where answer[i] is true if xi is divisible by 5.

Example 1:
Input: nums = [0,1,1]
Output: [true,false,false]
Explanation: The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
Only the first number is divisible by 5, so answer[0] is true.

Example 2:
Input: nums = [1,1,1]
Output: [false,false,false]

Hint 1
If X is the first i digits of the array as a binary number,
then 2X + A[i] is the first i+1 digits.
"""

# Runtime 197 ms Beats 37.33%
# Memory 12.99 MB Beats 37.33%
# Runtime 193 ms Beats 44.00%
# Memory 12.79 MB Beats 40.00%
# Runtime 191 ms Beats 48.00%
# Memory 13.10 MB Beats 34.67%

def prefixesDivBy5_(nums):
    """
    :type nums: List[int]
    :rtype: List[bool]
    """
    res = []
    for i in range(len(nums)):
        if i == 0:
            x = nums[i]
        else:
            x = 2 * x + nums[i]
        res.append(x % 5 == 0)
    return res


# Runtime 196 ms Beats 37.33%
# Memory 13.16 MB Beats 25.33%
# Runtime 180 ms Beats 72.00%
# Memory 13.19 MB Beats 25.33%

def prefixesDivBy5(nums):
    """
    :type nums: List[int]
    :rtype: List[bool]
    """
    res = []; x=0
    for i in range(len(nums)):
        x = 2 * x + nums[i]
        res.append(x % 5 == 0)
    return res
