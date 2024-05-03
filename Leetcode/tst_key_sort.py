"""
Как на Python Сделать свою сортировку?
https://qna.habr.com/q/459686
"""
from functools import cmp_to_key

def srt_rev(a, b):
    if a > b:
        return -1
    elif a < b:
        return 1
    else:
        return 0

def srt_prj(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


s=[1,1,2,2,2,3]
s1 = sorted(s, reverse=True)
print(sorted(s, key=cmp_to_key(srt_rev)))
print(sorted(s1, key=cmp_to_key(srt_prj)))