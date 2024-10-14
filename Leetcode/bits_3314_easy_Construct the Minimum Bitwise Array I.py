"""
Done 14.10.2024.
3314. Construct the Minimum Bitwise Array I
https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/description/

You are given an array nums consisting of n prime integers.
You need to construct an array ans of length n, such that, for each index i,
the bitwise OR of ans[i] and ans[i] + 1 is equal to nums[i],
i.e. ans[i] OR (ans[i] + 1) == nums[i].

Additionally, you must minimize each value of ans[i] in the resulting array.
If it is not possible to find such a value for ans[i] that satisfies the condition,
then set ans[i] = -1.

Example 1:
Input: nums = [2,3,5,7]
Output: [-1,1,4,3]
Explanation:
For i = 0, as there is no value for ans[0] that satisfies ans[0] OR (ans[0] + 1) = 2, so ans[0] = -1.
For i = 1, the smallest ans[1] that satisfies ans[1] OR (ans[1] + 1) = 3 is 1, because 1 OR (1 + 1) = 3.
For i = 2, the smallest ans[2] that satisfies ans[2] OR (ans[2] + 1) = 5 is 4, because 4 OR (4 + 1) = 5.
For i = 3, the smallest ans[3] that satisfies ans[3] OR (ans[3] + 1) = 7 is 3, because 3 OR (3 + 1) = 7.

Example 2:
Input: nums = [11,13,31]
Output: [9,12,15]
Explanation:
For i = 0, the smallest ans[0] that satisfies ans[0] OR (ans[0] + 1) = 11 is 9, because 9 OR (9 + 1) = 11.
For i = 1, the smallest ans[1] that satisfies ans[1] OR (ans[1] + 1) = 13 is 12, because 12 OR (12 + 1) = 13.
For i = 2, the smallest ans[2] that satisfies ans[2] OR (ans[2] + 1) = 31 is 15, because 15 OR (15 + 1) = 31.

Constraints:
1 <= nums.length <= 100
2 <= nums[i] <= 1000
nums[i] is a prime number.

Hint 1
The constraints are small, allowing you to iterate over all potential values for ans[i] directly.

My solution
✏️ Easy Python brute force solution, based on Hint 1
Intuition
Hint 1
The constraints are small, allowing you to iterate over all potential values for ans[i] directly.

Read: Python Bitwise Operators
https://www.geeksforgeeks.org/python-bitwise-operators/

Approach
Use cycle from 0 to 999
"""

# Runtime 219 ms Beats 100.00%
# Memory 11.72 MB Beats 100.00%

# Python Bitwise Operators
# https://www.geeksforgeeks.org/python-bitwise-operators/
def minBitwiseArray(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans=[]
    for n in nums:
        for i in range(1000):
            if i | (i+1)==n:
                ans.append(i)
                break
        else: ans.append(-1)
    return ans

print(minBitwiseArray([2,3,5,7]))
print(minBitwiseArray([11,13,31]))