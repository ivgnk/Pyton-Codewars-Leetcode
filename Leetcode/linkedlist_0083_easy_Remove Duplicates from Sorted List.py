"""
Done 18.05.2024. Topics: Linked List
83. Remove Duplicates from Sorted List
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

Given the head of a sorted linked list, delete all duplicates such that each element
appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""

# Runtime 15 ms Beats 94.36% of users with Python
# Memory 11.70 MB Beats 38.57% of users with Python


def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    h1 = head;    s = []
    while head:
        s.append(head.val)
        head = head.next

    if s==[]: return None
    s2=[s[0]]+[s[i] for i in range(1,len(s)) if s[i]!=s[i-1]]

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


