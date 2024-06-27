"""
Done 27.06.2024. Topics: Array, Heap (Priority Queue)
2558. Take Gifts From the Richest Pile

You are given an integer array gifts denoting the number of gifts in various piles.
Every second, you do the following:
- Choose the pile with the maximum number of gifts.
- If there is more than one pile with the maximum number of gifts, choose any.
- Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.
Return the number of gifts remaining after k seconds.

Вам дан целочисленный массив подарков, обозначающий количество подарков в различных стопках.
Каждую секунду вы делаете следующее: Выбираете стопку с максимальным количеством подарков.
Если стопок с максимальным количеством подарков больше одной, выбирайте любую.
Оставьте после себя квадратный корень из количества подарков в стопке.
Возьмите остальные подарки. Возвращает количество подарков, оставшихся через k секунд.

Hint 1
How can you keep track of the largest gifts in the array
Hint 2
What is an efficient way to find the square root of a number?
Hint 3
Can you keep adding up the values of the gifts while ensuring they are in a certain order?
Hint 4
Can we use a priority queue or heap here?
"""

# Runtime 44 ms Beats 82.31%
# Memory 16.96 MB Beats 8.50%
from heapq import *
def pickGifts(gifts, k):
    g = [-x for x in gifts]
    heapify(g)
    for i in range(k):
        heappush(g, -isqrt(-heappop(g)))
    return sum(-x for x in g)

# Runtime 100 ms Beats 28.23%
# Memory 16.28 MB Beats 100.00%
def pickGifts2(gifts, k):
    """
    :type gifts: List[int]
    :type k: int
    :rtype: int
    """
    for i in range(k):
        mmax=max(gifts)
        gifts[gifts.index(mmax)]=isqrt(mmax)
    return sum(gifts)


# Runtime 113 ms Beats 15.65%
# Memory 16.66 MB Beats 73.47%
# Runtime 109 ms Beats 20.58%
# Memory 16.61 MB Beats 73.47%
# Runtime 105 ms Beats 23.98%
# Memory 16.64 MB Beats 73.47%
from math import isqrt
def pickGifts2(gifts, k):
    """
    :type gifts: List[int]
    :type k: int
    :rtype: int
    """
    for i in range(k):
        mmax=max(gifts)
        ind=gifts.index(mmax)
        gifts[ind]=isqrt(mmax)
    return sum(gifts)

print(pickGifts(gifts = [25,64,9,4,100], k = 4))
print(pickGifts(gifts = [1,1,1,1], k = 4))