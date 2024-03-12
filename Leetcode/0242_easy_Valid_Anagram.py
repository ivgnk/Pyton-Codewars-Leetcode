'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''
import string

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    llens = len(s)

    if llens != len(t): return False
    sets = set(s)
    sett = set(t)
    if sets != sett: return False

    sobr = string.ascii_lowercase
    ds = dict.fromkeys(sobr, 0)
    dt = dict.fromkeys(sobr, 0)
    for ss in s: ds[ss] = ds[ss] + 1
    for ss in t: dt[ss] = dt[ss] + 1
    a1 = True
    for i in range(llens):
        a1 = a1 and (ds[s[i]] == dt[s[i]])

    return a1
