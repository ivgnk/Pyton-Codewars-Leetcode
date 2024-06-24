"""
Done 24.06.2024. Topics: Hash Table, String, Sliding Window
3090. Maximum Length Substring With Two Occurrences
https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/description/

Given a string s, return the maximum length of a substring
such that it contains at most two occurrences of each character.

Example 1:
Input: s = "bcbbbcba"
Output: 4
Explanation:
The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".

Example 2:
Input: s = "aaaa"
Output: 2
Explanation:
The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".

Constraints:
2 <= s.length <= 100
s consists only of lowercase English letters.

Hint 1
We can try all substrings by brute-force since the constraints are very small
"""

# Runtime 2869 ms Beats 5.10%
# Memory 11.53 MB Beats 84.71
from collections import Counter
def maximumLengthSubstring2(s):
    """
    :type s: str
    :rtype: int
    """
    dd=dict()
    for s1 in s:
        if s1 in dd:
            dd[s1]=dd[s1]+1
        else:
            dd[s1] = 1
    ll=len(s)
    if all([v==2 for k,v in dd.items()]): return ll

    mmax=0
    for i in range(ll):
        for j in range(i+1,ll):
            s1=s[i:j+1]
            dd1=Counter(s1)
            if all([v <= 2 for k, v in dd1.items()]):
                mmax=max(mmax,len(s1))
    return mmax

# Runtime 2860 ms Beats 5.10%
# Memory 11.58 MB Beats 84.71%
def maximumLengthSubstring3(s):
    """
    :type s: str
    :rtype: int
    """
    dd=dict()
    for s1 in s:
        if s1 in dd:
            dd[s1]=dd[s1]+1
        else:
            dd[s1] = 1
    ll=len(s)
    if all([v==2 for k,v in dd.items()]): return ll

    mmax=0
    for i in range(ll):
        s1 = s[i]; ll1=1
        for j in range(i+1,ll):
            s1=s1+s[j]; ll1=ll1+1
            dd1=Counter(s1)
            if all([v <= 2 for k, v in dd1.items()]):
                mmax=max(mmax,ll1)
    return mmax

# Runtime 458 ms Beats 5.73%
# Memory 11.82 MB Beats 19.75%
def maximumLengthSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    dd=dict()
    for s1 in s:
        if s1 in dd:
            dd[s1]=dd[s1]+1
        else:
            dd[s1] = 1
    ll=len(s)
    if all([v==2 for k,v in dd.items()]): return ll

    mmax=0;
    for i in range(ll):
        dd2=dict()
        s1 = s[i]; ll1=1
        dd2[s1]=1
        for j in range(i+1,ll):
            s1=s1+s[j]; ll1=ll1+1
            if s[j] in dd2:
                dd2[s[j]] = dd2[s[j]]+1
            else:
                dd2[s[j]] = 1
            if all([v <= 2 for k, v in dd2.items()]):
                mmax=max(mmax,ll1)
    return mmax

print(maximumLengthSubstring("bcbbbcba"))
print(maximumLengthSubstring("aaaa"))