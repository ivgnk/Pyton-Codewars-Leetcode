"""
Done 29.08.2024. Topics: Linked List
328. Odd Even Linked List
https://leetcode.com/problems/odd-even-linked-list/description/

Given the head of a singly linked list, group all the nodes with odd indices together
followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

Constraints:
The number of nodes in the linked list is in the range [0, 104].
-10**6 <= Node.val <= 10**6
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Runtime 13 ms Beats 99.20%
# Memory 14.89 MB Beats 99.83%
# Time Complexity O(N)
# Space Complexity O(N)
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return head
        h1=head
        res=[]
        while head:
            res.append(head.val)
            head=head.next
        ll=len(res)
        nl=[res[i] for i in range(ll) if i%2==0]; lnl=len(nl)
        nr=[res[i] for i in range(ll) if i%2!=0]

        head=h1
        for i in range(len(res)):
            if i<lnl:
                head.val=nl[i]
                head=head.next
            else:
                head.val = nr[i-lnl]
                head = head.next
        return h1


