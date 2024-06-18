"""
Done 20.05.2024. Topics: Linked List, Math

2807. Insert Greatest Common Divisors in Linked List
https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/

Given the head of a linked list head, in which each node contains an integer value.
Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.
Return the linked list after insertion.
The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

Example 1:
Input: head = [18,6,10,3]
Output: [18,6,6,2,10,1,3]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes (nodes in blue are the inserted nodes).
- We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
- We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
- We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
There are no more adjacent nodes, so we return the linked list.

Example 2:
Input: head = [7]
Output: [7]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes.
There are no pairs of adjacent nodes, so we return the initial linked list.
"""


from fractions import gcd

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Runtime 95 ms Beats 41.51% of users with Python
# Memory 21.31 MB Beats 5.66% of users with Python
# Runtime 88 ms Beats 63.52% of users with Python
# Memory 21.39 MB Beats 5.66% of users with Python


def insertGreatestCommonDivisors(self, head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    r=[]; h1=head
    while head:
        r.append(head.val)
        head=head.next
    if len(r)<=1: return h1
    r2=[r[0]]
    for i in range(1,len(r)):
        r2.append(gcd(r[i-1],r[i]))
        r2.append(r[i])

    result = ListNode(r2[0])
    temp = result
    for i in range(1, len(r2)):
        result.next = ListNode(r2[i])
        result = result.next
    return temp
