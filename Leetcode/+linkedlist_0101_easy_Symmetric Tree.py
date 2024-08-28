"""
28.08.2024. Topics: Tree, Binary Tree
101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself
(i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100

Follow up: Could you solve it both recursively and iteratively?

Solution
https://leetcode.com/problems/symmetric-tree/solutions/5673275/python-easy-solution-beats-95/
Intuition
    Recursive Comparison: Recursively compare the left and right subtrees:
     - The left subtree of the left node should be a mirror of the right subtree of the right node.
     - The right subtree of the left node should be a mirror of the left - subtree of the right node.
       The values of the corresponding nodes should be the same.

Approach
    -  isMirror(left, right): This helper function checks if two subtrees (left and right) are mirrors of each other.
    -- If both subtrees are None, they are mirrors.
    -- If one is None and the other is not, they are not mirrors.
    -- Otherwise, it checks if the values of the two nodes are the same and recursively checks
      the left subtree of the left node with the right subtree of the right node,
      and the right subtree of the left node with the left subtree of the right node.
    - isSymmetric(root): This function starts the symmetry check by comparing the left and right subtrees of the root.

Complexity
    Time complexity: O(n)
    Space complexity: O(h)
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Runtime 15 ms Beats 74.58%
# Memory 11.88 MB Beats 40.60%
class Solution:
    def isSymmetric(self, root):
        # A helper function to compare two nodes
        def isMirror(left, right):
            # If both nodes are None, they are symmetric
            if left is None and right is None:
                return True
            # If one of them is None, they are not symmetric
            if left is None or right is None:
                return False
            # Check if the values are the same and the subtrees are mirrors
            return (left.val == right.val and
                    isMirror(left.left, right.right) and
                    isMirror(left.right, right.left))

        # Start the recursion with the root's left and right children
        return isMirror(root.left, root.right)