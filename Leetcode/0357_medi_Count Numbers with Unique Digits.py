"""
Done 16.09.2024. Topics: Math
357. Count Numbers with Unique Digits
https://leetcode.com/problems/count-numbers-with-unique-digits/description/

Given an integer n, return the count of all numbers with unique digits, x,
where 0 <= x < 10n.

Example 1:
Input: n = 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99

Example 2:
Input: n = 0
Output: 1

Constraints:
0 <= n <= 8

Hint 1
A direct way is to use the backtracking approach.
Hint 2
Backtracking should contains three states which are
(the current number, number of steps to get that number and a
bitmask which represent which number is marked as visited so far in the current number).
Start with state (0,0,0) and count all valid number till we reach number of steps equals to 10n.
Hint 3
This problem can also be solved using a dynamic programming approach and some knowledge of combinatorics.
Hint 4
Let f(k) = count of numbers with unique digits with length equals k.
Hint 5
f(1) = 10, ..., f(k) = 9 * 9 * 8 * ... (9 - k + 2) [The first factor is 9 because a number cannot start with 0].
"""

# Runtime 7 ms Beats 93.68%
# Memory 11.76 MB Beats 10.92%
def countNumbersWithUniqueDigits4(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0:        return 1
    elif n == 1:        return 10
    elif n == 2:        return 91
    elif n == 3:        return 739
    elif n == 4:        return 5275
    elif n == 5:        return 32491
    elif n == 6:        return 168571
    elif n == 7:        return 712891
    elif n == 8:        return 2345851

# Runtime 12 ms Beats 54.60%
# Memory 11.54 MB Beats 67.24%
ff=[1,10]
def countNumbersWithUniqueDigits(n):
    if n == 0: return ff[0]
    elif n == 1: return ff[1]
    elif n == 2:
        ff.append(9*9+ff[n-1])
        return ff[n]
    elif n == 3:
        ff.append(9*9*8+ff[n-1])
        return ff[n]
    elif n == 4:
        ff.append(9*9*8*7+ff[n-1])
        return ff[n]
    elif n == 5:
        ff.append(9*9*8*7*6+ff[n-1])
        return ff[n]
    elif n == 6:
        ff.append(9 * 9 * 8 * 7 * 6 * 5 + ff[n-1])
        return ff[n]
    elif n == 7:
        ff.append(9 * 9 * 8 * 7 * 6 * 5 * 4 + ff[n - 1])
        return ff[n]
    elif n == 8:
        ff.append(9 * 9 * 8 * 7 * 6 * 5 * 4 * 3 + ff[n - 1])
        return ff[n]


for i in range(9):
    print(i,countNumbersWithUniqueDigits(i))

# Time Limit Exceeded - 6 / 9 testcases passed
from collections import Counter
def countNumbersWithUniqueDigits2(n):
    """
    :type n: int
    :rtype: int
    """

    if n == 0:        return 1
    elif n == 1:        return 10
    elif n == 2:        return 91
    nn = 10 ** n;    num = 0
    for i in range(nn):
        s = str(i)
        dd = dict(Counter(s))
        num += all(v == 1 for k, v in dd.items())
    return num

