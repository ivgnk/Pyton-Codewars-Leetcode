"""
Done 04.08.2024. Topics: Hash Table
3238. Find the Number of Winning Players
https://leetcode.com/problems/find-the-number-of-winning-players/description/

You are given an integer n representing the number of players in a game and a 2D array pick where
pick[i] = [xi, yi] represents that the player xi picked a ball of color yi.

Player i wins the game if they pick strictly more than i balls of the same color. In other words,
Player 0 wins if they pick any ball.
Player 1 wins if they pick at least two balls of the same color.
...
Player i wins if they pick at leasti + 1 balls of the same color.
Return the number of players who win the game.

Note that multiple players can win the game.

Example 1:
Input: n = 4, pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]
Output: 2
Explanation:
Player 0 and player 1 win the game, while players 2 and 3 do not win.

Example 2:
Input: n = 5, pick = [[1,1],[1,2],[1,3],[1,4]]
Output: 0
Explanation:
No player wins the game.

Example 3:
Input: n = 5, pick = [[1,1],[2,4],[2,4],[2,4]]
Output: 1
Explanation:
Player 2 wins the game by picking 3 balls with color 4.

Constraints:

2 <= n <= 10
1 <= pick.length <= 100
pick[i].length == 2
0 <= xi <= n - 1
0 <= yi <= 10

as hint https://leetcode.com/problems/find-the-number-of-winning-players/description/comments/2555197
This problem involves hash tables and is relatively straightforward.
The number of players 𝑛 n isn't critical to solving the question.

Hint: Consider the list pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]].
ht = {(0, 0): 1, (1, 0): 2, (2, 1): 2, (2, 0): 1}

The task is to determine the number of unique pairs where the first element of the pair (i[0]) is
greater than its value in the hash table.
"""
# Runtime 121 ms Beats 100.00%
# Memory 11.58 MB Beats 100.00%

# Easy Python step-by-step solution
from icecream import ic
def winningPlayerCount(n, pick):
    """
    :type n: int
    :type pick: List[List[int]]
    :rtype: int
    """
    # Get a list of players with a ball of each color
    # That is, to get a dictionary where the value is a list
    dd=dict() # Ball: [players]
    for d in pick:
        if d[1] in dd:
            dd[d[1]].append(d[0])
        else:
            dd[d[1]] = [d[0]]

    # Going through the dictionary to determine the number of winning players.
    #
    nwin=set()
    for k,v in dd.items():
        ss=set(v) # чтобы еще раз не вводить hash
        for ss1 in ss:
            if ss1==0: nwin.add(ss1)
            elif v.count(ss1) >ss1:
                nwin.add(ss1)
    return len(nwin)

ic(winningPlayerCount(4,[[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]))
ic(winningPlayerCount( n = 5, pick = [[1,1],[1,2],[1,3],[1,4]]))
ic(winningPlayerCount( n = 5, pick = [[1,1],[2,4],[2,4],[2,4]]))

