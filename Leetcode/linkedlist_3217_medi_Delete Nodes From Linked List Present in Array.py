"""
Done 14.07.2024.
You are given an array of integers nums and the head of a linked list.
Return the head of the modified linked list after removing all nodes
from the linked list that have a value that exists in nums.

Example 1:
Input: nums = [1,2,3], head = [1,2,3,4,5]
Output: [4,5]

Example 2:
Input: nums = [1], head = [1,2,1,2,1,2]
Output: [2,2,2]
Explanation:
Remove the nodes with value 1.

Example 3:
Input: nums = [5], head = [1,2,3,4]
Output: [1,2,3,4]
Explanation:
No node has value 5.

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 105
All elements in nums are unique.
The number of nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105
The input is generated such that there is at least one node in the linked list that has a value not present in nums.

Hint 1
Add all elements of nums into a Set.
Hint 2
Scan the list to check if the current element should be deleted by checking the Set.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time Limit Exceeded - 576 / 582 testcases passed
def modifiedList2(nums, head):
    """
    :type nums: List[int]
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    lst=[]
    while head:
        lst.append(head.val)
        head = head.next

    res = [j for j in lst if not (j in nums)]
    ll=len(res)
    if ll==0: return None
    else:
        temp=ListNode(res[0])
        if ll > 1:
            head = temp
            for i in range(1, ll):
                head.next = ListNode(res[i])
                head = head.next
        return temp

# Runtime 1887 ms Beats 100.00%
# Memory 136.15 MB Beats 100.00%
def modifiedList(nums, head):
    """
    :type nums: List[int]
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    res=[]
    n1=set(nums)
    while head:
        if head.val not in n1:
            res.append(head.val)
        head = head.next

    ll=len(res)
    if ll==0: return None
    else:
        temp=ListNode(res[0])
        if ll > 1:
            head = temp
            for i in range(1, ll):
                head.next = ListNode(res[i])
                head = head.next
        return temp




