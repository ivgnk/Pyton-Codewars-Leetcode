'''
1317. Convert Integer to the Sum of Two No-Zero Integers
https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/description/

No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.
Given an integer n, return a list of two integers [a, b] where:
a and b are No-Zero integers.
a + b = n
The test cases are generated so that there is at least one valid solution.
If there are many valid solutions, you can return any of them.

Example 1:
Input: n = 2
Output: [1,1]
Explanation: Let a = 1 and b = 1.
Both a and b are no-zero integers, and a + b = 2 = n.

Example 2:
Input: n = 11
Output: [2,9]
Explanation: Let a = 2 and b = 9.
Both a and b are no-zero integers, and a + b = 9 = n.
Note that there are other valid answers as [8, 3] that can be accepted.
'''

# Runtime 18 ms Beats 67.19% of users with Python
# Memory 11.75 MB Beats 82.81% of users with Python

def getNoZeroIntegers(n):
    """
    :type n: int
    :rtype: List[int]
    """
    if n==2: return [1,1]
    if n == 3: return [1, 2]
    n1=n//2
    for i in range(1,n1):
        n2=n-i
        if '0' not in str(i) and '0' not in str(n2):
            return [i,n2]

print(getNoZeroIntegers(11))