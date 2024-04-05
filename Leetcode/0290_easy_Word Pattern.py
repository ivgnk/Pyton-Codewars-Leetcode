'''
290. Word Pattern
https://leetcode.com/problems/word-pattern/description/

Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
'''
import shlex


#  https://stackoverflow.com/questions/3199171/append-multiple-values-for-one-key-in-a-dictionary

# Runtime 6 ms Beats 95.30% of users with Python
# Memory 11.59 MB Beats 93.95% of users with Python

def wordPattern(pattern, s):
    """
    :type pattern: str
    :type s: str
    :rtype: bool
    """
    sp = set(pattern)
    s1 = s.split()
    ss = set(s1)
    if len(sp) == len(ss):  # and len(s1)==len(pattern)
        if len(pattern) != len(s1): return False
        patt_d = dict()
        s1 = s.split()
        for i, p in enumerate(pattern):
            if p in patt_d:
                patt_d[p].append(s1[i])
            else:
                patt_d[p] = [s1[i]]
        for p in pattern:
            if len(set(patt_d[p])) != 1 or len(set(patt_d[p])) == 0:
                return False
    else:
        return False
    return True


print(wordPattern(pattern = "abba", s = "dog cat cat dog"))