"""
Done 24.09.2024. Topics: Hash Table, String
1496. Path Crossing
https://leetcode.com/problems/path-crossing/description/

Given a string path, where path[i] = 'N', 'S', 'E' or 'W',
each representing moving one unit north, south, east, or west, respectively.
You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
Return true if the path crosses itself at any point, that is,
if at any time you are on a location you have previously visited. Return false otherwise.

Example 1:
Input: path = "NES"
Output: false
Explanation: Notice that the path doesn't cross any point more than once.

Example 2:
Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.

Constraints:
1 <= path.length <= 10**4
path[i] is either 'N', 'S', 'E', or 'W'.

Hint 1
Simulate the process while keeping track of visited points.
Hint 2
Use a set to store previously visited points.
"""
# Time Complexity O(N)
# Space Complexity O(N)
# Runtime 11 ms Beats 78.20%
# Memory 11.78 MB Beats 76.50%
def isPathCrossing(path):
    """
    :type path: str
    :rtype: bool
    """
    x=0; y=0
    ss={(x,y)}
    for s in path:
        if s=='N': y+=1
        elif s=='S': y-=1
        elif s=='W': x-=1
        elif s=='E': x+=1
        d=(x,y)
        if d in ss: return True
        else: ss.add(d)
    return False

print(isPathCrossing("NES"))
print(isPathCrossing("NESWW"))

