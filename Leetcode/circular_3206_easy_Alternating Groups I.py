"""
08.07.2024. Topics: Array

3206. Alternating Groups I
https://leetcode.com/problems/alternating-groups-i/description/

There is a circle of red and blue tiles. You are given an array of integers colors.
The color of tile i is represented by colors[i]:
colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
Every 3 contiguous tiles in the circle with alternating colors (the middle tile has a different color
from its left and right tiles) is called an alternating group.
Return the number of alternating groups.
Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

Example 1:
Input: colors = [1,1,1]
Output: 0

Example 2:
Input: colors = [0,1,0,0,1]
Output: 3

Constraints:
3 <= colors.length <= 100
0 <= colors[i] <= 1

Hint 1
For each tile, check that the previous and the next tile have different colors from that tile or not.
"""

# Runtime 34 ms Beats 100.00%
# Memory 11.46 MB Beats 100.00%

def numberOfAlternatingGroups(colors):
    """
    :type colors: List[int]
    :rtype: int
    """
    ll=len(colors)
    ssum=0
    for i in range(ll):
        if i==0:
            if colors[0]!=colors[-1] and colors[0]!=colors[1]:
                ssum=ssum+1
        elif i==ll-1:
            if colors[ll-1]!=colors[ll-2] and colors[ll-1]!=colors[0]:
                ssum=ssum+1
        else:
            if colors[i]!=colors[i-1] and colors[i]!=colors[i+1]:
                ssum=ssum+1
    return ssum

print(numberOfAlternatingGroups([1,1,1]))
print(numberOfAlternatingGroups([0,1,0,0,1]))




