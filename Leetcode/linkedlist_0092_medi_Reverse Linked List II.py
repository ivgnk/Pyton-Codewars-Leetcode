"""
Done 18.05.2024. Topics: Linked List
92. Reverse Linked List II
https://leetcode.com/problems/reverse-linked-list-ii/description/

Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
"""

# Runtime 12 ms Beats 76.17% of users with Python
# Memory 11.67 MB Beats 97.71% of users with Python

def reverseBetween(self, head, left, right):
    """
    :type head: ListNode
    :type left: int
    :type right: int
    :rtype: ListNode
    """
    h1 = head;    s = []
    while head:
        s.append(head.val)
        head = head.next
    if left != right:
        li = left - 1  # ri=right-1
        s1 = s[li:right]
        s1 = s1[::-1]
        s[li:right] = s1
    head = h1; i = 0
    while head:
        head.val = s[i]
        head = head.next
        i = i + 1
    return h1
