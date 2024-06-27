"""
Done 27.06.2024. Topics: Graph
1791. Find Center of Star Graph
https://leetcode.com/problems/find-center-of-star-graph/description/

There is an undirected star graph consisting of n nodes labeled from 1 to n.
A star graph is a graph where there is one center node and exactly n - 1 edges
that connect the center node with every other node.
You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that
there is an edge between the nodes ui and vi. Return the center of the given star graph.

Example 1:
Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

Example 2:
Input: edges = [[1,2],[5,1],[1,3],[1,4]]
Output: 1

Hint 1
The center is the only node that has more than one edge.
Hint 2
The center is also connected to all other nodes.
Hint 3
Any two edges must have a common node, which is the center.
"""

# Runtime 591 ms Beats 81.92%
# Memory 50.55 MB Beats
# 75.62%
def findCenter(edges):
    """
    :type edges: List[List[int]]
    :rtype: int
    """
    lst=[edges[0][0],edges[0][1],edges[1][0],edges[1][1]]
    dd=dict()
    for i in lst:
        if i in dd: return i
        else: dd[i]=1


