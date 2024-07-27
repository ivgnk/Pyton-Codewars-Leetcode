"""
Done 27.07.2024. Topics: Math, Greedy
1753. Maximum Score From Removing Stones
https://leetcode.com/problems/maximum-score-from-removing-stones/

You are playing a solitaire game with three piles of stones of sizes a, b, and c respectively.
Each turn you choose two different non-empty piles, take one stone from each, and add 1 point to your score.
The game stops when there are fewer than two non-empty piles (meaning there are no more available moves).

Given three integers a, b, and c, return the maximum score you can get.

Example 1:
Input: a = 2, b = 4, c = 6
Output: 6
Explanation: The starting state is (2, 4, 6). One optimal set of moves is:
- Take from 1st and 3rd piles, state is now (1, 4, 5)
- Take from 1st and 3rd piles, state is now (0, 4, 4)
- Take from 2nd and 3rd piles, state is now (0, 3, 3)
- Take from 2nd and 3rd piles, state is now (0, 2, 2)
- Take from 2nd and 3rd piles, state is now (0, 1, 1)
- Take from 2nd and 3rd piles, state is now (0, 0, 0)
There are fewer than two non-empty piles, so the game ends. Total: 6 points.

Example 2:
Input: a = 4, b = 4, c = 6
Output: 7
Explanation: The starting state is (4, 4, 6). One optimal set of moves is:
- Take from 1st and 2nd piles, state is now (3, 3, 6)
- Take from 1st and 3rd piles, state is now (2, 3, 5)
- Take from 1st and 3rd piles, state is now (1, 3, 4)
- Take from 1st and 3rd piles, state is now (0, 3, 3)
- Take from 2nd and 3rd piles, state is now (0, 2, 2)
- Take from 2nd and 3rd piles, state is now (0, 1, 1)
- Take from 2nd and 3rd piles, state is now (0, 0, 0)
There are fewer than two non-empty piles, so the game ends. Total: 7 points.

Example 3:
Input: a = 1, b = 8, c = 8
Output: 8
Explanation: One optimal set of moves is to take from the 2nd and 3rd piles for 8 turns until they are empty.
After that, there are fewer than two non-empty piles, so the game ends.

Constraints:
1 <= a, b, c <= 105

Hint 1
It's optimal to always remove one stone from the biggest 2 piles
Hint 2
Note that the limits are small enough for simulation
"""

# Runtime 435 ms Beats 23.08%
# Memory 11.55 MB Beats 52.31%
# Runtime 423 ms Beats 23.08%
# Memory 11.45 MB Beats 84.62%

def maximumScore(a, b, c):
    n=0; am=sorted([a,b,c])
    ll = 3 - am.count(0)
    while ll>1:
        am[-1] = am[-1] - 1
        am[-2] = am[-2] - 1
        am=sorted(am)
        n=n+1
        ll = 3 - am.count(0)
    return n

print(maximumScore(a = 2, b = 4, c = 6)) # 6
print(maximumScore(a = 4, b = 4, c = 6)) # 7
print(maximumScore(a = 1, b = 8, c = 8)) # 8

# Runtime 848 ms Beats 9.23%
# Memory 11.66 MB Beats 16.92%
import heapq
def maximumScore2(a, b, c):
    """
    :type a: int
    :type b: int
    :type c: int
    :rtype: int
    """
    amount=[a,b,c]
    # if list(set(amount)) == [0]: return 0

    amount=[-s for s in amount]
    heapq.heapify(amount)
    ll=3 - amount.count(0)
    n=0
    while ll>1:
        a=heapq.heappop(amount)
        b=heapq.heappop(amount)
        heapq.heappush(amount, a+1)
        heapq.heappush(amount, b+1)
        n=n+1
        ll = 3 - amount.count(0)
    return n


