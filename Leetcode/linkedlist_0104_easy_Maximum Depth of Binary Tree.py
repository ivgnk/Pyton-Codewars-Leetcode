"""
Done 28.08.2024. Topics: Tree, Binary Tree

104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest
path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]

Output: 2
Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""

# Runtime 21 ms Beats 67.21%
# Memory 14.23 MB Beats 83.83%

# What is the difference between depth and height in a tree?
# https://stackoverflow.com/questions/2603692/what-is-the-difference-between-depth-and-height-in-a-tree
# https://ru.wikipedia.org/wiki/Категория:Теория_графов
# https://ru.wikipedia.org/wiki/Глубина_дерева_(теория_графов)
# https://ru.wikipedia.org/wiki/Глоссарий_теории_графов#высота_дерева
# Высота дерева — наибольшая длина пути от корня к листу.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else: return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))