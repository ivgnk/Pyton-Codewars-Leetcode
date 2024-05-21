"""
Done 21.05.2024. Topics: Linked List, Recursion
203. Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/

Given the head of a linked list and an integer val,
remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Runtime 53 ms Beats 10.89% of users with Python
# Memory 21.98 MB Beats 5.90% of users with Python

def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    r=[]
    while head:
        r.append(head.val)
        head=head.next
    r=[r1 for r1 in r if r1 !=val]
    if r == []: return None

    temp=ListNode(r[0])
    head=temp
    for i in range(1,len(r)):
        head.next=ListNode(r[i])
        head=head.next
    return temp