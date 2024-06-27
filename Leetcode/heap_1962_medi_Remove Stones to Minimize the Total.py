"""
Done 27.06.2024. Topics: Array, Heap (Priority Queue)
1962. Remove Stones to Minimize the Total
https://leetcode.com/problems/remove-stones-to-minimize-the-total/description/

You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the ith pile,
and an integer k. You should apply the following operation exactly k times:
Choose any piles[i] and remove floor(piles[i] / 2) stones from it.
Notice that you can apply the operation on the same pile more than once.
Return the minimum possible total number of stones remaining after applying the k operations.
floor(x) is the greatest integer that is smaller than or equal to x (i.e., rounds x down).

Example 1:
Input: piles = [5,4,9], k = 2
Output: 12
Explanation: Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [5,4,5].
- Apply the operation on pile 0. The resulting piles are [3,4,5].
The total number of stones in [3,4,5] is 12.

Example 2:
Input: piles = [4,3,6,7], k = 3
Output: 12
Explanation: Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [4,3,3,7].
- Apply the operation on pile 3. The resulting piles are [4,3,3,4].
- Apply the operation on pile 0. The resulting piles are [2,3,3,4].
The total number of stones in [2,3,3,4] is 12.


Hint 1
Choose the pile with the maximum number of stones each time.
Hint 2
Use a data structure that helps you find the mentioned pile each time efficiently.
Hint 3
One such data structure is a Priority Queue.
"""

from heapq import *
# on the base of
# https://leetcode.com/problems/remove-stones-to-minimize-the-total/solutions/4802110/python-solution-using-heap/
# Runtime 3656 ms Beats 61.63%
# Memory 24.23 MB Beats 36.05%
def minStoneSum(piles, k):
    g = [-x for x in piles]
    heapify(g)
    for i in range(k):
        p = -heappop(g)
        heappush(g, -p//2)
    return sum(-x for x in g)

# Runtime 3613 ms Beats 66.28%
# Memory 23.78 MB Beats 73.26%
# Runtime 3485 ms Beats 75.58%
# Memory 24.22 MB Beats 36.05%
def minStoneSum3(piles, k):
    """
    :type piles: List[int]
    :type k: int
    :rtype: int
    """
    g = [-x for x in piles]
    heapify(g)
    for i in range(k):
        heappush(g, heappop(g)//2)
    return sum(-x for x in g)


# Time Limit Exceeded - 45 / 59 testcases passed
from math import floor
def minStoneSum2(piles, k):
    """
    :type piles: List[int]
    :type k: int
    :rtype: int
    """
    for i in range(k):
        mmax=max(piles)
        ind = piles.index(mmax)
        piles[ind]=piles[ind]-mmax//2
    return sum(piles)

print(minStoneSum(piles = [5,4,9], k = 2))
print(minStoneSum(piles = [4,3,6,7], k = 3))