"""
Done 18.05.2024. Topics: Math
9. Palindrome Number
https://leetcode.com/problems/palindrome-number/description/

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""
# Runtime 42 ms Beats 51.02% of users with Python
# Memory 11.41 MB Beats 94.04% of users with Python
# Runtime 37 ms Beats 68.26% of users with Python
# Memory 11.48 MB Beats 94.04% of users with Python

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    s=str(x)
    return s==s[::-1]
