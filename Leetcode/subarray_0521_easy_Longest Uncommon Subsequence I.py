"""
Done 14.07.2024. Topics: String
521. Longest Uncommon Subsequence I

Given two strings a and b, return the length of the longest uncommon subsequence between a and b.
If no such uncommon subsequence exists, return -1.
An uncommon subsequence between two strings is a string that is a subsequence of exactly one of them.

Example 1:
Input: a = "aba", b = "cdc"
Output: 3
Explanation: One longest uncommon subsequence is "aba" because "aba" is a subsequence of "aba" but not "cdc".
Note that "cdc" is also a longest uncommon subsequence.

Example 2:
Input: a = "aaa", b = "bbb"
Output: 3
Explanation: The longest uncommon subsequences are "aaa" and "bbb".

Example 3:
Input: a = "aaa", b = "aaa"
Output: -1
Explanation: Every subsequence of string a is also a subsequence of string b.
Similarly, every subsequence of string b is also a subsequence of string a.
So the answer would be -1.

Hint 1
Think very simple.
Hint 2
If a == b, the answer is -1.
Hint 3
Otherwise, the answer is the string a or the string b.
"""

# Runtime 11 ms Beats 75.14%
# Memory 11.75 MB Beats 12.97%

def findLUSlength(a, b):
    """
    :type a: str
    :type b: str
    :rtype: int
    """
    if a == b:
        return -1
    else:
        return max(len(a), len(b))

