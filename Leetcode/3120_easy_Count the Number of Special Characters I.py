"""
3120. Count the Number of Special Characters I
You are given a string word. A letter is called special
if it appears both in lowercase and uppercase in word.
Return the number of special letters in word.

Example 1:
Input: word = "aaAbcBC"
Output: 3
Explanation:
The special characters in word are 'a', 'b', and 'c'.

Example 2:
Input: word = "abc"
Output: 0
Explanation:
No character in word appears in uppercase.

Example 3:
Input: word = "abBCab"
Output: 1
Explanation:
The only special character in word is 'b'
"""
from icecream import ic
from collections import Counter

# Runtime 19 ms Beats 100.00% of users with Python
# Memory 11.72 MB Beats 100.00% of users with Python

def numberOfSpecialChars(word):
    """
    :type word: str
    :rtype: int
    """
    dd=dict(Counter(word))
    n = 0
    for k,v in dd.items():
        if ord(k)<91:
            if chr(ord(k)+32) in dd:
                n=n+1
    return n



ic(numberOfSpecialChars("aaAbcBC"))
# for i in range(65,91):
#     print(chr(i),chr(i+32))
