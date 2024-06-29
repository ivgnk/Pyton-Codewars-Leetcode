"""
Done 29.06.2024. Topics: Math
1837. Sum of Digits in Base K
https://leetcode.com/problems/sum-of-digits-in-base-k/description/

Given an integer n (in base 10) and a base k,
return the sum of the digits of n after converting n from base 10 to base k.
After converting, each digit should be interpreted as a base 10 number,
and the sum should be returned in base 10.

Example 1:
Input: n = 34, k = 6
Output: 9
Explanation: 34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.

Example 2:
Input: n = 10, k = 10
Output: 1
Explanation: n is already in base 10. 1 + 0 = 1.

Constraints:
1 <= n <= 100

Hint 1
Convert the given number into base k.
Hint 2
Use mod-10 to find what each digit is after the conversion and sum the digits.
"""


# Runtime 16 ms Beats 27.55%
# Memory 11.47 MB Beats 89.80%
# Runtime 8 ms Beats 89.80%
# Memory 11.58 MB Beats 63.27%
def sumBase(n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """
    # https://ru.stackoverflow.com/questions/1297746/Перевод-систем-счисления
    ssum=0
    while n > 0:
        ssum = ssum+n % k
        n = n // k
    return ssum


print(sumBase(34,6))
print(sumBase(10,10))