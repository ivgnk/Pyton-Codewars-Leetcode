"""
Done 28.06.2024. Topics: Math
2119. A Number After a Double Reversal
https://leetcode.com/problems/a-number-after-a-double-reversal/description/

Reversing an integer means to reverse all its digits.
For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not retained.
Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2.
Return true if reversed2 equals num. Otherwise return false.

Example 1:
Input: num = 526
Output: true
Explanation: Reverse num to get 625, then reverse 625 to get 526, which equals num.

Example 2:
Input: num = 1800
Output: false
Explanation: Reverse num to get 81, then reverse 81 to get 18, which does not equal num.

Example 3:
Input: num = 0
Output: true
Explanation: Reverse num to get 0, then reverse 0 to get 0, which equals num.
"""

# Runtime 15 ms Beats 44.61%
# Memory 11.40 MB Beats 99.26%
# Runtime 8 ms Beats 88.10%
# Memory 11.72 MB Beats 25.28%

def isSameAfterReversals(num):
    """
    :type num: int
    :rtype: bool
    """
    if num==0: return True
    else: return not num%10==0

