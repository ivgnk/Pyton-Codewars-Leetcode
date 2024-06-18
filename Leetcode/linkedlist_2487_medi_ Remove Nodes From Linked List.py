"""
Done 20.05.2024. Topics: Linked List, Stack, Recursion, Monotonic Stack
2487. Remove Nodes From Linked List
https://leetcode.com/problems/remove-nodes-from-linked-list/description/

Remove every node which has a node with a greater value anywhere to the right side of it.
Return the head of the modified linked list.

Example 1:
Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.

Example 2:
Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Runtime 1666 ms Beats 9.71% of users with Python
# Memory 133.44 MB Beats 24.02% of users with Python
def removeNodes2(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    h1 = head;    r = []
    while head:
        r.append(head.val)
        head = head.next

    ll=len(r)
    if all([r[i]==r[i-1] for i in range(1,ll)]): return h1
    if r==sorted(r,reverse=True): return h1
    r2=[]; mmax=min(r)-1
    for i in range(ll-1,-1,-1):
        mmax2=max(mmax,r[i])
        if mmax2>=mmax:
            mmax=mmax2
            r2.append(mmax)
    r2.reverse()

    result = ListNode(r2[0])
    temp = result
    for i in range(1, len(r2)):
        result.next = ListNode(r2[i])
        result = result.next
    return temp

# Runtime 1540 ms Beats 27.69% of users with Python
# Memory 133.27 MB Beats 25.25% of users with Python
def removeNodes(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    h1 = head;    r = []
    while head:
        r.append(head.val)
        head = head.next

    ll=len(r)
    r2=[]; mmax=min(r)-1
    for i in range(ll-1,-1,-1):
        mmax2=max(mmax,r[i])
        if mmax2>=mmax:
            mmax=mmax2
            r2.append(mmax)
    r2.reverse()

    result = ListNode(r2[0])
    temp = result
    for i in range(1, len(r2)):
        result.next = ListNode(r2[i])
        result = result.next
    return temp


print(removeNodes('head'))

