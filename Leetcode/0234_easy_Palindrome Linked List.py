"""
Done 18.05.2024. Topics: Linked List
234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a
palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
"""

# Runtime 723 ms Beats 62.31% of users with Python
# Memory 83.47 MB Beats 26.92% of users with Python

def isPalindrome(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    s = []
    while head:
        s.append(head.val)
        head = head.next
    return s == s[::-1]

