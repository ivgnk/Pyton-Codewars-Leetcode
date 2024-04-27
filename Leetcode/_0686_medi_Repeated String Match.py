"""
27.04.2024
686. Repeated String Match
Given two strings a and b, return the minimum number of times you should repeat string a
so that string b is a substring of it.
If it is impossible for b to be a substring of a after repeating it, return -1.

Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated 2 times is "abcabc".

Example 1:
Input: a = "abcd", b = "cdabcdab"
Output: 3
Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.

Example 2:
Input: a = "a", b = "aa"
Output: 2
"""

# Memory Limit Exceeded -- 57 / 59 testcases passed

from collections import Counter
def repeatedStringMatch(a, b):
    """
    :type a: str
    :type b: str
    :rtype: int
    """
    if a.count(b) > 0: return 1
    la = len(a);    lb = len(b)
    print(la, lb)
    ba = b.count(a)
    if ba > 0 and ba * la == lb: return b.count(a)
    ca = Counter(a);    cb = Counter(b)
    sa = set(ca);    a_ = sorted(list(sa))
    sb = set(cb);    b_ = sorted(list(sb))
    print(ca)
    print(cb)
    if a_ != b_:
        if not sb.issubset(sa): return -1
    elif b.count(a) == lb:
        return b.count(a)
    nn = 1;    a1 = a
    for i in range(1, la * lb):
        if a1.find(b) > -1: return nn
        if len(a1) > lb * 2 and la < lb: return -1
        a1 = a1 + a;        nn += 1
    return -1

