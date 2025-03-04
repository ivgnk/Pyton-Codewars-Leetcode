"""
04.03.2025. Topics: Math
1780. Check if Number is a Sum of Powers of Three

Given an integer n, return true if it is possible to represent n as the sum of
distinct powers of three. Otherwise, return false.
An integer y is a power of three if there exists an integer x such that y == 3x.

Example 1:
Input: n = 12
Output: true
Explanation: 12 = 31 + 32

Example 2:
Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34

Example 3:
Input: n = 21
Output: false

Constraints:
1 <= n <= 10**7

Hint 1
Let's note that the maximum power of 3 you'll use in your soln is 3^16
Hint 2
The number can not be represented as a sum of powers of 3 if it's ternary presentation has a 2 in it
"""

# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/
def checkPowersOfThree(n):
    """
    :type n: int
    :rtype: bool
    """
    while n > 0:
        if n % 3 == 2:
            return False
        n = n // 3
    return True


print(checkPowersOfThree(12))
print(checkPowersOfThree(91))
print(checkPowersOfThree(21))