"""
Done 18.05.2024. Topics: Linked List
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/description/

Given the head of a singly linked list, reverse the list, and return the reversed list.
Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
"""

# Runtime 10 ms Beats 96.81% of users with Python
# Memory 13.78 MB Beats 25.79% of users with Python

def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    h1 = head;  s = []
    while head:
        s.append(head.val)
        head = head.next
    s = s[::-1]
    head = h1; i=0
    while head:
        head.val=s[i]
        head = head.next
        i=i+1
    return h1
