"""
Done 03.10.2024. Topics: Hash Table
997. Find the Town Judge
https://leetcode.com/problems/find-the-town-judge/description/

In a town, there are n people labeled from 1 to n.
There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:
The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing
that the person labeled ai trusts the person labeled bi.
If a trust relationship does not exist in trust array, then such a trust
relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified,
or return -1 otherwise.

Example 1:
Input: n = 2, trust = [[1,2]]
Output: 2

Example 2:
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

My Solution
https://leetcode.com/problems/find-the-town-judge/solutions/5864402/python-solution-with-dictionary/
"""

from icecream import ic
def findJudge3(n, trust):
    ll = len(trust)
    if ll == n:
        return -1
    lst = [i for i in range(1, n + 1)]
    all_ = True
    prev = trust[0][1]
    for ii in trust:
        if ii[0] in lst:
            all_ = all_ and (prev == ii[1])
            lst.remove(ii[0])

    if not all_ and ll - n > 1: return -1
    return lst[0]

# Runtime 592 ms Beats 88.66%
# Memory 21.56 MB Beats 56.62%
# Time Complexity O(N)
# Space Complexity O(N)

import sys
def findJudge(n, trust):
    ll = len(trust)
    if ll == n:
        return -1


    dd= {i:0 for i in range(1,n+1)}
    for i in range(ll):
        dd[trust[i][0]]=None
        if not dd[trust[i][1]] is None:
            dd[trust[i][1]]+=1
    nmax=-1; res=[]
    for k,v in dd.items():
        if not v is None:
            if v>nmax:
                nmax=v
                res.append(k)
    if len(res)==1 and nmax==n-1:
        return res[0]
    else: return -1

# ic(findJudge(2, [[1,2]]))
# ic('-----')
# ic(findJudge(n = 3, trust = [[1,3],[2,3]]))
# ic('-----')
# ic(findJudge(n = 3, trust = [[1,3], [2,3], [3,1]]))
ic(findJudge(n = 4, trust = [[1,2],[3,2],[1,3],[4,1],[3,1],[2,1],[2,3],[4,3],[4,2],[3,4],[2,4]]))
