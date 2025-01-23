"""
23.01.2024. Topics: Tree, Depth-First Search, Breadth-First Search
112. Path Sum
https://leetcode.com/problems/path-sum/description/

Given the root of a binary tree and an integer targetSum,
return true if the tree has a root-to-leaf path such that adding up all the values
along the path equals targetSum.

A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.


Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""
from typing import Optional

###----1
# https://leetcode.com/problems/path-sum/solutions/6312757/simple-python-multiple-solutions-dfs-rec-x4qt/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS - recursive
class Solution1:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currSum) -> bool:
            # base case
            if not node:
                return False

            currSum += node.val
            # only when we reach a leaf node
            if not node.left and not node.right:
                return currSum == targetSum

            # process
            return dfs(node.left, currSum) or dfs(node.right, currSum)

        if not root:
            return False

        return dfs(root, 0)


# iterative  - using stack
class Solution2:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # add the node to stack
        stack = [[root, 0]]

        # pop from stack and process it
        while stack:
            node, currSum = stack.pop()
            currSum += node.val
            if not node.left and not node.right and currSum == targetSum:
                return True

            if node.left:
                stack.append([node.left, currSum])
            if node.right:
                stack.append([node.right, currSum])

        return False


# # iteratiev - BFS - using a QUEUE
class Solution3:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        from collections import deque

        if not root:
            return False

        q = deque([[root, 0]])
        while q:
            # pop from queue
            node, currSum = q.popleft()
            currSum += node.val

            # process it
            if not node.left and not node.right and currSum == targetSum:
                return True

            # append child again to the queue
            if node.left:
                q.append([node.left, currSum])
            if node.right:
                q.append([node.right, currSum])

        return False
###----1

# Runtime 4 ms Beats 33.15%
# Memory 14.20 MB Beats 46.77%
# Runtime 0 ms Beats 100.00%
# Memory 14.18 MB Beats 74.41%
# https://leetcode.com/problems/path-sum/solutions/6310028/on-by-navani_hk-zte1/
class Solution(object):
    def hasPathSum(self, root, targetSum):
        def helper(node,cur):
            if(not node):
                return False
            cur+=node.val
            if(not node.left and not node.right):
                return cur==targetSum
            return helper(node.left,cur) or helper(node.right,cur)
        return helper(root,0)