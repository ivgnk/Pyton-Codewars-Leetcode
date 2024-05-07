"""
Done 07.05.2024. Topics: Linked List, Two Pointers

876. Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/description/

Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
"""

# Runtime 3 ms Beats 99.61% of users with Python
# Memory 11.70 MB Beats 62.28% of users with Python

def middleNode(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    res = []
    while head:
        res.append([head.val, head])
        head = head.next
    return res[len(res) // 2][1]
