"""
Done 03.11.2024. Hash Table, String, Sliding Window
76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/description/

Given two strings s and t of lengths m and n respectively, return the minimum window
substring of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
m == s.length
n == t.length
1 <= m, n <= 10**5
s and t consist of uppercase and lowercase English letters.

Hint 1
Use two pointers to create a window of letters in s, which would have all the characters from t.
Hint 2
Expand the right pointer until all the characters of t are covered.
Hint 3
Once all the characters are covered, move the left pointer and ensure that all the characters are still covered to minimize the subarray size.
Hint 4
Continue expanding the right and left pointers until you reach the end of s.
"""
# Time Limit Exceeded - 265 / 268 testcases passed
import string
from string import *

def minWindow2(s: str, t: str) -> str:
    ll = len(s);    lt = len(t)
    if ll < lt: return "";
    res = []
    ddt = dict(Counter(t));  minl = 1000000
    s = list(s)
    i = 0; j = i + lt
    while i < j and i < ll and j <= ll:
        s1 = s[i:j]
        # print(i,j,s1)
        s1dd = dict(Counter(s1))
        # ---- Control
        bad = True
        for k, v in ddt.items():
            if k in s1dd:
                if s1dd[k] < ddt[k]: break
            else:
                break
        else:
            bad = False
        if bad:
            j = j + 1
        else:
            if (r := len(s1)) < minl:
                minl = r
                res = s1
            i += 1
    return ''.join(res)

# Time Limit Exceeded - 265 / 268 testcases passed
from collections import Counter, defaultdict
def minWindow3(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    ll = len(s); lt=len(t)
    if ll<lt: return "";
    if s.find(t)>-1: return t
    res=[]
    ddt=dict(Counter(t)); minl=1000000
    print(ddt)
    s=list(s)
    i=0; j=i+lt; s1=s[i:j]; j=j-1
    while i<j and i<ll and j<=ll:
        print(i,j,s1)
        s1dd=dict(Counter(s1))
        # ---- Control
        bad=True
        for k, v in ddt.items():
            if k in s1dd:
                if s1dd[k]<v: break
            else:
                break
        else: bad=False
        if bad:
            j=j+1;
            if j<=ll-1: s1=s1+[s[j]]
            print('1 = ',j,s1)
        else:
            if (r:=len(s1))<minl:
                minl=r
                res=s1.copy()
            i+=1; s1.pop(0)
        print(bad,res)
    return ''.join(res)

# Runtime 4278 ms Beats 5.05%
# Memory 18.60 MB Beats
# 5.22%
def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    ll = len(s); lt=len(t)
    if ll<lt: return "";
    if s.find(t)>-1: return t
    res=[]
    ddt=dict(Counter(t)); minl=1000000
    s=list(s)
    i=0; j=i+lt; s1=s[i:j]; j=j-1; s1dd=dict(Counter(s1))
    while i<j and i<ll and j<=ll:
        # ---- Control
        bad=True
        for k, v in ddt.items():
            if k in s1dd:
                if s1dd[k]<v: break
            else:
                break
        else: bad=False
        if bad:
            j=j+1;
            if j<=ll-1:
                s1=s1+[s[j]];
                if s[j] in s1dd: s1dd[s[j]]+=1
                else: s1dd[s[j]]=1
        else:
            if (r:=len(s1))<minl:
                minl=r
                res=s1.copy()
            i+=1
            s1dd[s1.pop(0)]-=1
    return ''.join(res)


# print(minWindow(s = "ADOBECODEBANC", t = "ABC"))
# print(minWindow(s = "abc", t = "ac"))
# print(minWindow(s = "a", t = "a"))
# print(minWindow(s = "a", t = "aa"))
# print(minWindow(s = "a", t = "b"))
# print({s:0 for s in string.ascii_letters})
window_counts = defaultdict(int)
window_counts['s'] += 1
window_counts['B'] += 1
print(window_counts)