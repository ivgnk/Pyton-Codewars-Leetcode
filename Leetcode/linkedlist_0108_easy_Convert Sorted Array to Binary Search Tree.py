"""
12.09.2024. Topics: Binary Search Tree

108. Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
"""

# Runtime 47 ms Beats 91.93%
# Memory 17.78 MB Beats 60.20%

# https://lifewithdata.com/2023/06/10/convert-sorted-array-to-binary-search-tree-problem-on-leetcode-in-python/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST2(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    if not nums:
        return None
    mid = len(nums)//2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST2(nums[:mid])
    root.right = sortedArrayToBST2(nums[mid+1:])
    return root

def sortedArrayToBST(nums) -> TreeNode:
    if not nums:
        return None

    root = TreeNode(0)
    stack = [(root, 0, len(nums) - 1)]

    while stack:
        node, left, right = stack.pop()
        if left > right:
            continue

        mid = (left + right) // 2
        node.val = nums[mid]

        node.left = TreeNode(0)
        stack.append((node.left, left, mid - 1))

        node.right = TreeNode(0)
        stack.append((node.right, mid + 1, right))

    return root

print(sortedArrayToBST2([-10,-3,0,5,9,10, 12]))