"""
Done 26.08.2024. Topics: Binary Tree
94. Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/description/

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# https://www.geeksforgeeks.org/inorder-traversal-of-binary-tree/
# Inorder(root):
# If root is NULL, then return
# Inorder (root -> left)
# Process root (For example, print root’s data)
# Inorder (root -> right)

# Solution
# ✏️ Easy Python recurcsive solution
# Intuition
# https://en.wikipedia.org/wiki/Tree_traversal
#
# Approach
# https://www.geeksforgeeks.org/inorder-traversal-of-binary-tree/
# Analog from
# https://www.geeksforgeeks.org/postorder-traversal-of-binary-tree
# https://leetcode.com/discuss/topic/5689934/easy-python-solution-based-on-sample-from-geeksforgeeks/





# Runtime 6 ms Beats 96.97%
# Memory 11.62 MB Beats 50.83%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res=[]
        self.getInorder(root)
        return self.res

    def getInorder(self, node):
        if node != None:
            self.getInorder(node.left)
            self.res.append(node.val)
            self.getInorder(node.right)

