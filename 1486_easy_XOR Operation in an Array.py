'''
You are given an integer n and an integer start.
Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.
Return the bitwise XOR of all elements of nums.

Example 1:
Input: n = 5, start = 0
Output: 8
Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.

Example 2:
Input: n = 4, start = 3
Output: 8
Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8
'''

# 10 ms Beats 89.58% of users with Python
# Memory 11.63 MB Beats 48.33% of users with Python
# https://lifewithdata.com/2023/08/26/leetcode-xor-operation-in-an-array-solution/

def xorOperation(n, start):
    """
    :type n: int
    :type start: int
    :rtype: int
    """
    nums = [start + 2 * i for i in range(n)]
    # print(nums)
    xor_result = 0
    for num in nums:
        xor_result ^= num
    return xor_result
