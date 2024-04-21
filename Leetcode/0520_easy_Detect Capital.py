"""
520. Detect Capital
We define the usage of capitals in a word to be right when one of the following cases holds:
All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

Example 1:
Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false
"""

# Runtime 7 ms Beats 97.21% of users with Python
# Memory 11.68 MB Beats 57.84% of users with Python

def detectCapitalUse(word):
    """
    :type word: str
    :rtype: bool
    """
    if word == word.upper(): return True
    elif word == word.lower(): return True
    elif word == word.capitalize(): return True
    else: return False
