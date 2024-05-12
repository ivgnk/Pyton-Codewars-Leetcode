"""
Done 12.05.2024. Topics: Array, Hash Table, Counting
2347. Best Poker Hand
https://leetcode.com/problems/best-poker-hand/description/

You are given an integer array ranks and a character array suits.
You have 5 cards where the ith card has a rank of ranks[i] and a suit of suits[i].

The following are the types of poker hands you can make from best to worst:

"Flush": Five cards of the same suit.
"Three of a Kind": Three cards of the same rank.
"Pair": Two cards of the same rank.
"High Card": Any single card.
Return a string representing the best type of poker hand you can make with the given cards.

Note that the return values are case-sensitive.

Example 1:
Input: ranks = [13,2,3,1,9], suits = ["a","a","a","a","a"]
Output: "Flush"
Explanation: The hand with all the cards consists of 5 cards with the same suit, so we have a "Flush".

Example 2:
Input: ranks = [4,4,2,4,4], suits = ["d","a","a","b","c"]
Output: "Three of a Kind"
Explanation: The hand with the first, second, and fourth card consists of 3 cards with the same rank, so we have a "Three of a Kind".
Note that we could also make a "Pair" hand but "Three of a Kind" is a better hand.
Also note that other cards could be used to make the "Three of a Kind" hand.

Example 3:
Input: ranks = [10,10,2,12,9], suits = ["a","b","c","a","d"]
Output: "Pair"
Explanation: The hand with the first and second card consists of 2 cards with the same rank, so we have a "Pair".
Note that we cannot make a "Flush" or a "Three of a Kind".
"""

# Runtime 9 ms Beats 86.54% of users with Python
# Memory 11.80 MB Beats 26.92% of users with Python

from collections import Counter
def bestHand(ranks, suits):
    """
    :type ranks: List[int]
    :type suits: List[str]
    :rtype: str
    """
    ll=len(ranks)
    alls=[suits[i]==suits[i-1] for i in range(1,ll)]
    if all(alls): return "Flush"
    dd=dict(Counter(ranks))
    rr = [v for k,v in dd.items()]
    # print(dd); print(rr, 3 in rr)
    if max(rr)>=3: return "Three of a Kind"
    if 2 in rr: return "Pair"
    return "High Card"

print(bestHand(ranks = [4,4,2,4,4], suits = ["d","a","a","b","c"]))
# print(3 in [4, 1])