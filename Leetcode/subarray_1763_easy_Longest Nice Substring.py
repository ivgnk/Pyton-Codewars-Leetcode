"""
Done 03.07.2024. Topics: Hash Table, String, Divide and Conquer, Bit Manipulation, Sliding Window

1763. Longest Nice Substring
https://leetcode.com/problems/longest-nice-substring/description/

A string s is nice if, for every letter of the alphabet that s contains,
it appears both in uppercase and lowercase.
For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear.
However, "abA" is not because 'b' appears, but 'B' does not.
Given a string s, return the longest substring of s that is nice.
If there are multiple, return the substring of the earliest occurrence.
If there are none, return an empty string.

Example 1:
Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.

Example 2:
Input: s = "Bb"
Output: "Bb"
Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.

Example 3:
Input: s = "c"
Output: ""
Explanation: There are no nice substrings.

Hint 1
Brute force and check each substring to see if it is nice.
"""

# Runtime 305 ms Beats 5.13%
# Memory 11.58 MB Beats 85.47%
from icecream import ic
def longestNiceSubstring3(s):
    """
    :type s: str
    :rtype: str
    """
    ll=len(s); res=''; ml=0
    if ll==1: return res
    for i in range(ll):
        # ic(i,'----')
        for j in range(i+1,ll):
            s1=s[i:j+1]
            # ic(i,j,s1)
            dd=dict()
            for s2 in s1:
                if s2 in dd:
                    dd[s2]=dd[s2]+1
                else:
                    dd[s2]=1
            nk=len(dd)
            if nk%2==0:
                ks=sorted([k for k in dd.keys()])
                tr=True; nk2=nk//2
                for ii in range(nk//2):
                    tr = tr and abs(ord(ks[ii])-ord(ks[ii+nk2]))==32
                ll4=len(s1)
                if tr and ll4>ml:
                    ml=ll4
                    res=s1
    return res

# Runtime 246 ms Beats 7.69%
# Memory 11.51 MB Beats 85.47%
def longestNiceSubstring2(s):
    """
    :type s: str
    :rtype: str
    """
    ll=len(s); res=''; ml=0
    if ll==1: return res
    for i in range(ll):
        # ic(i,'----')
        for j in range(i+1,ll):
            s1=s[i:j+1]
            # ic(i,j,s1)
            dd=dict()
            for s2 in s1:
                if s2 in dd:
                    dd[s2]=dd[s2]+1
                else:
                    dd[s2]=1
            nk=len(dd)
            if nk%2==0:
                ks=sorted([k for k in dd.keys()])
                tr=True; nk2=nk//2
                for ii in range(nk//2):
                    tr = tr and abs(ord(ks[ii])-ord(ks[ii+nk2]))==32
                ll4=len(s1)
                if tr and ll4>ml:
                    ml=ll4
                    res=s1
    return res

# Runtime 150 ms Beats 19.66%
# Memory 11.56 MB Beats 85.47%
# Runtime 143 ms Beats 19.66%
# Memory 11.65 MB Beats 62.39%
# Runtime 142 ms Beats 19.66%
# Memory 11.69 MB Beats 62.39%
# Runtime 141 ms Beats 20.51%
# Memory 11.77 MB Beats 34.19%
def longestNiceSubstring(self, s):
    """
    :type s: str
    :rtype: str
    """
    ll=len(s); res=''; ml=0
    if ll==1: return res
    for i in range(ll):
        # ic(i,'----')
        for j in range(i+1,ll):
            s1=s[i:j+1]
            # ic(i,j,s1)
            dd=set(s1)
            nk=len(dd)
            if nk%2==0:
                ks=sorted(dd)
                tr=True; nk2=nk//2
                for ii in range(nk//2):
                    tr = tr and abs(ord(ks[ii])-ord(ks[ii+nk2]))==32
                ll4=len(s1)
                if tr and ll4>ml:
                    ml=ll4
                    res=s1
    return res

ic(longestNiceSubstring("YazaAay"))
ic(longestNiceSubstring("Bb"))
ic(longestNiceSubstring("c"))

# print(ord("a")-ord("A"))



