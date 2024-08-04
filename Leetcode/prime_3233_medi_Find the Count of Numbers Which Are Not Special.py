"""
03.08.2024. Array, Math, Number Theory

3233. Find the Count of Numbers Which Are Not Special
https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/description/

You are given 2 positive integers l and r.
For any number x, all positive divisors of x except x are called the proper divisors of x.
A number is called special if it has exactly 2 proper divisors. For example:

The number 4 is special because it has proper divisors 1 and 2.
The number 6 is not special because it has proper divisors 1, 2, and 3.
Return the count of numbers in the range [l, r] that are not special.

Example 1:
Input: l = 5, r = 7
Output: 3
Explanation:
There are no special numbers in the range [5, 7].

Example 2:
Input: l = 4, r = 16
Output: 11
Explanation:
The special numbers in the range [4, 16] are 4 and 9.

Constraints:
1 <= l <= r <= 10**9

Hint 1
A special number must be a square of a prime number.
Hint 2
We need to find all primes in the range [sqrt(l), sqrt(r)].
Hint 3
Use sieve to find primes till sqrt(109).
"""

# Runtime 363 ms Beats 90.60%
# Memory 12.24 MB Beats 84.05%

import math

class Solution(object):
    def sieve_of_eratosthenes(self, limit):
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for start in range(2, int(math.sqrt(limit)) + 1):
            if is_prime[start]:
                for multiple in range(start*start, limit + 1, start):
                    is_prime[multiple] = False
        return [num for num, prime in enumerate(is_prime) if prime]

    def nonSpecialCount(self, l, r):
        upper_limit = int(math.sqrt(r)) + 1
        primes = self.sieve_of_eratosthenes(upper_limit)
        semi_primes = 0
        for i in range(len(primes)):
            semi_prime = primes[i]**2
            if l <= semi_prime <= r:
                semi_primes += 1
            if semi_prime > r: break
        return (r - l + 1) - semi_primes


from numba import jit
def get_primes(n):
    sieve = [True] * n
    primes = []
    for p in range(2, n):
        if sieve[p]:
            primes.append(p)
        for i in range(p * p, n, p):
            sieve[i] = False
    return primes

def nonSpecialCount(l, r):
    """
    :type l: int
    :type r: int
    :rtype: int
    """
    global pr_lst
    rght=int(math.sqrt(r))
    primes = get_primes(rght)



