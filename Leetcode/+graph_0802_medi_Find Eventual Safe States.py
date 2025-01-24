"""
24.01.2025. Topics: Depth-First Search, Breadth-First Search, Graph, Topological Sort
802. Find Eventual Safe States
https://leetcode.com/problems/find-eventual-safe-states/description/

There is a directed graph of n nodes with each node labeled from 0 to n - 1.
The graph is represented by a 0-indexed 2D integer array graph where graph[i]
is an integer array of nodes adjacent to node i,
meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges.
A node is a safe node if every possible path starting from that node leads0
to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph.
The answer should be sorted in ascending order.

Example 1:
Illustration of graph
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.

Example 2:
Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]
Explanation:
Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.


Constraints:
n == graph.length
1 <= n <= 104
0 <= graph[i].length <= n
0 <= graph[i][j] <= n - 1
graph[i] is sorted in a strictly increasing order.
The graph may contain self-loops.
The number of edges in the graph will be in the range [1, 4 * 104].
"""
from typing import List


# Runtime 35 ms Beats 74.63%
# Memory 23.64 MB Beats 53.15%
class Solution1:
    def eventualSafeNodes(self, graph:  List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}
        res = []

        def dfs(i):
            if i in safe:
                return safe[i]

            safe[i] = False
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            safe[i] = True
            return True

        for i in range(n):
            if dfs(i):
                res.append(i)
        return res

# Runtime 430 ms Beats 5.04%
# Memory 23.80 MB Beats 39.31%
class Solution2:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        is_safe = [False] * n
        visited = [False] * n
        for i in range(n):
            if not graph[i]:
                is_safe[i] = True
                visited[i] = True

        def dfs(u):
            visited[u] = True
            flag = True
            for v in graph[u]:
                if not visited[v] and not is_safe[v]:
                    flag = flag and dfs(v)
                if visited[v] and not is_safe[v]:
                    flag = False
            is_safe[u] = flag
            visited[u] = False
            return flag

        for u in range(n):
            if not visited[u] and not is_safe[u]:
                dfs(u)
        res = []
        for i in range(n):
            if is_safe[i]:
                res.append(i)
        return res
