"""
Done 19.06.2024. Topics: Math

1952. Three Divisors
https://leetcode.com/problems/three-divisors/description/

Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.
An integer m is a divisor of n if there exists an integer k such that n = k * m.

Example 1:
Input: n = 2
Output: false
Explantion: 2 has only two divisors: 1 and 2.

Example 2:
Input: n = 4
Output: true
Explantion: 4 has three divisors: 1, 2, and 4.
"""

# Runtime 19 ms Beats 58.57%
# Memory 11.86 MB Beats 58.17%
# Runtime 17 ms Beats 71.31%
# Memory 11.81 MB Beats 58.17%
# Runtime 16 ms Beats 76.49%
# Memory 11.96 MB Beats 31.08%

def isThree(n):
    """
    :type n: int
    :rtype: bool
    """
    if n<=2: return False
    nn=1
    for i in range(2,n+1):
        if n%i == 0:
            nn+=1
    return nn==3


# another algo
# https://leetcode.com/problems/three-divisors/description/comments/1896194
# https://leetcode.com/problems/three-divisors/description/comments/1967414