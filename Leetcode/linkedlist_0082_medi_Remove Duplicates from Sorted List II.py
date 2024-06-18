"""
Done 18.05.2024. Topics: Linked List, Two Pointers
82. Remove Duplicates from Sorted List II
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.
Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]
"""

# Runtime 19 ms Beats 80.64%# of users with Python
# Memory 11.59 MB Beats 93.81% of users with Python

from collections import Counter
def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    h1 = head;    s = []
    while head:
        s.append(head.val)
        head = head.next
    dd = dict(Counter(s))
    s2 = [i for i in s if dd[i] == 1]
    if s2 == []: return None
    head = h1;    i = 0
    ll = len(s2)
    while i < ll:
        head.val = s2[i]
        if i == len(s2) - 1:
            head.next = None
            break
        else:
            head = head.next
            i = i + 1
    return h1