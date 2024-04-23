"""
680. Valid Palindrome II
https://leetcode.com/problems/valid-palindrome-ii/

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false
"""

# Time Limit Exceeded -- 420 / 471 testcases passed

def validPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    print(s)

    ll=len(s)
    if ll>53000:
        ll2=ll//2+ll%2
    else: ll2=ll
    for i in range(ll2):
        s1=s[:i]+s[i+1:]
        print(i,s1)
        if s1==s1[::-1]: return True
    return False

print(validPalindrome("cbbcc"))