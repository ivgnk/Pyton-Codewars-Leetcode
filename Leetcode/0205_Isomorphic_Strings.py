'''
205. Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/description/

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
'''

import string
from copy import deepcopy
def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    llens = len(s)
    if llens != len(t): return False
    if llens == 1: return True
    sobr = string.printable
    ds = dict.fromkeys(sobr, 0)
    dt = dict.fromkeys(sobr, 0)
    for ss in s: ds[ss] = ds[ss] + 1
    for ss in t: dt[ss] = dt[ss] + 1
    a1 = True
    for i in range(llens):
        a1 = a1 and (ds[s[i]] == dt[t[i]])

    sets = set(s);    sett = set(t);    a21 = True
    if (sets == sett) and (len(sett) == 2):
        b0 = abs(ord(s[0]) - ord(t[0]))
        for i in range(1, llens):
            bi = abs(ord(s[i]) - ord(t[i]))
            a21 = a21 and (b0 == bi)

    return a1 and a21

    # for i in range(llens):
    #     alls = alls and (ds[s[i]] == dt[t[i]])
    # return alls

print(isIsomorphic("egg","add"))
print(isIsomorphic("abab","baba"))
print(isIsomorphic("bbbaaaba","aaabbbba"))