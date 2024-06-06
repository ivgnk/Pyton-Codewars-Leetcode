"""
Done 06.06.2024. Topics: Array, Hash Table, Greedy, Sorting
846. Hand of Straights
https://leetcode.com/problems/hand-of-straights/description/

Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize,
and consists of groupSize consecutive cards.
Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize,
return true if she can rearrange the cards, or false otherwise.

Example 1:
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

Example 2:
Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.

test case: [2,1] 2
I think it should return false, but expected true;
The question is confusing. You don't need 2 groups if W=2. Only size of group needs to be 2. There can be any number of groups.
Other main condition is, numbers in groups should be consecutive i.e. nextNumber = prevNumber + 1 in each group.
https://leetcode.com/problems/hand-of-straights/description/comments/1734657
"""

from collections import Counter
# https://leetcode.com/problems/hand-of-straights/solutions/684392/yet-another-python-solution-99/
# Runtime 161 ms Beats 64.60% of users with Python3
# Memory 18.10 MB Beats 94.17% of users with Python3

def isNStraightHand(hand, W):
    counter = Counter(hand)
    for num in sorted(counter):
        if counter[num]:
            val = counter[num]
            for i in range(W):
                counter[num + i] -= val
                if counter[num + i] < 0:
                    return False
    return True

# Runtime 493 ms Beats 9.30% of users with Python
# Memory 12.94 MB Beats 95.35% of users with Python

def isNStraightHand(hand, groupSize):
    if groupSize == 1: return True
    ll = len(hand)
    if ll % groupSize != 0: return False
    h = sorted(hand)
    ngr = ll // groupSize
    print('in')
    for i in range(ngr):
        ini = h[0]
        h.remove(ini)
        for j in range(1, groupSize):
            if ini + 1 in h:
                ini = ini + 1
                h.remove(ini)
            else:
                return False
        h = sorted(h)
    return True


print(isNStraightHand(hand = [3,2,4,3], groupSize = 2))
