"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/description/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

# Runtime 33 ms Beats 52.42% of users with Python
# Memory 13.42 MB Beats 41.11% of users with Python

from string import ascii_lowercase
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    # 2023_Алгоритмы С примерами на Python_Хайнеман.pdf
    # стр. 45, Пример 1.8
    def is_palindrome1(w):
        """Сделаем секцию, содержащую все символы в обратном порядке, и проверим ее на наличие w"""
        return w[::-1] == w

    ns = s.lower()
    a = ascii_lowercase + '0123456789'
    ns = ''.join([s1 for s1 in ns if s1 in a])
    if len(ns) == 1:
        return True
    else:
        return is_palindrome1(ns)


print(isPalindrome("0P"))