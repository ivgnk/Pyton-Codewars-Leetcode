"""
Done 06.05.2024
2859. Sum of Values at Indices With K Set Bits
https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/description/

You are given a 0-indexed integer array nums and an integer k.
Return an integer that denotes the sum of elements in nums whose corresponding indices have exactly k set bits in their binary representation.
The set bits in an integer are the 1's present when it is written in binary.
For example, the binary representation of 21 is 10101, which has 3 set bits.

Example 1:
Input: nums = [5,10,1,5,2], k = 1
Output: 13
Explanation: The binary representation of the indices are:
0 = 0002
1 = 0012
2 = 0102
3 = 0112
4 = 1002
Indices 1, 2, and 4 have k = 1 set bits in their binary representation.
Hence, the answer is nums[1] + nums[2] + nums[4] = 13.

Example 2:
Input: nums = [4,3,2,1], k = 2
Output: 1
Explanation: The binary representation of the indices are:
0 = 002
1 = 012
2 = 102
3 = 112
Only index 3 has k = 2 set bits in its binary representation.
Hence, the answer is nums[3] = 1.
"""

# Runtime 53 ms Beats 70.63% of users with Python
# Memory 11.78 MB Beats 63.44% of users with Python

def sumIndicesWithKSetBits(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    s=[bin(i) for i in range(len(nums))]
    return sum([nums[i] for i,v in enumerate(s) if v.count('1')==k])

print((sumIndicesWithKSetBits(nums = [5,10,1,5,2], k = 1)))
