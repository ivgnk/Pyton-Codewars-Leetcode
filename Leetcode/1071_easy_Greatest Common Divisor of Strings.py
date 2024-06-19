"""
Done 19.06.2024. Topics: Math, String
1071. Greatest Common Divisor of Strings
https://leetcode.com/problems/greatest-common-divisor-of-strings/description/

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t
(i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

Hint 1
The greatest common divisor must be a prefix of each string, so we can try all prefixes.
"""

# Runtime 39 ms Beats 40.80%
# Memory 16.60 MB Beats 20.09%
# Runtime 33 ms Beats 78.32%
# Memory 16.51 MB Beats 53.66%
# https://leetcode.com/problems/greatest-common-divisor-of-strings/solutions/5329297/python-solution-without-using-gcd-function-like-a-sane-person/

def gcdOfStrings(self, str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""
    str1, str2 = (str1, str2) if len(str2) < len(str1) else (str2, str1)
    for i in range(len(str2)):
        temp = str2[:len(str2) - i]
        if temp * int(len(str1) / len(temp)) == str1 and temp * int(len(str2) / len(temp)) == str2:
            return temp


# Runtime 43 ms Beats 20.47%
# Memory 16.75 MB Beats 6.45%
# Runtime 44 ms Beats 17.05%
# Memory 16.62 MB Beats 20.09%
# Runtime 41 ms Beats 29.76%
# Memory 16.61 MB Beats 20.09%
from collections import Counter
from math import gcd
def gcdOfStrings3(self, str1: str, str2: str) -> str:
    if str1[0] == str2[0]:
        prf = str1[0]
    else:
        return ""
    dd1 = dict(Counter(str1))
    dd2 = dict(Counter(str2))
    if len(dd1) != len(dd2): return ""

    l1 = len(str1);    l2 = len(str2)
    mil = min(l1, l2);    mal = max(l1, l2)
    ll = gcd(mil, mal)

    for i in range(1, ll):
        if str1[i] == str2[i]:
            prf += str1[i]
        else:
            break
    if prf * (l1 // ll) == str1 and prf * (l2 // ll) == str2:
        return prf
    else:
        return ""

# on the base of
# https://leetcode.com/problems/greatest-common-divisor-of-strings/solutions/5329349/easy-beginner-friendly-solution/
# Runtime 46 ms Beats 12.50%
# Memory 16.53 MB Beats 53.66%
# Runtime 41 ms Beats 29.76%
# Memory 16.55 MB Beats 53.66%

from icecream import ic
def gcdOfStrings2(str1, str2):
    """
    :type str1: str
    :type str2: str
    :rtype: str
    """
    if str1[0] != str2[0]: return ""

    l1 = len(str1);    l2 = len(str2)
    mil = min(l1, l2);    mal = max(l1, l2)
    ll = gcd(mil, mal)

    prf=""; res=[""]

    for i in range(ll):
        if str1[i]==str2[i]:
            prf = prf+str1[i]
            i1=i+1
            if prf*(l1//i1)==str1 and prf*(l2//i1)==str2:
                res.append(prf)
    return res[-1]

ic(gcdOfStrings2(str1 = "ABCABC", str2 = "ABC"))
ic(gcdOfStrings2(str1 = "ABABAB", str2 = "ABAB")) # AB
ic(gcdOfStrings2(str1 = "ABCABCABC", str2 = "ABCAAA"))

