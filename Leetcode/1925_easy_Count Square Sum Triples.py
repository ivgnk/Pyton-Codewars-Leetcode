"""
Done 24.06.2024. Topics: Math, Enumeration
1925. Count Square Sum Triples
https://leetcode.com/problems/count-square-sum-triples/description/

A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.
Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.

Example 1:
Input: n = 5
Output: 2
Explanation: The square triples are (3,4,5) and (4,3,5).

Example 2:
Input: n = 10
Output: 4
Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).

Constraints:
1 <= n <= 250

Hint 1
Iterate over all possible pairs (a,b) and check that the square root of a * a + b * b is an integers less than or equal n
Hint 2
You can check that the square root of an integer is an integer using binary seach or a builtin function like sqrt
"""


# Runtime 6561 ms Beats 7.14%
# Memory 11.50 MB Beats 90.82%
def countTriples3(n):
    """
    :type n: int
    :rtype: int
    """
    rr = range(1, n + 1);   n2 = 0;  n1 = n + 1
    arr = [i * i for i in range(1, n1)]
    for i in rr:
        for j in rr:
            ll = arr[i - 1] + arr[j - 1]
            for k in range(j + 1, n1):
                if arr[k - 1] == ll:
                    n2 = n2 + 1
    return n2


# Runtime 248 ms Beats 63.27%
# Memory 11.56 MB Beats 64.29%
from math import sqrt
def countTriples(n):
    """
    :type n: int
    :rtype: int
    """
    rr = range(1, n + 1);   n2 = 0;  n1 = n + 1
    arr = [i * i for i in range(1, n1)]; n22=n*n

    for i in rr:
        i1 = i - 1
        for j in rr:
            ll = arr[i1] + arr[j - 1]
            lls = sqrt(ll)
            if lls % 1 == 0 and lls <= n:
                n2 = n2 + 1
    return n2

print(countTriples(5)) # 2
print(countTriples(10)) # 4
# print(countTriples(247))


