"""
Done 09.05.2024. Topics: Hash Table, String
1935. Maximum Number of Words You Can Type
There is a malfunctioning keyboard where some letter keys do not work.
All other keys on the keyboard work properly.
Given a string text of words separated by a single space (no leading or trailing spaces)
and a string brokenLetters of all distinct letter keys that are broken,
return the number of words in text you can fully type using this keyboard.

Example 1:
Input: text = "hello world", brokenLetters = "ad"
Output: 1
Explanation: We cannot type "world" because the 'd' key is broken.

Example 2:
Input: text = "leet code", brokenLetters = "lt"
Output: 1
Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.
"""

# Runtime 16 ms Beats 51.79% of users with Python
# Memory 12.13 MB Beats 13.10% of users with Python
def canBeTypedWords2(text, brokenLetters):
    """
    :type text: str
    :type brokenLetters: str
    :rtype: int
    """
    t2=text.split(); n=0
    for w in t2:
        if all([s1 not in brokenLetters for s1 in w]): n=n+1
    return n

# Runtime 10 ms Beats 92.26% of users with Python
# Memory 11.97 MB Beats 52.98% of users with Python
def canBeTypedWords(text, brokenLetters):
    return sum(all([s1 not in brokenLetters for s1 in w]) for w in text.split())

print(canBeTypedWords(text = "hello world", brokenLetters = "ad"))