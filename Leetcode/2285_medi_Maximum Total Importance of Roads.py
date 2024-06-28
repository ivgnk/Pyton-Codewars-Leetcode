"""
Done 28.06.2024. Topics: Graph, Sorting
2285. Maximum Total Importance of Roads
https://leetcode.com/problems/maximum-total-importance-of-roads/

You are given an integer n denoting the number of cities in a country.
The cities are numbered from 0 to n - 1.

You are also given a 2D integer array roads where roads[i] = [ai, bi]
denotes that there exists a bidirectional road connecting cities ai and bi.

You need to assign each city with an integer value from 1 to n, where each value can only be used once.
The importance of a road is then defined as the sum of the values of the two cities it connects.

Return the maximum total importance of all roads possible after assigning the values optimally.

Example 1:
Input: n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
Output: 43
Explanation: The figure above shows the country and the assigned values of [2,4,5,3,1].
- The road (0,1) has an importance of 2 + 4 = 6.
- The road (1,2) has an importance of 4 + 5 = 9.
- The road (2,3) has an importance of 5 + 3 = 8.
- The road (0,2) has an importance of 2 + 5 = 7.
- The road (1,3) has an importance of 4 + 3 = 7.
- The road (2,4) has an importance of 5 + 1 = 6.
The total importance of all roads is 6 + 9 + 8 + 7 + 7 + 6 = 43.
It can be shown that we cannot obtain a greater total importance than 43.

Example 2:
Input: n = 5, roads = [[0,3],[2,4],[1,3]]
Output: 20
Explanation: The figure above shows the country and the assigned values of [4,3,2,5,1].
- The road (0,3) has an importance of 4 + 5 = 9.
- The road (2,4) has an importance of 2 + 1 = 3.
- The road (1,3) has an importance of 3 + 5 = 8.
The total importance of all roads is 9 + 3 + 8 = 20.
It can be shown that we cannot obtain a greater total importance than 20.

Hint 1
Consider what each city contributes to the total importance of all roads.
Hint 2
Based on that, how can you sort the cities such that
assigning them values in that order will yield the maximum total importance?

as hint1
Consider that each cities assigned "importance score" gets used
as many times as the edges/roads that connect to that city.
In other words, if city A has 3 roads that connect to it with an importance score of 4,
the total importance that cityA will contribute is equal to 4 * 3 = 12.

Since we can assign the importance scores ourselves from 1 to n,
it would make sense then that the highest importance scores should be assigned
to the cities with the most roads connected to them.
"""

# Runtime 1269 ms Beats 33.33%
# Memory 40.60 MB Beats 16.67%
# Runtime 1248 ms Beats 38.89%
# Memory 40.52 MB Beats 16.67%
# Runtime 1246 ms Beats 38.89%
# Memory 40.30 MB Beats 16.67%
# Runtime 1233 ms Beats 50.00%
# Memory 40.50 MB Beats 16.67%
from icecream import ic
def maximumImportance(n, roads):
    """
    :type n: int
    :type roads: List[List[int]]
    :rtype: int
    """
    ll = len(roads)
    if ll == 1: return n + (n - 1)

    dd=dict(); dd2=dict()
    for i in range(ll):
        a,b = roads[i][0], roads[i][1]
        if a in dd: dd[a]=dd[a]+1
        else: dd[a]=1
        if b in dd: dd[b]=dd[b]+1
        else: dd[b]=1
    ldd=len(dd)
    lst=sorted([[v,k,0] for k,v in dd.items()], reverse=True)
    for i in range(ldd):
        # c = lst[i][1]
        # dd2[c]=n
        dd2[lst[i][1]] = n
        n=n-1
    # ssum=0
    # for i in range(ll):
    #     a,b = roads[i][0], roads[i][1]
    #     ssum=ssum+dd2[a]+dd2[b]
    # return ssum
    return sum([dd2[roads[i][0]]+dd2[roads[i][1]] for i in range(ll)])



ic(maximumImportance(n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))
ic(maximumImportance(n = 5, roads = [[0,3],[2,4],[1,3]]))
ic(maximumImportance(n = 4, roads = [[3,2],[0,2]]))







