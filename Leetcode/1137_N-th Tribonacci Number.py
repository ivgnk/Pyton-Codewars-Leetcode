'''
1137. N-th Tribonacci Number
The Tribonacci sequence Tn is defined as follows:
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
'''

# Runtime 4 ms Beats 98.04% of users with Python
# Memory 11.60 MB Beats 72.16% of users with Python

def tribonacci(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0: return 0
    if n == 1 or n == 2: return 1
    T0 = 0;    T1 = 1;    T2 = 1;   i = 3
    while i <= n:
        Tn = T0 + T1 + T2
        T0 = T1;  T1 = T2; T2 = Tn
        i = i + 1
    return Tn

