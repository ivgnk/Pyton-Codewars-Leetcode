"""
Done 27.11.2024
3360. Stone Removal Game
https://leetcode.com/problems/stone-removal-game/description/

Alice and Bob are playing a game where they take turns removing stones from a pile, with Alice going first.
Alice starts by removing exactly 10 stones on her first turn.
For each subsequent turn, each player removes exactly 1 fewer stone than the previous opponent.
The player who cannot make a move loses the game.
Given a positive integer n, return true if Alice wins the game and false otherwise.


Example 1:
Input: n = 12
Output: true
Explanation:
Alice removes 10 stones on her first turn, leaving 2 stones for Bob.
Bob cannot remove 9 stones, so Alice wins.

Example 2:
Input: n = 1
Output: false
Explanation:

Alice cannot remove 10 stones, so Alice loses.

Constraints:
1 <= n <= 50

My solution ✏️ Fast (0 ms) and easy Python solution for Problem 3360
https://leetcode.com/problems/stone-removal-game/solutions/6089438/fast-0-ms-and-easy-python-solution-for-problem-3360/

Intuition
Use cycle while and flaf for win indication
"""
# Runtime 0 ms Beats 100.00%
# Memory 12.08 MB Beats 10.06%
# Time Complexity O(N)
# Space Complexity O(1)
def canAliceWin(n):
    """
    :type n: int
    :rtype: bool
    """
    k = 10;    a = False
    if n < k: return a
    while n >= k:
        n -= k
        k -= 1
        a = not a
    return a

