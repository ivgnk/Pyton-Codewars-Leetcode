'''
383. Ransom Note
https://leetcode.com/problems/ransom-note/description/

Given two strings ransomNote and magazine,
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
'''

# Runtime 48 ms Beats 81.94% of users with Python3
# Memory 16.83 MB Beats 20.92% of users with Python3

# Runtime 66 ms Beats 27.45% of users with Python
# Memory 11.76 MB Beats 77.51% of users with Python

from collections import Counter
def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    da = dict(Counter(ransomNote))
    db = dict(Counter(magazine))
    for k, v in da.items():
        if k not in db: return False
        if da[k] > db[k]: return False
    print(da, db)
    return True
