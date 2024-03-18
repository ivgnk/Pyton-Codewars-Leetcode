'''
Fix string case
https://www.codewars.com/kata/5b180e9fedaa564a7000009a/train/python

In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and
your task is to convert that string to either lowercase only or uppercase only based on:
make as few changes as possible.
if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
For example:
solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
solve("coDE") = "code". Upper == lowercase. Change all to lowercase.
'''

import string

def solve(s):
    llen = len(s)
    lc = sum([1 for ss in s if ss in string.ascii_lowercase]);
    uc = llen-lc
    if uc <= lc: return s.lower()
    else: return s.upper()

print(solve("CODe"))