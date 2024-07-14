"""
14.07.2024. Topics: Math, Binary Search

You have n coins and you want to build a staircase with these coins.
The staircase consists of k rows where the ith row has exactly i coins.
The last row of the staircase may be incomplete.
Given the integer n, return the number of complete rows of the staircase you will build.

Example 1:
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

Example 2:
Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
"""

def aprogr(n):
    return (2 + n-1)*n//2

def rev_aprogr(n):
    n*2-2

def arrangeCoins_(n):
    """
    :type n: int
    :rtype: int
    """
    for i in range(1,5):
        print(aprogr(i))


# https://leetcode.com/problems/arranging-coins/description/comments/1564663
# 1+2+3+...+x = n
# -> (1+x)x/2 = n
# -> x^2+x = 2n
# -> x^2+x+1/4 = 2n +1/4
# -> (x+1/2)^2 = 2n +1/4
# -> (x+0.5) = sqrt(2n+0.25)
# -> x = -0.5 + sqrt(2n+0.25)
#
# def arrangeCoins(n)
#   return floor(-0.5+sqrt(2*n+0.25))
#
# Runtime 14 ms Beats 89.84%
# Memory 11.66 MB Beats 23.77%

def arrangeCoins_2(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1: return 1
    return n%4

# Runtime 1193 ms Beats 5.08%
# Memory 11.57 MB Beats 56.35%
# Runtime 1105 ms Beats 5.08%
# Memory 11.52 MB Beats 56.35%
def arrangeCoins(n):
    if n == 1: return 1
    ssum=0; i=0
    while ssum<n:
        i=i+1
        ssum=aprogr(i)
    return i-1

print(arrangeCoins_2(8))