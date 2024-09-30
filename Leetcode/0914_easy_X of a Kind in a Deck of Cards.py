"""
Done 01.10.2024. Topics: Hash Table
914. X of a Kind in a Deck of Cards
You are given an integer array deck where deck[i] represents the number written on the ith card.
Partition the cards into one or more groups such that:

Each group has exactly x cards where x > 1, and
All the cards in one group have the same integer written on them.
Return true if such partition is possible, or false otherwise.

Example 1:
Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].

Example 2:
Input: deck = [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.

Constraints:
1 <= deck.length <= 10**4
0 <= deck[i] < 10**4

My solution
✏️ Not quite simple Python solution based on dictionaty, set and math.gcd
Intuition
1) Use dictionary and set for calculate the number of instances of each number
2) Use math.gcd because there may be several lists with the same numbers
3) Сonsider extreme cases
https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/solutions/5853751/not-quite-simple-python-solution-based-on-dictionaty-set-and-math-gcd/
"""
# Runtime
# 103 ms Beats 93.50%
# Memory 16.92 MB Beats 25.91%
from math import gcd
def hasGroupsSizeX(deck):
    """
    :type deck: List[int]
    :rtype: bool
    """
    if len(deck) == 1: return False
    dd=dict()
    for s in deck:
        if s in dd:
            dd[s]+=1
        else:
            dd[s]=1

    va = {v for v in dd.values()}
    if len(va)==1: return True
    mmin=min(va)
    if mmin==1: return False
    va_l=list(va)
    return gcd(*va_l)>1
    # %mmin !=0 - for case [1,1,2,2,2,2]
    if va[0]%mmin !=0: return False

    for i in range(1,len(va)):
        if va[i]%mmin !=0: return False
    else: return True

# print(hasGroupsSizeX([1,2,3,4,4,3,2,1]))
# print(hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3]))
# a=list({2,4,6,8})
# print(gcd(*a))

# Wrong Answer - 46 / 75 testcases passed
# deck = [1,1,1,1,2,2,2,2,2,2]
# Output false
# Expected true
def hasGroupsSizeX3(deck):
    """
    :type deck: List[int]
    :rtype: bool
    """
    if len(deck) == 1: return False
    dd=dict()
    for s in deck:
        if s in dd:
            dd[s]+=1
        else:
            dd[s]=1

    va = [v for v in dd.values()]
    mmin=min(va)
    # %mmin !=0 - for case [1,1,2,2,2,2]
    if va[0]%mmin !=0: return False

    for i in range(1,len(va)):
        if va[i]%mmin !=0: return False
    else: return True

