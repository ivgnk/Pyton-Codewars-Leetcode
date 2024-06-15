"""
Done 15.06.2024. Topics: Linked List
61. Rotate List
https://leetcode.com/problems/rotate-list/description

Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
"""

# Wrong Answer -- # 30 / 232 testcases passed

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        elif k == 0:
            return head
        h1 = head;    res = []
        while head:
            res.append(head.val)
            head = head.next

        ll = len(res)
        if k == 1:
            if ll == 2:
                res = [res[1], res[0]]
        else:
            if ll == 2:
                if k % 2 != 0:
                    res = [res[1], res[0]]
            else:
                # https://bobbyhadz.com/blog/how-to-shift-rotate-list-in-python
                k = k % ll
                res = res[k + 1:] + res[:k + 1]
        head = h1
        for i in range(ll):
            head.val = res[i]
            head = head.next
        return h1

# Runtime 17 ms Beats 73.34%
# Memory 11.60 MB Beats 56.53%

# https://leetcode.com/problems/rotate-list/solutions/5227088/simple-python-solution-using-list-beats-95-running-time/
def rotateRight(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if head == None:
        return None
    elif k == 0:
        return head
    h1 = head;    res = []
    while head:
        res.append(head.val)
        head = head.next

    ll = len(res)
    # https://leetcode.com/problems/rotate-list/solutions/5227088/simple-python-solution-using-list-beats-95-running-time/
    if k >= ll:
        k -= (k // ll) * ll

    # Rotate the list
    res = res[ll - k:] + res[:ll - k]

    head = h1
    for i in range(ll):
        head.val = res[i]
        head = head.next
    return h1
