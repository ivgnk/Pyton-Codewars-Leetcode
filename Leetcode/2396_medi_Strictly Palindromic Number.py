"""
Done 14.05.2024. Topics: Math, Two Pointers, Brainteaser

2396. Strictly Palindromic Number
An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive),
the string representation of the integer n in base b is palindromic.
Given an integer n, return true if n is strictly palindromic and false otherwise.
A string is palindromic if it reads the same forward and backward.

Example 1:
Input: n = 9
Output: false
Explanation: In base 2: 9 = 1001 (base 2), which is palindromic.
In base 3: 9 = 100 (base 3), which is not palindromic.
Therefore, 9 is not strictly palindromic so we return false.
Note that in bases 4, 5, 6, and 7, n = 9 is also not palindromic.

Example 2:
Input: n = 4
Output: false
Explanation: We only consider base 2: 4 = 100 (base 2), which is not palindromic.
Therefore, we return false.

Constraints:
4 <= n <= 105

Hint 1
Consider the representation of the given number in the base n - 2.
Hint 2
The number n in base (n - 2) is always 12, which is not palindromic.
"""

# Runtime 6 ms Beats 96.30% of users with Python
# Memory 11.58 MB Beats 77.37% of users with Python

def isStrictlyPalindromic(self, n):
    """
    :type n: int
    :rtype: bool
    """
    return False