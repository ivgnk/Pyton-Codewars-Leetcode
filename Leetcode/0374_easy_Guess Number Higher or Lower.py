"""
Done 04.05.2024
374. Guess Number Higher or Lower
https://leetcode.com/problems/guess-number-higher-or-lower/description/

We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
You call a pre-defined API int guess(int num), which returns three possible results:
-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.
"""

NN = 50


def guess(n):
    if n==NN: return 0
    elif n>NN: return -1
    else: return 1

# Runtime 8 ms Beats 87.42% of users with Python
# Memory 11.70 MB Beats 35.38% of users with Python

def guessNumber(n):
    """
    :type n: int
    :rtype: int
    """
    nmin = 1
    nmax = 2**31 - 1
    if guess(nmax)==0: return nmax
    elif guess(nmin)==0: return nmin
    n = nmax // 2
    while True:
        s = guess(n)
        print(nmin, nmax, n,s)
        if s == 0:
            return n
        elif s > 0:
            nmin = n
            n = (nmax + nmin) // 2
        else:
            nmax = n
            n = (nmax + nmin) // 2

print(guessNumber(1000))