"""
Done 27.05.2024. Topics: Array, Math
204. Count Primes
https://leetcode.com/problems/count-primes/

Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0
"""

# Runtime 3093 ms Beats 20.72% of users with Python3
# Memory 68.98 MB Beats 44.19% of users with Python3

# Runtime 3042 ms Beats 21.33% of users with Python3
# Memory 68.88 MB Beats 44.66% of users with Python3
def countPrimes3(n):
    if n <= 1: return 0
    isq=isqrt(n)
    a=[True]*n
    for i in range(2,isq+1):
        if a[i]==True:
            j=0; nn=i**2
            while j<n:
                if nn <n:
                    a[nn]=False
                    j=j+1
                    nn=nn+i
                else: break
    return len([i for i in range(2,n) if a[i]])


# Runtime 3693 ms# Beats 14.41% of users with Python3
# Memory 68.90 MB Beats 44.19% of users with Python3

from math import isqrt
# https://ru.wikipedia.org/wiki/Решето_Эратосфена#Псевдокод
# https://ru.wikipedia.org/wiki/Решето_Эратосфена#Псевдокод_2
def countPrimes2(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 1: return 0
    isq=isqrt(n)
    a=[True]*n
    for i in range(2,isq+1):
        if a[i]==True:
            j=0; i2=i**2
            while j<n:
                nn=i2+j*i
                if nn <n:
                    a[nn]=False
                    j=j+1
                else: break
    res=[i for i in range(2,n) if a[i]]
    return len(res)

print(countPrimes(10))

