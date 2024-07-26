"""
Done 26.07.2024. Topics: Graph, Shortest Path
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


# Runtime 445 ms Beats 56.96%
# Memory 12.92 MB Beats 29.11%

# Runtime 444 ms Beats 56.96%
# Time Complexity O(N^3)
# Memory 13.21 MB Beats 7.59%
# Space Complexity O(N^2)

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

    ## If not all cities are on the list
    alls={i for i in rn}
    ss=set()
    for d in edges:
        ss.add(d[0])
        ss.add(d[1])
    ress=alls-ss
    print(alls, ss)
    if len(ress) !=0 : return max(ress)

    ## Preparation matrix for Floyd Warshall Algorithm
    dist = [[INF]*n for i in rn]
    for i in rn:
        for j in rn:
            if i==j: dist[i][j]=0

    for i,d in enumerate(edges):
        dist[d[0]][d[1]] = d[2]
        dist[d[1]][d[0]] = d[2]

    # Calc all distances: Floyd Warshall Algorithm
    for k in rn:
        # pick all vertices as source one by one
        for i in rn:
            # Pick all vertices as destination for the
            # above picked source
            for j in rn:
                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Find result
    ## We choose distances no more than distanceThreshold
    res=[(dist[i][j],i) for i in rn for j in rn if dist[i][j]<=distanceThreshold ]

    ## We find the number of neighboring cities
    dd=dict()
    for d in res:
        if d[1] in dd:
            dd[d[1]]=dd[d[1]]+1
        else:
            dd[d[1]] = 1

    ## The final choice
    lst=sorted([(v,k) for k,v in dd.items()],key=lambda x: (-x[0],x[1]),reverse=True)
    return lst[0][1]


# print(findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4))  # 3
# print(findTheCity(n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2)) # 0
# print(findTheCity(n = 6, edges = [[0,3,7],[2,4,1],[0,1,5],[2,3,10],[1,3,6],[1,2,1]], distanceThreshold = 417))
print(findTheCity(n = 8, edges = [[3,6,5840],[0,6,7765],[0,4,4017],[0,3,3930],[0,7,1730],[3,4,9214],[0,5,5861],
                                  [2,6,2600],[1,4,1908],[4,6,665],[1,5,5140],[5,7,6921],[2,7,5674],[1,2,4154],
                                  [2,5,913],[0,2,7125],[6,7,6799],[1,7,6166],[4,5,5878],[1,6,4816],[1,3,5591],
                                  [5,6,7226],[3,7,3901],[3,5,9989],[2,3,8504],[4,7,2366]], distanceThreshold = 919))



