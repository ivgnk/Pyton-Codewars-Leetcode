"""
Done 26.07.2024. Topics: Array, Heap (Priority Queue)
1046. Last Stone Weight
https://leetcode.com/problems/last-stone-weight/description/

You are given an array of integers stones where stones[i] is the weight of the ith stone.
We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together.
Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

Example 2:
Input: stones = [1]
Output: 1

Constraints:
1 <= stones.length <= 30
1 <= stones[i] <= 1000

Hint 1
Simulate the process.
We can do it with a heap, or by sorting some list of stones every time we take a turn.
"""

# Runtime 14 ms Beats 69.89%
# Memory 11.65 MB Beats 45.54%

def lastStoneWeight2(stones):
    """
    :type stones: List[int]
    :rtype: int
    """
    ll=len(stones)
    while ll>1:
        stones.sort()
        x=stones.pop()
        y=stones.pop()
        if x>y:
            stones.append(x - y)
        elif x<y:
            stones.append(y - x)
        ll=len(stones)
    if ll==1: return stones[0]
    else: return 0

import heapq
def lastStoneWeight(stones):
    heapq.heapify(stones)
    ll=len(stones)
    while ll>1:
        if ll == 1:
            return stones[0]
        else:
            return 0


print(lastStoneWeight([2,7,4,1,8,1]))
print(lastStoneWeight([1]))