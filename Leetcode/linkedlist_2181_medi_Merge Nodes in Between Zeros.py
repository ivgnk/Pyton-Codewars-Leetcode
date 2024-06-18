"""
Done 16.05.2024. Topics: Linked List, Simulation
2181. Merge Nodes in Between Zeros
https://leetcode.com/problems/merge-nodes-in-between-zeros/description/

You are given the head of a linked list, which contains a series of integers separated by 0's.
The beginning and end of the linked list will have Node.val == 0.
For every two consecutive 0's, merge all the nodes lying in between them into a single node
whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.

Example 1:
Input: head = [0,3,1,0,4,5,2,0]
Output: [4,11]
Explanation:
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 3 + 1 = 4.
- The sum of the nodes marked in red: 4 + 5 + 2 = 11.

Example 2:
Input: head = [0,1,0,3,0,2,2,0]
Output: [1,3,4]
Explanation:
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 1 = 1.
- The sum of the nodes marked in red: 3 = 3.
- The sum of the nodes marked in yellow: 2 + 2 = 4.

Hint 1
How can you use two pointers to modify the original list into the new list?
Hint 2
Have a pointer traverse the entire linked list,
while another pointer looks at a node that is currently being modified.
Hint 3
Keep on summing the values of the nodes between the traversal pointer and
the modifying pointer until the former comes across a ‘0’. In that case,
the modifying pointer is incremented to modify the next node.
Hint 4
Do not forget to have the next pointer of the final node of the modified list point to null.
"""

# Runtime 2051 ms Beats 87.39% of users with Python
# Memory 130.11 MB Beats 58.56% of users with Python

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeNodes(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    ssum = 0;    lst = [];    ini = True;    h1 = head;    h2 = head
    while head:
        if head.val == 0:
            if ini: ini = False
            else:  lst.append(ssum); ssum = 0
        else:
            ssum = ssum + head.val
        head = head.next

    head = h1;    i = 0
    if len(lst) == 1:
        head.val = lst[i]
        head.next = None
    else:
        while i < len(lst):
            head.val = lst[i]
            head = head.next
            i = i + 1
            if i == len(lst) - 1: head.next = None
    return h1
