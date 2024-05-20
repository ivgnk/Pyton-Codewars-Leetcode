"""
Done 20.05.2024. Topics: Linked List, Recursion
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/description/

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""

# Runtime 15 ms Beats 82.95% of users with Python
# Memory 11.71 MB Beats 31.11% of users with Python

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    if list1 == None and list2 == None: return None
    res=[]
    while list1:
        res.append(list1.val)
        list1=list1.next

    while list2:
        res.append(list2.val)
        list2=list2.next

    res=sorted(res)
    # print(res)
    # https://www.geeksforgeeks.org/merge-two-sorted-linked-lists/

    result = ListNode(res[0])
    temp = result
    for i in range(1, len(res)):
        result.next = ListNode(res[i])
        result = result.next
    return temp


