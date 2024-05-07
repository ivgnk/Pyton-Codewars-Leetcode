"""
Done 07.05.2024. Topics: Math, Two Pointers, Binary Search
633. Sum of Square Numbers
Given a non-negative integer c,
decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
Input: c = 3
Output: false
"""

# Runtime 58 ms Beats 76.40% of users with Python
# Memory 11.72 MB Beats 21.91%# of users with Python

# See also
# https://en.wikipedia.org/wiki/Pythagorean_triple
# https://en.wikipedia.org/wiki/Fermat%27s_theorem_on_sums_of_two_squares


from math import sqrt
def judgeSquareSum(c):
    """
    :type c: int
    :rtype: bool
    """
    i=0; j=int(sqrt(c))
    while i<j:
        n = i * i + j * j
        if n==c: return True
        if n>c: j=j-1
        else: i=i+1
    return False

print(judgeSquareSum(3))