"""
Done 19.08.2024. Topics: Math, Dynamic Programming
650. 2 Keys Keyboard
https://leetcode.com/problems/2-keys-keyboard/description

There is only one character 'A' on the screen of a notepad.
You can perform one of two operations on this notepad for each step:
Copy All: You can copy all the characters present on the screen
(a partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the character
'A' exactly n times on the screen.

Example 1:
Input: n = 3
Output: 3
Explanation: Initially, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.

Example 2:
Input: n = 1
Output: 0

Constraints:
1 <= n <= 1000

Hint 1
How many characters may be there in the clipboard at the last step
if n = 3? n = 7? n = 10? n = 24?


# https://leetcode.com/problems/2-keys-keyboard/description/comments/1930658
Solution
✏️ Easy Python solution without any difficulties based on prime factors
Intuition
Intuition from https://leetcode.com/problems/2-keys-keyboard/description/comments/1930658
by https://leetcode.com/u/kamiidaisuke/ :
"
we can solve it even without dynamic programming or recursion but with just simple mathematics like we have to just represt it in terms of prime factors and add it
for example in case of 24
24 = 2 * 2 * 2 * 3
and result = 2+2+2+3
and for something like 124
124 = 2 * 2 * 31
and the result is as you guesses = 2+2+31
"

Approach
Use function for calculating prime factors.
The function is specially placed outside the object.
Otherwise, the calculation time increases 2-3 times

Done 19.08.2024
Runtime 7 ms Beats 98.51%
Memory 11.78 MB Beats 31.34%
"""

# Runtime 7 ms Beats 98.51%
# Memory 11.78 MB Beats 31.34%


# https://pythonhint.com/post/1173869442130105/prime-factorization-list
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def minSteps(n):
    """
    :type n: int
    :rtype: int
    """

    return len(prime_factors(n))
