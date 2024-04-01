'''
1446. Consecutive Characters
https://leetcode.com/problems/consecutive-characters/description/

The power of the string is the maximum length of a non-empty substring that contains only one unique character.
Given a string s, return the power of s.

Example 1:
Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:
Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
'''

# Runtime 23 ms Beats 59.26% of users with Python
# Memory 11.74 MB Beats 28.40% of users with Python

def maxPower(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) == 2 and s[0] == s[1]: return 2
    s1=s[0]
    n=1; mmax=1
    for i in range(1,len(s)):
        if s[i]==s1:
            n=n+1
        else:
            if n>mmax: mmax=n
            s1 = s[i]
            n = 1
    if n > mmax: mmax=n
    return mmax

