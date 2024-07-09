"""
Done 09.07.2024. Topics: Linked List, Math
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""
from typing import Optional
from copy import deepcopy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Runtime 55 ms Beats 56.30%
# Memory 16.51 MB Beats 67.51%
# Runtime 48 ms Beats 88.50%
# Memory 16.47 MB Beats 94.60%
# Runtime 46 ms Beats 93.56%
# Memory 16.69 MB Beats 23.38%

def addTwoNumbers(self, l1, l2):
    dl1 = [];    dl2 = []
    while l1:
        dl1.append(l1.val)
        l1 = l1.next
    while l2:
        dl2.append(l2.val)
        l2 = l2.next

    dl1.reverse();    n1 = int(''.join([str(dat) for dat in dl1]))
    dl2.reverse();    n2 = int(''.join([str(dat) for dat in dl2]))

    n = str(n1 + n2)
    res = [int(i) for i in n]
    res.reverse()
    lln = len(res)

    temp = ListNode(res[0])
    if lln > 1:
        head = temp
        for i in range(1, lln):
            head.next = ListNode(res[i])
            head = head.next
    return temp