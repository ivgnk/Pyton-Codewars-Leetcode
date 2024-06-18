"""
Done 09.05.2024. Topics: Linked List, Sorting
148. Sort List
https://leetcode.com/problems/sort-list/description/

Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []
"""

# Runtime 198 ms Beats 99.15% of users with Python
# Memory 52.03 MB Beats 66.79% of users with Python

def sortList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    res = [];    h1 = head
    while head:
        res.append(head.val)
        head = head.next
    res = sorted(res)
    head = h1;    i = 0
    while head:
        head.val = res[i]
        head = head.next
        i = i + 1
    return h1
