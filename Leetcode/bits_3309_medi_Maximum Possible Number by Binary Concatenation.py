"""
Done 10.10.2024. Topics: Array, Bit Manipulation
3309. Maximum Possible Number by Binary Concatenation
https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/description/

You are given an array of integers nums of size 3.
Return the maximum possible number whose binary representation can be formed
by concatenating the binary representation of all elements in nums in some order.

Note that the binary representation of any number does not contain leading zeros.

Example 1:
Input: nums = [1,2,3]
Output: 30
Explanation:
Concatenate the numbers in the order [3, 1, 2] to get the result "11110", which is the binary representation of 30.

Example 2:
Input: nums = [2,8,16]
Output: 1296
Explanation:
Concatenate the numbers in the order [2, 8, 16] to get the result "10100010000",
which is the binary representation of 1296.

Constraints:
nums.length == 3
1 <= nums[i] <= 127

Hint 1
How many possible concatenation orders are there?

According to given constraints brute force is working fine.
https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/description/comments/2661160

main tip
Convert each number in the array to its binary representation.
Try all possible permutations of the array to check which order gives the maximum concatenated binary value.
Convert the concatenated binary string back to a decimal number.
Return the maximum value.
https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/description/comments/2661271
"""

# Runtime 11 ms Beats 96.28%
# Memory 11.56 MB Beats 55.79%
from itertools import permutations
def maxGoodNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    lst=[bin(i)[2:] for i in nums]
    lst2=list(permutations(lst))
    lst3=['0b'+''.join(s) for s in lst2]
    lst4=[int(i, 2) for i in lst3]
    # print(lst)
    # print(lst2)
    # print(lst3)
    # print(lst4)
    return max(lst4)

print(maxGoodNumber([1,2,3]))
print(maxGoodNumber([2,8,16]))