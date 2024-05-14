"""
Done 14.05.2024. Topics: Array, Hash Table
1282. Group the People Given the Group Size They Belong To
https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/

There are n people that are split into some unknown number of groups.
Each person is labeled with a unique ID from 0 to n - 1.

You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in.
For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

Return a list of groups such that each person i is in a group of size groupSizes[i].
Each person should appear in exactly one group, and every person must be in a group.
If there are multiple answers, return any of them.
It is guaranteed that there will be at least one valid solution for the given input.

Example 1:
Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation:
The first group is [5]. The size is 1, and groupSizes[5] = 1.
The second group is [0,1,2]. The size is 3, and groupSizes[0] = groupSizes[1] = groupSizes[2] = 3.
The third group is [3,4,6]. The size is 3, and groupSizes[3] = groupSizes[4] = groupSizes[6] = 3.
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].

Example 2:
Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]

Hint 1
Put people's IDs with same groupSize into buckets, then split each bucket into groups.
Hint 2
Greedy fill until you need a new group.
"""


from collections import Counter

# Runtime 54 ms Beats 34.55% of users with Python
# Memory 11.76 MB Beats 74.87% of users with Python
# Runtime 52 ms Beats 43.46% of users with Python
# Memory 11.87 MB Beats 38.22% of users with Python
def groupThePeople(groupSizes):
    """
    :type groupSizes: List[int]
    :rtype: List[List[int]]
    """
    dd=dict(Counter(groupSizes)); ll=len(groupSizes)
    lst=sorted([[k,v] for k,v in dd.items()]); ll2=len(dd)
    res=[[] for i in range(ll2)]
    res2=[]
    for i in range(ll2):
        res.append([])
    for i in range(ll):
        for j in range(ll2):
            if lst[j][0]==groupSizes[i]:
                 res[j].append(i)
    for j in range(ll2):
       ll3=len(res[j])
       if ll3==lst[j][0]:
           res2.append(res[j])
       else:
           nn=lst[j][0]
           for i in range(0, ll3, nn):
               res2.append(res[j][i:i + nn])
    return res2



# Runtime 62 ms Beats 19.37% of users with Python
# Memory 11.89 MB Beats 38.22% of users with Python
def groupThePeople2(groupSizes):
    """
    :type groupSizes: List[int]
    :rtype: List[List[int]]
    """
    dd=dict(Counter(groupSizes)); ll=len(groupSizes)
    lst=sorted([[k,v] for k,v in dd.items()]); ll2=len(dd)
    res=[]; res2=[]
    for i in range(ll2):
        res.append([])
    for i in range(ll):
        for j in range(ll2):
            if lst[j][0]==groupSizes[i]:
                 res[j].append(i)
    for j in range(ll2):
       ll3=len(res[j])
       if ll3==lst[j][0]:
           res2.append(res[j])
       else:
           nn=lst[j][0]
           for i in range(0, ll3, nn):
               res2.append(res[j][i:i + nn])
    return res2




print('groupThePeople= ',groupThePeople([3,3,3,3,3,1,3]))
