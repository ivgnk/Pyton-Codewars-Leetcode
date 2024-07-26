"""
1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti]
represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most
istanceThreshold, If there are multiple such cities, return the city with the greatest number.
RUS: Возвращает город с наименьшим количеством городов, до которых можно добраться по некоторому пути и расстояние
до которых не превышает distanceThreshold. Если таких городов несколько, верните город с наибольшим числом (номером).

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

Example 1:
Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph.
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2]
City 1 -> [City 0, City 2, City 3]
City 2 -> [City 0, City 1, City 3]
City 3 -> [City 1, City 2]
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.

Example 2:
Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
Explanation: The figure above describes the graph.
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1]
City 1 -> [City 0, City 4]
City 2 -> [City 3, City 4]
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3]
The city 0 has 1 neighboring city at a distanceThreshold = 2.

Constraints:
2 <= n <= 100
1 <= edges.length <= n * (n - 1) / 2
edges[i].length == 3
0 <= fromi < toi < n
1 <= weighti, distanceThreshold <= 10^4
All pairs (fromi, toi) are distinct.

Hint 1
Use Floyd-Warshall's algorithm to compute any-point to any-point distances.
(Or can also do Dijkstra from every node due to the weights are non-negative).
Hint 2
For each city calculate the number of reachable cities within the threshold, then search for the optimal city.
"""

#  Floyd Warshall Algorithm
#  https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
# Wrong Answer - 44 / 54 testcases passed

INF = 999999

def printSolution(n,dist,inform=''):
    print(inform)
    if inform =='': print("Following matrix shows the shortest distances between every pair of vertices")
    for i in range(n):
        for j in range(n):
            if(dist[i][j] == INF):
                print("%7s" % ("INF"), end=" ")
            else:
                print("%7d\t" % (dist[i][j]), end=' ')
            if j == n-1:
                print()


def findTheCity(n, edges, distanceThreshold):
    """
    Add all vertices one by one to the set of intermediate vertices.
     ---> Before start of an iteration, we have shortest distances
     between all pairs of vertices  such that the shortest
     distances consider only the  vertices in the set
    {0, 1, 2, .. k-1} as intermediate vertices.
      ----> After the end of a   iteration, vertex no. k is
     added to the set of intermediate vertices and the set becomes {0, 1, 2, .. k}

    :type n: int
    :type edges: List[List[int]]
    :type distanceThreshold: int
    :rtype: int
    """
    # Preparation
    rn = range(n)
    dist = [[INF]*n for i in rn]
    for i in rn:
        for j in rn:
            if i==j: dist[i][j]=0

    # print(edges)
    for i,d in enumerate(edges):
        dist[d[0]][d[1]] = d[2]
        dist[d[1]][d[0]] = d[2]

    # printSolution(n, dist, inform='initialization')

    # Calc all distances
    for k in rn:
        # pick all vertices as source one by one
        for i in rn:
            # Pick all vertices as destination for the
            # above picked source
            for j in rn:
                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # printSolution(n, dist, inform='finding')

    # Find result
    res=[(dist[i][j],i) for i in rn for j in rn  if 0<dist[i][j]<=distanceThreshold ]
    # print(res)
    dd=dict()
    for d in res:
        if d[1] in dd:
            dd[d[1]]=dd[d[1]]+1
        else:
            dd[d[1]] = 1
    # print(dd)
    lst=sorted([(v,k) for k,v in dd.items()],key=lambda x: (-x[0],x[1]),reverse=True)
    # print(lst)
    return lst[0][1]


print(findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4))
print(findTheCity(n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2))




