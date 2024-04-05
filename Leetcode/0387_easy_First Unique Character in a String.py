'''
387. First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string/description/

Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
'''

# Runtime 146 ms Beats 36.59% of users with Python
# Memory 12.58 MB Beats 62.72% of users with Python

from collections import Counter
def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    d = dict(Counter(s))
    for i,s1 in enumerate(s):
        if d[s1]==1: return i
    return -1
    # d2=sorted(d.items(),key=lambda x: x[1])

print(firstUniqChar("leetcode"))