"""
Done 12.06.2024. Topics: Linked List
1721. Swapping Nodes in a Linked List. Topics: Linked List, Two Pointers

You are given the head of a linked list, and an integer k.
Return the head of the linked list after swapping the values of the kth node from the
beginning and the kth node from the end (the list is 1-indexed).

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
"""

# Runtime 998 ms Beats 13.24% of users with Python
# Memory 91.36 MB Beats 9.06% of users with Python

def swapNodes(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if head == None: return None
    s = [];    h1 = head
    while head:
        s.append(head.val)
        head = head.next
    ll = len(s)
    if ll == 1 or ll<k: return h1
    head = h1
    s[k - 1], s[ll-k]=s[ll-k], s[k - 1]
    for i in range(ll):
        head.val = s[i]
        head = head.next
    return h1

