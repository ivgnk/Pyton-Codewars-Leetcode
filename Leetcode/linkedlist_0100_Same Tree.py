"""
Done 28.08.2024. Topics: Tree, Binary Tree
100. Same Tree
https://leetcode.com/problems/same-tree/description/

Given the roots of two binary trees p and q,
write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
The number of nodes in both trees is in the range [0, 100].
-10**4 <= Node.val <= 10**4
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Runtime 32 ms Beats 75.69%
# Memory 16.48 MB Beats 84.65%
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

# Runtime 35 ms Beats 55.51%
# Memory 16.59 MB Beats 36.48%
# Runtime 30 ms Beats 86.56%
# Memory 16.51 MB Beats 36.48%
class Solution2(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        self.res_p=[]
        self.res_q=[]
        self.getInorder_p(p)
        self.getInorder_q(q)
        return self.res_p==self.res_q

    def getInorder_p(self, node):
        if node != None:
            self.getInorder_p(node.left)
            self.res_p.append(node.val)
            self.getInorder_p(node.right)
        self.res_p.append(None)

    def getInorder_q(self, node):
        if node != None:
            self.getInorder_q(node.left)
            self.res_q.append(node.val)
            self.getInorder_q(node.right)
        self.res_q.append(None)

