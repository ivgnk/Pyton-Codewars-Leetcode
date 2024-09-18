"""
Done 18.09.2024. Topics: Math
1922. Count Good Numbers
https://leetcode.com/problems/count-good-numbers/description/

A digit string is good if the digits (0-indexed) at even indices are even
and the digits at odd indices are prime (2, 3, 5, or 7).

For example, "2582" is good because the digits (2 and 8) at even positions are even
and the digits (5 and 2) at odd positions are prime.

However, "3245" is not good because 3 is at an even index but is not even.
Given an integer n, return the total number of good digit strings of length n.
Since the answer may be large, return it modulo 109 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

Example 1:
Input: n = 1
Output: 5
Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".

Example 2:
Input: n = 4
Output: 400

Example 3:
Input: n = 50
Output: 564908303

Constraints:
1 <= n <= 1015

Hint 1
Is there a formula we can use to find the count of all the good numbers?
Hint 2
Exponentiation can be done very fast if we looked at the binary bits of n.

https://leetcode.com/problems/count-good-numbers/description/comments/1575584
numbers for even positions - 0,2,4,6,8
numbers for odd positions - 2,3,5,7
n = 4 - 5*4*5*4 = 400

https://leetcode.com/problems/count-good-numbers/description/comments/1882025
N=1 odd index odd-index positions in the string will be one of the numbers (0, 2, 4, 6, 8) -> ans = 5
N=2 x0x1 -> ans = 5x4 (x1 will be one of (3,5,7,2))
N= 3 x0x1x2 -> ans = 5x4x5
N=4 x0x1x2x3 -> ans = 5x4x5x4
...
if N is odd: ans = 5^(n/2+1) * 4^(n/2),
if N is even: ans = 5^(n/2)*4^(n/2).

Solution
✏️ Not so obvious solution in Python

Intuition
Main hints
- https://leetcode.com/problems/count-good-numbers/description/comments/1575584
- https://leetcode.com/problems/count-good-numbers/description/comments/1882025

Approach
In the implementation, the main thing is to work correctly with large numbers. Modulo division is recommended.
Even if you do the division modulo for individual parts. it will still be TLE.
It is necessary to use the built-in pow() function, which can take an optional mode argument,
with which it raises a number to a power modulo.*
"""

# https://habr.com/ru/articles/823438/
# встроенная функция pow() также может принимать необязательный аргумент mod,
# с помощью которого она возводит число в степень по модулю.

# Runtime 30 ms Beats 88.44%
# Memory 16.51 MB Beats 52.98%
def countGoodNumbers(n):
    """
    :type n: int
    :rtype: int
    """
    n2=n//2
    modu=1000000007
    if n%2==0:
        p1=pow(5,n2,modu)
    else:
        p1=pow(5,n2+1,modu)
    p2=pow(4,n2,modu)
    s = p1 * p2
    return s%modu

print(countGoodNumbers(1))
print(countGoodNumbers(50))

def countGoodNumbers3(n):
    """
    :type n: int
    :rtype: int
    """
    n2=n//2
    modu=1000000007
    if n%2==0:
        p1=(5**n2)%modu
    else:
        p1=(5**(n2+1))%modu
    p2=(4**n2)%modu
    s = p1 * p2
    return s%modu

# Time Limit Exceeded - 69 / 166 testcases passed
def countGoodNumbers(n):
    n2=n//2
    if n%2==0:
        s=5**(n2) * 4**n2
    else:
        s=5**(n2+1) * 4**n2
    # https://www.geeksforgeeks.org/modulo-1097-1000000007/
    return s%1000000007
