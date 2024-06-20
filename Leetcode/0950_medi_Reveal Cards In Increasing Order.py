"""
Done 21.06.2024. Topics: Array, Queue, Sorting, Simulation

950. Reveal Cards In Increasing Order
https://leetcode.com/problems/reveal-cards-in-increasing-order/description/

You are given an integer array deck. There is a deck of cards where every card has a unique integer.
The integer on the ith card is deck[i].

You can order the deck in any order you want. Initially, all the cards start face down (unrevealed) in one deck.

You will do the following steps repeatedly until all cards are revealed:

Take the top card of the deck, reveal it, and take it out of the deck.
If there are still cards in the deck then put the next top card of the deck at the bottom of the deck.
If there are still unrevealed cards, go back to step 1. Otherwise, stop.
Return an ordering of the deck that would reveal the cards in increasing order.

Note that the first entry in the answer is considered to be the top of the deck.

Example 1:
Input: deck = [17,13,11,2,3,5,7]
Output: [2,13,3,11,5,17,7]
Explanation:
We get the deck in the order [17,13,11,2,3,5,7] (this order does not matter), and reorder it.
After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
We reveal 13, and move 17 to the bottom.  The deck is now [17].
We reveal 17.
Since all the cards revealed are in increasing order, the answer is correct.

Example 2:
Input: deck = [1,1000]
Output: [1,1000]
"""


# https://leetcode.com/problems/reveal-cards-in-increasing-order/solutions/504896/java-solution-without-queue/
# [fill, skip, fill, skip, fill, skip, fill]
# [2,    _,    3,    _,    5,    _,    7]
# The last status is 'fill', next status should be 'skip'
#     skip,     fill,     skip
# [2,  _,   3,  11,   5,   _,   7]
# The last status is 'skip', so the next status should be 'fill'
# 	  fill,           skip
# [2,   13,   3, 11, 5,  _,   7]
# The last status is 'skip', so the next status should be 'fill'
#                    fill
# [2, 13, 3, 11, 5,  17,   7]

# Runtime 34 ms Beats 15.79%
# Memory 11.70 MB Beats 86.40%
# Runtime 26 ms Beats 61.84%
# Memory# 11.71 MB Beats 86.40%
def deckRevealedIncreasing(deck):
    """
    :type deck: List[int]
    :rtype: List[int]
    """
    d1=sorted(deck)
    ll=len(deck)
    res=[0.5]*ll
    if ll<3: return d1
    else:
        n=0; wrk=True
        num=0
        while n<ll:
            # print(n,num,res)
            if res[num]!=0.5:
                num = (num + 1)%ll
                continue
            if wrk:
                res[num]=d1[n]
                n=n+1
            num = (num + 1)%ll
            wrk=not wrk
    return res

print(deckRevealedIncreasing([17,13,11,2,3,5,7]))  # [2,13,3,11,5,17,7]


