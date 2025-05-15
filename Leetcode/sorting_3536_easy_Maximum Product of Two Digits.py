"""
Done 15.05.2025. Topics: Math, Sorting
3536. Maximum Product of Two Digits
https://leetcode.com/problems/maximum-product-of-two-digits

You are given a positive integer n.
Return the maximum product of any two digits in n.
Note: You may use the same digit twice if it appears more than once in n.

Example 1:
Input: n = 31
Output: 3
Explanation:
The digits of n are [3, 1].
The possible products of any two digits are: 3 * 1 = 3.
The maximum product is 3.

Example 2:
Input: n = 22
Output: 4
Explanation:
The digits of n are [2, 2].
The possible products of any two digits are: 2 * 2 = 4.
The maximum product is 4.

Example 3:
Input: n = 124
Output: 8
Explanation:
The digits of n are [1, 2, 4].
The possible products of any two digits are: 1 * 2 = 2, 1 * 4 = 4, 2 * 4 = 8.
The maximum product is 8.

Constraints:
10 <= n <= 109

Hint 1
Use brute force

My solution
✏️ Easy and fast (0 ms) Python solution
https://leetcode.com/problems/maximum-product-of-two-digits/solutions/6746356/easy-and-fast-0-ms-python-solution-by-iv-th1y/
Intuition
int -> str-list of str -> list of int -> sorting -> get two bigest int

Time Complexity O(NLogN)
Space Complexity O(N)

"""

# 4 ms Beats 50.90%
# Memory 12.27 MB Beats 99.10%
def maxProduct2(n):
    """
    :type n: int
    :rtype: int
    """
    s = list(str(n))
    ni = sorted(map(int, s), reverse=True)
    return ni[0] * ni[1]

# Runtime 0 ms Beats 100.00%
# Memory 12.35 MB Beats 80.90%
def maxProduct(n):
    """
    :type n: int
    :rtype: int
    """
    ni = sorted(map(int, list(str(n))), reverse=True)
    return ni[0] * ni[1]
