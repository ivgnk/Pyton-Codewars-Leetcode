'''
338. Counting Bits
https://leetcode.com/problems/counting-bits/description/

Given an integer n, return an array ans of length n + 1 such that
for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
'''

# Runtime ms Beats 81.85% of users with Python
# Memory 15.46 MB Beats 84.34% of users with Python

def countBits(self, n):
    """
    :type n: int
    :rtype: List[int]
    """
    return [bin(i)[2:].count('1') for i in range(n + 1)]

def countBits2(self, n):
    """
    :type n: int
    :rtype: List[int]
    """
    res=[]
    for i in range(n+1):
        s=bin(i); s= s[2:]
        l = s.count('1')
        res.append(l)
    return res