"""
Done 26.11.2024. Topics: Graph
2924. Find Champion II
https://leetcode.com/problems/find-champion-ii

There are n teams numbered from 0 to n - 1 in a tournament; each team is also a node in a DAG.
https://en.wikipedia.org/wiki/Directed_acyclic_graph
You are given the integer n and a 0-indexed 2D integer array edges of length m representing the DAG,
where edges[i] = [ui, vi] indicates that there is a directed edge from team ui to team vi in the graph.

A directed edge from a to b in the graph means that team a is stronger than team b and team b is weaker than team a.
Team a will be the champion of the tournament if there is no team b that is stronger than team a.
Return the team that will be the champion of the tournament if there is a unique champion, otherwise, return -1.

Notes
A cycle is a series of nodes a1, a2, ..., an, an+1 such that node a1 is the same node as node an+1,
the nodes a1, a2, ..., an are distinct, and there is a directed edge
from the node ai to node ai+1 for every i in the range [1, n].
A DAG is a directed graph that does not have any cycle.

Example 1:
Input: n = 3, edges = [[0,1],[1,2]]
Output: 0
Explanation: Team 1 is weaker than team 0. Team 2 is weaker than team 1. So the champion is team 0.

Example 2:
Input: n = 4, edges = [[0,2],[1,3],[1,2]]
Output: -1
Explanation: Team 2 is weaker than team 0 and team 1. Team 3 is weaker than team 1. But team 1 and team 0 are not weaker than any other teams. So the answer is -1.

Constraints:
1 <= n <= 100
m == edges.length
0 <= m <= n * (n - 1) / 2
edges[i].length == 2
0 <= edge[i][j] <= n - 1
edges[i][0] != edges[i][1]
The input is generated such that if team a is stronger than team b, team b is not stronger than team a.
The input is generated such that if team a is stronger than team b and team b is stronger than team c, then team a is stronger than team c.

What is a winner? A team that did not lose any fight.
Use a boolean[n] losses to mark which team has lost (edge[1])
Traverse losses and, if current team has not lost, mark its index. You will return this index at the end.
If encountering another such case, (a second winner) then return -1.
https://leetcode.com/problems/find-champion-ii/description/comments/2176605
"""

# My solution ✏️ Fastest (0 ms) and easy Python solution for Problem 2924 based on tip
# https://leetcode.com/problems/find-champion-ii/solutions/6084806/fastest-0-ms-and-easy-python-solution-for-problem-2924-based-on-tip/
#
# Runtime 0 ms Beats 100.00%
# Memory 13.18 MB Beats 8.33%
def findChampion(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: int
    """
    bl=[True]*n # True not loss
    for dat in edges:
        bl[dat[1]]=False
    have=False
    for i in range(n):
        if bl[i]:
            if have: return -1
            else:
                nn = i
                have=True
    return nn

print(findChampion(n = 3, edges = [[0,1],[1,2]]))
print(findChampion(n = 4, edges = [[0, 2], [1, 3], [1, 2]]))