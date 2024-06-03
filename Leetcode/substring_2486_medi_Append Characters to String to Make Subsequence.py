"""
Done 03.06.2024. Topics: Two Pointers, String, Greedy
2486. Append Characters to String to Make Subsequence
https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description

You are given two strings s and t consisting of only lowercase English letters.
Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.
A subsequence is a string that can be derived from another string by deleting some or
no characters without changing the order of the remaining characters.

Example 1:
Input: s = "coaching", t = "coding"
Output: 4
Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
Now, t is a subsequence of s ("coachingding").
It can be shown that appending any 3 characters to the end of s will never make t a subsequence.

Example 2:
Input: s = "abcde", t = "a"
Output: 0
Explanation: t is already a subsequence of s ("abcde").

Example 3:
Input: s = "z", t = "abcde"
Output: 5
Explanation: Append the characters "abcde" to the end of s so that s = "zabcde".
Now, t is a subsequence of s ("zabcde").
It can be shown that appending any 4 characters to the end of s will never make t a subsequence.

Hint 1
Find the longest prefix of t that is a subsequence of s.
Hint 2
Use two variables to keep track of your location in s and t.
If the characters match, increment both variables.
Otherwise, only increment the variable for s.
Hint 3
The remaining characters in t must be appended to the end of s.
"""

# Runtime 36 ms Beats 95.92% of users with Python
# Memory 13.60 MB Beats 55.10% of users with Python

def appendCharacters(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    if s.find(t)>-1: return 0
    ls=len(s); lt=len(t)
    i, j=0, 0
    while i<ls and j<lt:
        if s[i]==t[j]:
            i=i+1; j=j+1
        else:
            i = i + 1
    if i !=j:
        return lt-j
    else:
        return 0
