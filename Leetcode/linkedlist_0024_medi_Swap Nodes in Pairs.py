"""
24. Swap Nodes in Pairs. Topics: Linked List, Recursion
https://leetcode.com/problems/swap-nodes-in-pairs/description/
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]
"""

# Runtime 15 ms Beats 50.66% of users with Python
# Memory 11.59 MB Beats 85.40% of users with Python
# Runtime 7 ms Beats 97.01% of users with Python
# Memory 11.43 MB Beats 98.50% of users with Python

def swapPairs(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head == None: return None
    s = [];    h1 = head
    while head:
        s.append(head.val)
        head = head.next
    ll = len(s)
    if ll == 1: return h1
    for i in range(1, ll, 2):
        s[i], s[i - 1] = s[i - 1], s[i]
    head = h1
    for i in range(ll):
        head.val = s[i]
        head = head.next
    return h1


print(swapPairs([1,2,3,4]))