"""
27.09.2024. Topics: Math
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/description/

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45

Hint 1
To reach nth step, what could have been your previous steps? (Think about the step sizes)
"""

# https://leetcode.com/problems/climbing-stairs/solutions/5835311/python3-with-explanation/
# Intuition
# n stairs in toal, find the number of ways to climb if you can climb one or two steps each time.
#
# Approach
# if n == 1: 1 way
# if n == 2: 2 ways
# if n == 3: 1 + 2 ways
# if n== 4: 2 + 3 ways
# image Fibonacci: 1, 1, 2, 3, 5, 8.....

# Runtime 16 ms Beats 32.42%
# Memory 11.54 MB Beats 72.51%
def climbStairs5(n):
    a = 0
    b = 1
    for i in range(n):
        temp = a
        a = b
        b += temp
    return b

# https://leetcode.com/problems/climbing-stairs/solutions/5832570/climbing-stairs/
def climbStairs5(n):
    if n == 1:
        return 1
    a = 1
    b = 1
    c = 0
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return c

# https://leetcode.com/problems/climbing-stairs/solutions/5831590/easy-solution/
def climbStairs(self, n: int) -> int:
    fib = [0] * (n + 1)
    fib[0] = 1
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

# https://leetcode.com/problems/climbing-stairs/solutions/5830136/it-s-like-a-fibonacci/
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        else:
            prev1 = 1
            prev2 = 2
            current = 0

            for _ in range(2, n):
                current = prev1 + prev2
                prev1 = prev2
                prev2 = current

            return current
