"""
Done 20.05.2024. Topics: Linked List
23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/description/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
"""

# Runtime 65 ms Beats 88.76% of users with Python
# Memory 16.95 MB Beats 100.00% of users with Python

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(self, lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    ll=len(lists); r = range(ll)
    if ll == 0: return None
    if all(lists[i]==None for i in r): return None

    res=[]
    for i in r:
        while lists[i]:
            res.append(lists[i].val)
            lists[i] = lists[i].next
    res=sorted(res)

    result = ListNode(res[0])
    temp = result
    for i in range(1, len(res)):
        result.next = ListNode(res[i])
        result = result.next
    return temp

