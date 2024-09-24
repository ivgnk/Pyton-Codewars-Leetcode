"""
Done 24.09.2024. Topics: Stack
Topics: Depth-First Search, Breadth-First Search, Graph
841. Keys and Rooms
https://leetcode.com/problems/keys-and-rooms/description/

There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0.
Your goal is to visit all the rooms.
However, you cannot enter a locked room without having its key.
When you visit a room, you may find a set of distinct keys in it. Each key has a number on it,
denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.
Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i,
return true if you can visit all the rooms, or false otherwise.

Example 1:
Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation:
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.

Example 2:
Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.

Constraints:
n == rooms.length
2 <= n <= 1000
0 <= rooms[i].length <= 1000
1 <= sum(rooms[i].length) <= 3000
0 <= rooms[i][j] < n
All the values of rooms[i] are unique.
"""

# Runtime 103 ms Beats 5.07%
# Memory 12.04 MBBeats 93.55%
def canVisitAllRooms2(rooms):
    """
    :type rooms: List[List[int]]
    :rtype: bool
    """
    llen=len(rooms)
    keys=[0]; lk=len(keys)
    while lk !=llen:
        curr=keys; prev=lk
        for s in curr:
            for dd in rooms[s]:
                if dd not in keys:
                    keys.append(dd)
                    lk+=1
        if prev==lk:
            return lk==llen
    return lk==llen

# Runtime 104 ms Beats 5.07%
# Memory 12.07 MB Beats 93.55%
def canVisitAllRooms3(rooms):
    """
    :type rooms: List[List[int]]
    :rtype: bool
    """
    llen=len(rooms)
    keys=[0]; lk=len(keys)
    newkey=keys
    while lk !=llen:
        curr=newkey
        prev=lk
        for s in curr:
            newkey=[]
            for dd in rooms[s]:
                if dd not in keys:
                    keys.append(dd)
                    lk+=1
                    newkey.append(dd)
        if prev==lk:
            return lk==llen
    return lk==llen

# Runtime 81 ms Beats 22.10%
# Memory 12.03 MB Beats 93.55%
def canVisitAllRooms_(rooms):
    """
    :type rooms: List[List[int]]
    :rtype: bool
    """
    llen=len(rooms)
    opn=[0 for i in range(llen)]
    opn[0]=1
    stack=[0]
    while stack != []:
        curr=stack.pop()
        for key in rooms[curr]:
            if opn[key]==0:
                stack.append(key)
                opn[key] = 1
    return llen==opn.count(1)

# Runtime 86 ms Beats 20.03%
# Memory 12.18 MB Beats 75.67%
# Runtime 83 ms Beats 21.72% Analyze Complexity
# Memory 12.02 MB Beats 93.55%
def canVisitAllRooms__(rooms):
    """
    :type rooms: List[List[int]]
    :rtype: bool
    """
    llen=len(rooms)
    opn=[0 for i in range(llen)]
    opn[0]=1; opnn=1
    stack=[0]
    while stack != []:
        curr=stack.pop()
        for key in rooms[curr]:
            if opn[key]==0:
                stack.append(key)
                opn[key] = 1
                opnn+=1
    return llen==opnn

# Runtime 83 ms Beats 21.72%
# Memory 12.17 MB Beats 75.67%
def canVisitAllRooms(rooms):
    """
    :type rooms: List[List[int]]
    :rtype: bool
    """
    llen = len(rooms)
    stack = [0]; visit = set()
    while stack:
        curr = stack.pop()
        visit.add(curr)
        for key in rooms[curr]:
            if key not in visit:
                stack.append(key)
    return llen == len(visit)
