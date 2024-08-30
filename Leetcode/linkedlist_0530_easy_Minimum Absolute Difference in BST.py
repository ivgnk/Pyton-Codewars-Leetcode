"""
Done 30.08.2024. Topics: Tree, Binary Tree

530. Minimum Absolute Difference in BST
Given the root of a Binary Search Tree (BST), return the minimum absolute difference
between the values of any two different nodes in the tree.

Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105
Note: This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/

Solution
✏️ Easy Python solution with Binary Tree Inorder Traversal

Intuition
Use Binary Tree Inorder Traversal without sorting
or
Use Binary Tree Postorder Traversal with sorting
The difference in execution speed is not great.

Approach
Use Binary Tree Inorder Traversal
"""

# Runtime 27 ms Beats 90.67%
# Memory 15.70 MB Beats 75.00%
# Time Complexity O(N)
# Space Complexity O(N)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res=[]
        self.getInorder(root)
        # b = sorted(self.res)
        b = self.res
        minDiff=1000000
        for i in range(len(b)-1):
            minDiff = min(minDiff, abs(b[i] - b[i + 1]))
        return minDiff

    def getInorder(self, node):
        if node != None:
            self.getInorder(node.left)
            self.res.append(node.val)
            self.getInorder(node.right)
