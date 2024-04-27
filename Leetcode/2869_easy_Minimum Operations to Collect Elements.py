"""
Done 27.04.2024

2869. Minimum Operations to Collect Elements
https://leetcode.com/problems/minimum-operations-to-collect-elements/description/

You are given an array nums of positive integers and an integer k.
In one operation, you can remove the last element of the array and add it to your collection.
Return the minimum number of operations needed to collect elements 1, 2, ..., k.

Example 1:
Input: nums = [3,1,5,4,2], k = 2
Output: 4
Explanation: After 4 operations, we collect elements 2, 4, 5, and 1, in this order.
Our collection contains elements 1 and 2. Hence, the answer is 4.

Example 2:
Input: nums = [3,1,5,4,2], k = 5
Output: 5
Explanation: After 5 operations, we collect elements 2, 4, 5, 1, and 3, in this order.
Our collection contains elements 1 through 5. Hence, the answer is 5.

Example 3:
Input: nums = [3,2,5,3,1], k = 3
Output: 4
Explanation: After 4 operations, we collect elements 1, 3, 5, and 2, in this order.
Our collection contains elements 1 through 3. Hence, the answer is 4.
"""


def minOperations(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # Runtime 14 ms Beats 96.15% of users with Python
    # Memory 11.62 MB Beats 44.23% of users with Python
    res=set(); rr=range(1,k+1); n=0
    while len(res) != k:
        if nums[-1] in rr and nums[-1] not in res:
            res.add(nums[-1])
        nums.pop()
        n=n+1
    return n

def minOperations2(nums, k):
    # Runtime 18 ms Beats 80.77% of users with Python
    # Memory 11.67 MB Beats 44.23% of users with Python
    res = set();    rr = range(1, k + 1)
    n = 0;    ind = 1
    while len(res) != k:
        if nums[-ind] in rr and nums[-ind] not in res:
            res.add(nums[-ind])
        ind = ind + 1
        n = n + 1
    return n

print(minOperations([1,2,2], k = 2))