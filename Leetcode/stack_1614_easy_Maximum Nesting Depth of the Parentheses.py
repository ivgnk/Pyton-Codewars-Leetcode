"""
Done 22.05.2024. Topics: String, Stack
1614. Maximum Nesting Depth of the Parentheses
https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/

Given a valid parentheses string s, return the nesting depth of s.
The nesting depth is the maximum number of nested parentheses.

Example 1:
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation:
Digit 8 is inside of 3 nested parentheses in the string.

Example 2:
Input: s = "(1)+((2))+(((3)))"
Output: 3
Explanation:
Digit 3 is inside of 3 nested parentheses in the string.

Example 3:
Input: s = "()(())((()()))"
Output: 3
"""


# Wrong Answer --  153 / 168 testcases passed
# https://evileg.com/ru/post/642/
def maxDepth2(s):
    """
    :type s: str
    :rtype: int
    """
    s1 = "".join(c for c in s if c=='(' or c==')')
    print(s1)
    for i in range(len(s1),-1,-1):
        if s1.find('('*i) !=-1 or s1.find(')'*i) !=-1: return i

# Runtime 14 ms Beats 59.03% of users with Python
# Memory 11.94 MB Beats 5.10% of users with Python
# Runtime 12 ms Beats 74.99% of users with Python
# Memory 11.51 MB Beats 86.37% of users with Python
def maxDepth(s):
    """
    :type s: str
    :rtype: int
    """
    s1 = "".join(c for c in s if c=='(' or c==')')
    print(s1); m=0; smax=0
    for i in range(len(s1)):
        if s1[i]=='(':
            m=m+1
            smax=max(smax,m)
        else:
            m=m-1
            smax=max(smax,m)
    return smax

print(maxDepth("(1+2)/(5+((4-9+8)*((1+8+(5*7)*4)/(7+9-5)))/(7/3-8-4-8))"))