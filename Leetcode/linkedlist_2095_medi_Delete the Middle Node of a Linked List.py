"""
Done 21.05.2024. Topics: Linked List, Two Pointers

2095. Delete the Middle Node of a Linked List
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/

You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing,
where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

Example 1:
Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node.

Example 2:
Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.

Example 3:
Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.
"""

# Runtime 1898 ms Beats 5.25% of users with Python
# Memory 98.55 MB Beats 7.35% of users with Python

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteMiddle(self, head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    r=[]; h1=head
    while head:
        r.append(head.val)
        head=head.next

    ll=len(r)
    if ll==2: del r[-1]
    elif ll==1: return None
    else: r=[r[i] for i in range(ll) if i !=ll//2]

    head = h1; ll2 = len(r)
    for i in range(ll2):
        head.val = r[i]
        if i != ll2 - 1:
            head = head.next
        else:
            head.next = None
    return h1


# Runtime 3504 ms Beats 5.01% of users with Python
# Memory 133.34 MB Beats 7.35% of users with Python

def deleteMiddle2(self, head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    r=[]
    while head:
        r.append(head.val)
        head=head.next

    ll=len(r)
    if ll==2: del r[-1]
    elif ll==1: return None
    else: r=[r[i] for i in range(ll) if i !=ll//2]

    temp=ListNode(r[0])
    head=temp
    for i in range(1,ll-1):
        head.next=ListNode(r[i])
        head=head.next
    return temp




