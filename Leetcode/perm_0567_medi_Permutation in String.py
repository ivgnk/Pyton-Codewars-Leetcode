"""
05.09.2024. Topics: Hash Table, Two Pointers, String, Sliding Window
567. Permutation in String
https://leetcode.com/problems/permutation-in-string/description

Given two strings s1 and s2, return true if s2 contains a
permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.

Hint 1
Obviously, brute force will result in TLE. Think of something else.
Hint 2
How will you check whether one string is a permutation of another string?
Hint 3
One way is to sort the string and then compare. But, Is there a better way?
Hint 4
If one string is a permutation of another string then they must have one common metric. What is that?
Hint 5
Both strings must have same character frequencies, if one is permutation of another. Which data structure should be used to store frequencies?
Hint 6
What about hash table? An array of size 26?

tips
https://leetcode.com/problems/permutation-in-string/description/comments/1811445
https://leetcode.com/problems/permutation-in-string/description/comments/1868390
"""

# Not pass test 2
# s1 = "ab", s2 ="eidboaoo"
def checkInclusion2(s1: str, s2: str) -> bool:
    if len(s1) > len(s2): return False

    dd1=dict(); dd2=dict()
    for s in s1:
        if s in dd1:
            dd1[s]+=1
        else:
            dd1[s]=1

    for s in s2:
        if s in dd2:
            dd2[s]+=1
        else:
            dd2[s]=1

    return all([(k in dd2) and (dd2[k]==v) for k,v in dd1.items()])

# https://leetcode.com/problems/permutation-in-string/description/comments/1989060
# Runtime 1140 ms Beats 18.47%
# Memory 16.64 MB Beats 62.60%
# Runtime 1130 ms Beats 18.73%
# Memory 16.74 MB Beats 22.10
# Runtime 1120 ms Beats 19.04%
# Memory 16.87 MB Beats 22.10%
# Runtime 1041 ms Beats 20.98%
# Memory 16.87 MB Beats 22.10%
# My # https://leetcode.com/problems/permutation-in-string/submissions/1412725369/
from collections import Counter
def checkInclusion3(s1: str, s2: str) -> bool:
    if (ls1:=len(s1)) >(ls2:=len(s2)): return False
    dd1=Counter(s1)
    l=0; r=l+ls1
    while r<ls2+1:
        s=s2[l:r]
        if Counter(s)==dd1: return True
        l+=1
        r+=1
    return False

# Runtime 50 ms Beats 87.68%
# Memory 16.60 MB Beats 88.94%
lc='abcdefghijklmnopqrstuvwxyz'
def checkInclusion(s1: str, s2: str) -> bool:
    d1 = {s:0 for s in lc}
    d2 = d1.copy()

    if (ls1:=len(s1)) >(ls2:=len(s2)): return False
    for i,s in enumerate(s1):
        d1[s]+=1
        d2[s2[i]] += 1

    if d1==d2: return True
    for i in range(ls1,ls2):
        d2[s2[i]] += 1
        d2[s2[i - ls1]] -= 1
        if d1 == d2: return True
    return False


# print(checkInclusion(s1 = "ab", s2 = "eidbaooo"))
# print(checkInclusion(s1 = "ab", s2 = "eidbaooo"))
# print(checkInclusion(s1 = "adc", s2 = "dcda"))
# from string import ascii_lowercase
# print(ascii_lowercase)
# print({s:0 for s in ascii_lowercase})