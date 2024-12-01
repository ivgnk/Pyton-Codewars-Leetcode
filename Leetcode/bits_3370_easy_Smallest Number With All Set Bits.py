"""
3370. Smallest Number With All Set Bits
https://leetcode.com/problems/smallest-number-with-all-set-bits/description/

You are given a positive number n.
Return the smallest number x greater than or equal to n,
such that the binary representation of x contains only set bits.

A set bit refers to a bit in the binary representation of a number that has a value of 1.

Example 1:
Input: n = 5
Output: 7
Explanation:
The binary representation of 7 is "111".

Example 2:
Input: n = 10
Output: 15
Explanation:
The binary representation of 15 is "1111".

Example 3:
Input: n = 3
Output: 3
Explanation:
The binary representation of 3 is "11".

Constraints:
1 <= n <= 1000

Hint 1
Find the strictly greater power of 2, and subtract 1 from it.

My solution
https://leetcode.com/problems/smallest-number-with-all-set-bits/solutions/6099962/fast-and-easy-python-solution-for-problem-3370-based-on-hint/
✏️ Fast and easy Python solution for Problem 3370, based on hint

Intuition
Read hint

Approach
Done 01.12.2024

Complexity
Time complexity: O(1)
Space complexity: O(1)

Runtime 0 ms Beats 100.00%
Memory 17.34 MB Beats 100.00%
"""

class Solution:
    def smallestNumber(self, n: int) -> int:
        for i in range(12):
            if (r:=2**i)>n:
                return r-1
