"""
Done 25.08.2024. Topics: Tree
145. Binary Tree Postorder Traversal
https://leetcode.com/problems/binary-tree-postorder-traversal/description/

Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
Follow up: Recursive solution is trivial, could you do it iteratively?

Solution
✏️ Easy Python solution based on sample from geeksforgeeks

# Intuition
https://en.wikipedia.org/wiki/Tree_traversal

# Approach
I read it and made it according to the sample
https://www.geeksforgeeks.org/postorder-traversal-of-binary-tree
Done 25.08.2024.
Runtime 10 ms Beats 85.24%
Memory 11.69 MB Beats 50.69%

# Complexity
- Time complexity: O(N)
- Space complexity: O(N)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res=[]
        self.getPostorder(root)
        return self.res

    def getPostorder(self,node):
        if node != None:
            self.getPostorder(node.left)
            self.getPostorder(node.right)
            self.res.append(node.val)
