"""
25.12.2024. Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree
111. Minimum Depth of Binary Tree
https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path
from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Constraints:
The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
"""
# Runtime 214 ms Beats 12.66%
# Memory 94.48 MB Beats 33.63%
# Time Complexity O(N)
# Space Complexity O(Log(N))

from typing import Optional
# https://leetcode.com/problems/minimum-depth-of-binary-tree/solutions/6168147/minimum-depth-of-binary-tree-by-roieben-0ykz/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftHeight = self.minDepth(root.left)
        rightHeight = self.minDepth(root.right)

        if not root.left or not root.right:  # one side is empty - we still calculate height based on the other side
            return 1 + max(leftHeight, rightHeight)

        return 1 + min(leftHeight, rightHeight)