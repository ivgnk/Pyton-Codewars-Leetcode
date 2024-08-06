"""
Done 06.08.2024. Topics: Array, String
2414. Length of the Longest Alphabetical Continuous Substring
https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/description/

An alphabetical continuous string is a string consisting of consecutive letters in the alphabet.
In other words, it is any substring of the string "abcdefghijklmnopqrstuvwxyz".

For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not.
Given a string s consisting of lowercase letters only, return the length of the longest
alphabetical continuous substring.

Example 1:
Input: s = "abacaba"
Output: 2
Explanation: There are 4 distinct continuous substrings: "a", "b", "c" and "ab".
"ab" is the longest continuous substring.

Example 2:
Input: s = "abcde"
Output: 5
Explanation: "abcde" is the longest continuous substring.

Constraints:
1 <= s.length <= 10**5
s consists of only English lowercase letters.

Hint 1
What is the longest possible continuous substring?
Hint 2
The size of the longest possible continuous substring is at most 26, so we can just brute force the answer.

Main hint
To check the longest possible continuous substring, we can check if difference between two adjacent character
is 1 or not. If it is 1 then increment the counter variable and update the answer.
If it is not continuous then reset it to 1.
https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/description/comments/1845924
"""
# Python
# Runtime 247 ms Beats 46.15%
# Memory 16.56 MB Beats 20.51%
# Python 3
# Runtime 245 ms Beats 60.04%
# Memory 18.80 MB Beats 6.09%

def longestContinuousSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    nn = 1;    mmax = 0;   ll = len(s)
    ords = map(ord, s)
    for i in range(0, ll - 1):
        if ords[i + 1] - ords[i] == 1:
            nn += 1
        else:
            mmax = max(mmax, nn)
            nn = 1
    mmax = max(mmax, nn)
    return mmax


# Runtime 261 ms Beats 46.15%
# Memory 16.26 MB Beats 41.03%
def longestContinuousSubstring2(s):
    """
    :type s: str
    :rtype: int
    """
    nn=1; mmax=0
    for i in range(0,len(s)-1):
        if ord(s[i+1])-ord(s[i])==1:
            nn+=1
        else:
            mmax=max(mmax,nn)
            nn=1
    mmax = max(mmax, nn)
    return mmax

# Runtime 290 ms Beats 35.90%
# Memory 16.80 MBBeats 20.51%
def longestContinuousSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    nn=1; mmax=0; ll=len(s)
    ords=[ord(s[i]) for i in range(ll)]
    for i in range(0,ll-1):
        if ords[i+1]-ords[i]==1:
            nn+=1
        else:
            mmax=max(mmax,nn)
            nn=1
    mmax = max(mmax, nn)
    return mmax


print(longestContinuousSubstring("abacaba"))
print(longestContinuousSubstring("abcde"))


