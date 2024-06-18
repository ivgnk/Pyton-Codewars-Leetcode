"""
Done 21.05.2024. Topics: Linked List, Two Pointers, Stack, Recursion
143. Reorder List
https://leetcode.com/problems/reorder-list/description/

You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
"""

# Runtime 55 ms Beats 83.74% of users with Python
# Memory 32.42 MB Beats 5.67% of users with Python

def reorderList(self, head):
    """
    :type head: ListNode
    :rtype: None Do not return anything, modify head in-place instead.
    """
    r = [];  h1 = head
    while head:
        r.append(head.val)
        head = head.next
    r = [r[i // 2] if i % 2 == 0 else r[-1 - i // 2] for i in range(len(r))]

    head=h1;  i=0
    while head:
        head.val=r[i]
        head=head.next
        i=i+1
    return h1
