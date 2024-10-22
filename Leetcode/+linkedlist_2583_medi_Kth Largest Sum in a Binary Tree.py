"""
22.10.2024. Topics: Tree, Breadth-First Search, Sorting, Binary Tree
2583. Kth Largest Sum in a Binary Tree
https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

You are given the root of a binary tree and a positive integer k.
The level sum in the tree is the sum of the values of the nodes that are on the same level.

Return the kth largest level sum in the tree (not necessarily distinct).
If there are fewer than k levels in the tree, return -1.

Note that two nodes are on the same level if they have the same distance from the root.

Example 1:
Input: root = [5,8,9,2,1,3,7,4,6], k = 2
Output: 13
Explanation: The level sums are the following:
- Level 1: 5.
- Level 2: 8 + 9 = 17.
- Level 3: 2 + 1 + 3 + 7 = 13.
- Level 4: 4 + 6 = 10.
The 2nd largest level sum is 13.

Example 2:
Input: root = [1,2,null,3], k = 1
Output: 3
Explanation: The largest level sum is 3.

Constraints:
The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= 106
1 <= k <= n

Hint 1
Find the sum of values of nodes on each level and return the kth largest one.
Hint 2
To find the sum of the values of nodes on each level, you can use a DFS or BFS algorithm
to traverse the tree and keep track of the level of each node.
"""

from pBST import *
TreeNode = Node

# Definition for a binary tree node.
import heapq
def kthLargestLevelSum(root: TreeNode, k: int) -> int:
    bigger = []
    stk = [root]
    curr_max = -1

    while stk:
        new_stk = []
        curr_val = 0
        for node in stk:
            if node.right:
                new_stk.append(node.right)
            if node.left:
                new_stk.append(node.left)
            curr_val += node.val

        stk = new_stk

        if len(bigger) < k:
            heapq.heappush(bigger, curr_val)
            curr_max = max(curr_max, curr_val)
        else:
            if curr_val > bigger[0]:
                heapq.heappop(bigger)
                heapq.heappush(bigger, curr_val)
                curr_max = max(curr_max, curr_val)
    print('bigger = ',bigger)
    return -1 if len(bigger) < k else bigger[0]
# print(kthLargestLevelSum())

def work_tree():
    print(TreeNode, type(TreeNode))
    print(Node, type(Node))
    root=create_BST_from_list([5,8,9,2,1,3,7,4,6])
    root.view_tree()
    print(f'{type(root)=} ')
    print(kthLargestLevelSum(root, 2))

if __name__=="__main__":
    work_tree()