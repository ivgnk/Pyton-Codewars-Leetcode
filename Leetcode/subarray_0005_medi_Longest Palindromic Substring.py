"""
Done 05.06.2024. Topics: Two Pointers, String, Dynamic Programming
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/description/

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Hint 1
How can we reuse a previously computed palindrome to compute a larger palindrome?
Hint 2
If “aba” is a palindrome, is “xabax” a palindrome? Similarly is “xabay” a palindrome?
Hint 3
Complexity based hint:
If we use brute-force and check whether for every start and end position a substring is
a palindrome we have O(n^2) start - end pairs and O(n) palindromic checks.
Can we reduce the time for palindromic checks to O(1) by reusing some previous computation.
"""

# Time Limit Exceeded -- 134 / 142 testcases passed
def longestPalindrome5(s):
    """
    :type s: str
    :rtype: str
    """
    # if s==s[::-1]: return s
    ll=len(s)
    ss = s[0]
    le=1
    for i in range(ll):
        palin=s[i]
        for j in range(i+1,ll):
            palin=palin + s[j]
            if palin==palin[::-1] and le<len(palin):
                ss=palin
                le=len(palin)
    return ss

# Runtime 6594 ms Beats 5.00% of users with Python
# Memory 11.92 MB Beats 27.92% of users with Python
def longestPalindrome2(s):
    """
    :type s: str
    :rtype: str
    """
    if s==s[::-1]: return s
    ll=len(s); le=0; ss=''
    for i in range(ll):
        for j in range(ll,-1,-1):
            t=s[i:j]
            if t==t[::-1]:
                if len(t)>le:
                    le=len(t)
                    ss=t
    return ss

# Runtime 2059 ms Beats 38.21% of users with Python
# Memory 11.78 MB Beats 70.41% of users with Python
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if s==s[::-1]: return s
    ll = len(s)
    le=0; ss=''
    for i in range(ll):
        for j in range(ll-1,-1,-1):
            if s[i]==s[j]:
                t=s[i:j+1]
                if t==t[::-1]:
                    if len(t)>le:
                        le=len(t)
                        ss=t
    return ss

print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))


# Wrong Answer -- 135 / 142 testcases passed
def longestPalindrome0(s):
    """
    :type s: str
    :rtype: str
    """

    if s==s[::-1]: return s
    ll = len(s)
    i=0; j=ll-1

    while s[i] !=s[j]:
        if s[i+1] != s[j] and s[i] != s[j-1]:
            i=i+1
            j=j-1
        elif s[i]==s[j-1]:
                j=j-1
        elif s[i+1]==s[j]:
                i=i+1
    s=s[i:j+1]
    ll = len(s)
    le=0; ss=''
    for i in range(ll):
        for j in range(ll-1,-1,-1):
            if s[i]==s[j]:
                t=s[i:j+1]
                if t==t[::-1]:
                    if len(t)>le:
                        le=len(t)
                        ss=t
    return ss


