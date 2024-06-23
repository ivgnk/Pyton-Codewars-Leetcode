"""
Done 23.06.2024. Topics: String
500. Keyboard Row
https://leetcode.com/problems/keyboard-row

Given an array of strings words,
return the words that can be typed using letters of the alphabet on only one row
of American keyboard like the image below.

In the American keyboard:
the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Example 1:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]

Example 2:
Input: words = ["omk"]
Output: []

Example 3:
Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]

words[i] consists of English letters (both lowercase and uppercase).
"""

# Runtime 21 ms Beats 12.05%
# Memory 11.82 MB Beats 17.32%
# Runtime 13 ms Beats 61.97%
# Memory 11.70 MB Beats 49.58%
# Runtime 7 ms Beats 95.25%
# Memory 11.55 MB Beats 81.83%

r1="qwertyuiopQWERTYUIOP"
r2="asdfghjklASDFGHJKL"
r3="zxcvbnmZXCVBNM"

def findWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    res=[]
    for w1 in words:
        if all([w2 in r1 for w2 in w1]) or all([w2 in r2 for w2 in w1]) or all([w2 in r3 for w2 in w1]):
            res.append(w1)
    return res

print(findWords(["Hello","Alaska","Dad","Peace"]))
