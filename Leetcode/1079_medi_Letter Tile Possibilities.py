"""
Done 29.05.2024. Topics: Hash Table, String, Backtracking, Counting
1079. Letter Tile Possibilities
https://leetcode.com/problems/letter-tile-possibilities/description/

You have n  tiles, where each tile has one letter tiles[i] printed on it.
Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

Example 1:
Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:
Input: tiles = "AAABBC"
Output: 188

Example 3:
Input: tiles = "V"
Output: 1
"""
from collections import Counter
from itertools import permutations


# Runtime 26 ms Beats 94.29% of users with Python
# Memory 12.81 MB Beats 54.29% of users with Python
# https://leetcode.com/problems/letter-tile-possibilities/solutions/2835607/simple-4-lines-beginner-friendly-solution/
def numTilePossibilities(tiles: str) -> int:
    n = len(tiles)
    tiles = list(tiles)
    s1 = set()
    for i in range(1, n + 1):
        s1.update(permutations(tiles, i))
    return len(s1)

# Runtime 95 ms Beats 31.43% of users with Python
# Memory 14.33 MB Beats 30.00% of users with Python

def numTilePossibilities2(self, tiles):
    """
    :type tiles: str
    :rtype: int
    """
    ll = len(tiles)
    if ll == 1:
        return 1
    else:
        sset = set(); ssum = len(Counter(tiles))
        # print(ssum)
        for i in range(2, ll + 1):
            lst = list(permutations(tiles, i))
            for i in lst:
                sset.add(''.join([s for s in i]))
        return ssum + len(sset)


# Runtime 102 ms Beats 21.43% of users with Python
# Memory 14.64 MB Beats 30.00% of users with Python
# Runtime 96 ms Beats 28.57% of users with Python
# Memory 14.52 MB Beats 30.00% of users with Python

def numTilePossibilities3(tiles):
    """
    :type tiles: str
    :rtype: int
    """
    ll=len(tiles)
    if ll==1: return 1
    else:
        sset=set(); ssum=len(Counter(tiles))
        # print(ssum)
        for i in range(2,ll+1):
            lst=list(permutations(tiles,i))
            lst2=[''.join([s for s in i]) for i in lst]
            # print(i,lst2)
            for j in lst2:
                sset.add(j)
        return ssum+len(sset)

print(numTilePossibilities("AAB"))