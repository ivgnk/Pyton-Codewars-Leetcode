"""
Done 18.05.2024. Topics: Array, Two Pointers, String

2108. Find First Palindromic String in the Array
https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/

Given an array of strings words, return the first palindromic string in the array.
If there is no such string, return an empty string "".
A string is palindromic if it reads the same forward and backward.

Example 1:
Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.

Example 2:
Input: words = ["notapalindrome","racecar"]
Output: "racecar"
Explanation: The first and only string that is palindromic is "racecar".

Hint 1
Iterate through the elements in order. As soon as the current element is a palindrome, return it.
Hint 2
To check if an element is a palindrome, can you reverse the string?
"""

# Runtime 49 ms Beats 71.71% of users with Python
# Memory 12.12 MB Beats 12.26% of users with Python

def firstPalindrome(words):
    """
    :type words: List[str]
    :rtype: str
    """
    for s in words:
        if s==s[::-1]: return s
    else: return ""