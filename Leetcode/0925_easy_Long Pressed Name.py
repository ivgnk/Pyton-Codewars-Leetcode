"""
Done 27.09.2024. 925. Long Pressed Name
https://leetcode.com/problems/long-pressed-name/description/

Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed,
and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name,
with some characters (possibly none) being long pressed.

Example 1:
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.

Example 2:
Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it was not in the typed output.

Solution
✏️ Python solution  with groupby and with Letter-by-letter comparison

Intuition
Use groupby

# Approach
- comparing the lengths of the parts
- compare letters in parts
"""

from collections import Counter
from icecream import ic

# Runtime 46 # ms Beats 6.11%
# Memory 16.84 MB Beats 6.19%
# Runtime 32 ms Beats 76.98%
# Memory 16.78 MB Beats 6.19%
from itertools import groupby
def isLongPressedName(name, typed):
    # Letter-by-letter comparison
    n11=[list(g) for k, g in groupby(name)] # [['v'], ['t'], ['k'], ['g'], ['n']]
    t11=[list(g) for k, g in groupby(typed)] # [['v'], ['t', 't'], ['k'], ['g'], ['n', 'n']]
    if len(n11)!=len(t11): return False
    for i in range(len(n11)):
        if len(n11[i])>len(t11[i]): return False
        if n11[i][0] != t11[i][0]: return False
    return True

def isLongPressedName2(name, typed):
    # 0 case = The first and last letters must match
    if (name[0] != typed[0]) or (name[-1] != typed[-1]): return False

    # 1 case = equal strings length
    ln1 = len(name);  lt1 = len(typed)
    if ln1 == lt1 and name != typed: return False

    # 2 case = equal dictionaries length
    dn = dict(Counter(name))
    dt = dict(Counter(typed))
    if len(dn) != len(dt): return False

    # 3 case = equal letters in dictionaries
    for k, v in dn.items():
        if k not in dt: return False

    # 4 case = сompare the number of each letter
    if any([dn[k] > dt[k] for k, v in dn.items()]): return False

    # 5 case = Letter-by-letter comparison
    n11=[list(g) for k, g in groupby(name)] # [['v'], ['t'], ['k'], ['g'], ['n']]
    t11=[list(g) for k, g in groupby(typed)] # [['v'], ['t', 't'], ['k'], ['g'], ['n', 'n']]
    if len(n11)!=len(t11): return False
    for i in range(len(n11)):
        if len(n11[i])>len(t11[i]): return False
    return True

# print(isLongPressedName(name = "xnhtq", typed = "xhhttqq"))
# print(isLongPressedName(name = "znxnorutzt", typed = "zznxxnnooruuzztt"))
# print(isLongPressedName(name = "leelee", typed = "lleeelee"))
# ic(isLongPressedName(name = "alex", typed = "aaleexeex"))
ic(isLongPressedName(name = "kpufanyrqqmtgxhyycltlnusyeyyqygwupcaagtkuqkwamvdsi",
typed = "kpuufaanyrqqqmttggxxhyyyycclttllnusyeyqqyggwuuppccaaaggtkkuuqkwwamvvddsii"))

# not work
def isLongPressedName23(name, typed):
    """
    :type name: str
    :type typed: str
    :rtype: bool
    """
    # 0 case = The first and last letters must match
    if (name[0] != typed[0]) or (name[-1] != typed[-1]): return False

    # 1 case = equal strings length
    ln1 = len(name);  lt1 = len(typed)
    if ln1 == lt1 and name != typed: return False

    # 2 case = equal dictionaries length
    dn = dict(Counter(name))
    dt = dict(Counter(typed))
    if len(dn) != len(dt): return False

    # 3 case = equal letters in dictionaries
    for k, v in dn.items():
        if k not in dt: return False

    # 4 case = сompare the number of each letter
    if any([dn[k] > dt[k] for k, v in dn.items()]): return False

    ic('5 case')
    # 5 case = Letter-by-letter comparison
    typed2=list(typed)
    i=0; j=0
    while j<lt1 and i<ln1:
        # ic(i,j,name, typed2)
        if name[i]==typed2[j]:
            i+=1
            j+=1
        elif name[i-1]==typed2[j]:
            typed2.pop(j)
    else:
        if name[-1]==typed2[-1]==typed2[-2]: typed2.pop(-1)
    return ln1 == len(typed2)
