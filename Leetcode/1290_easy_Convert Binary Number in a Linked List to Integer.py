"""
Done 07.05.2024. Topics: Linked List, Math

1290. Convert Binary Number in a Linked List to Integer
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/

Given head which is a reference node to a singly-linked list.
The value of each node in the linked list is either 0 or 1.
The linked list holds the binary representation of a number.
Return the decimal value of the number in the linked list.
The most significant bit is at the head of the linked list.

Example 1:

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Example 2:
Input: head = [0]
Output: 0
"""

# Runtime 8 ms Beats 92.63% of users with Python
# Memory 11.81 MB Beats 11.38% of users with Python

# https://www.youtube.com/watch?v=j3RUXW55aeA
def getDecimalValue(head):
    """
    :type head: ListNode
    :rtype: int
    """
    if not head: return 0
    res = ""
    while head:
        res = res+str(head.val)
        head = head.next
    return int(res,2)

