"""
Done 27.07.2024. Topics: Heap (Priority Queue)
You have a water dispenser that can dispense cold, warm, and hot water.
Every second, you can either fill up 2 cups with different types of water, or 1 cup of any type of water.

You are given a 0-indexed integer array amount of length 3 where amount[0], amount[1], and amount[2]
denote the number of cold, warm, and hot water cups you need to fill respectively.
Return the minimum number of seconds needed to fill up all the cups.

Example 1:
Input: amount = [1,4,2]
Output: 4
Explanation: One way to fill up the cups is:
Second 1: Fill up a cold cup and a warm cup.
Second 2: Fill up a warm cup and a hot cup.
Second 3: Fill up a warm cup and a hot cup.
Second 4: Fill up a warm cup.
It can be proven that 4 is the minimum number of seconds needed.

Example 2:
Input: amount = [5,4,4]
Output: 7
Explanation: One way to fill up the cups is:
Second 1: Fill up a cold cup, and a hot cup.
Second 2: Fill up a cold cup, and a warm cup.
Second 3: Fill up a cold cup, and a warm cup.
Second 4: Fill up a warm cup, and a hot cup.
Second 5: Fill up a cold cup, and a hot cup.
Second 6: Fill up a cold cup, and a warm cup.
Second 7: Fill up a hot cup.

Example 3:
Input: amount = [5,0,0]
Output: 5
Explanation: Every second, we fill up a cold cup.

Constraints:
amount.length == 3
0 <= amount[i] <= 100

Hint 1
To minimize the amount of time needed, you want to fill up as many cups as possible in each second. This means that you want to maximize the number of seconds where you are filling up two cups.
Hint 2
You always want to fill up the two types of water with the most unfilled cups.
"""

# Модуль heapq, кучи в Python
# https://docs-python.ru/standart-library/modul-heapq-python/

import heapq
# Runtime 19 ms Beats 42.86%
# Memory 11.65 MB Beats 35.71%
def fillCups(amount):
    """
    :type amount: List[int]
    :rtype: int
    """
    if list(set(amount)) == [0]: return 0

    amount=[-s for s in amount]
    heapq.heapify(amount)
    ll=len(amount); n=0
    while ll>1:
        a = heapq.heappop(amount) + 1
        b = heapq.heappop(amount) + 1
        n=n+1
        if a < 0:  heapq.heappush(amount, a)
        if b < 0:  heapq.heappush(amount, b)
        ll = len(amount)
    if ll>0:
        return n - amount[0]
    if ll==0:
        return n

print(fillCups([1,4,2]))
print(fillCups([5,4,4]))
print(fillCups([5,0,0]))

