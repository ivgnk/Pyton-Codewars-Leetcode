"""
Done 11.11.2024.
3345. Smallest Divisible Digit Product I
https://leetcode.com/problems/smallest-divisible-digit-product-i/description/

You are given two integers n and t.
Return the smallest number greater than or equal to n such that the product
of its digits is divisible by t

Example 1:
Input: n = 10, t = 2
Output: 10
Explanation:
The digit product of 10 is 0, which is divisible by 2, making it the smallest number greater than or equal to 10 that satisfies the condition.

Example 2:
Input: n = 15, t = 3
Output: 16
Explanation:
The digit product of 16 is 6, which is divisible by 3, making it the smallest number greater than or equal to 15 that satisfies the condition.

Constraints:
1 <= n <= 100
1 <= t <= 10

Hint 1
You have to check at most 10 numbers.
Hint 2
Apply a brute-force approach by checking each possible number.
"""
# Runtime 3 ms Beats 100.00%
# Memory 16.79 MB Beats 100.00%
from math import prod
def smallestNumber(n, t):
    """
    :type n: int
    :type t: int
    :rtype: int
    """
    for i in range(n,1000,1):
        pr=prod([int(s1) for s1 in str(i)])
        if pr%t==0: return i

# print(smallestNumber(10,2))
# print(smallestNumber(15,3))
print(smallestNumber(1,3))
# print(1%3)
# print(2%3)


