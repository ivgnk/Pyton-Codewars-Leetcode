"""
Done 28.07.2024. Topics: String, Sliding Window
1456. Maximum Number of Vowels in a Substring of Given Length
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length

Hint 1
Keep a window of size k and maintain the number of vowels in it.
Hint 2
Keep moving the window and update the number of vowels while moving.
Answer is max number of vowels of any window.
"""
from icecream import ic

vowel=['a', 'e', 'i', 'o', 'u']
# Runtime 8269 ms Beats 5.01%
# Memory 15.56 MB Beats 51.39%
def maxVowels2(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    mmax=-1
    for i in range(len(s)-k+1):
        s1=s[i:i+k]
        n=sum([s1.count(ss)  for ss in vowel])
        print(i,s1,n)
        mmax=max(mmax,n)
    return mmax

# Time Limit Exceeded - 99 / 106 testcases passed
def maxVowels3(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    mmax=-1; ll=len(s)
    s1 = list(s[0:k]); i=k
    while i<=ll:
        n=sum([s1.count(ss)  for ss in vowel])
        mmax=max(mmax,n)
        if i==ll: break
        s1.pop(0)
        s1.append(s[i])
        i=i+1
    return mmax


# Runtime 595 ms Beats 5.33%
# Memory 13.54 MB Beats 86.47%
def maxVowels4(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    mmax=-1; ll=len(s)
    s1 = list(s[0:k]); i=k
    n = sum([s1.count(ss) for ss in vowel])
    while i<=ll:
        mmax=max(mmax,n)
        if i==ll: break
        out=s1.pop(0)
        if out in vowel: n=n-1
        s1.append(s[i])
        if s[i] in vowel: n=n+1
        i=i+1
    return mmax

# Runtime 544 ms Beats 6.35% Analyze Complexity
# Memory 15.73 MB Beats 15.52%
def maxVowels(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    mmax=-1; ll=len(s)
    nn=[1 if ss in vowel else 0 for ss in s]
    s1 = list(nn[0:k]); i=k
    n = sum(s1)
    while i<=ll:
        mmax=max(mmax,n)
        if i==ll: break
        out=s1.pop(0)
        n=n-out
        s1.append(nn[i])
        n=n+nn[i]
        i=i+1
    return mmax


ic(maxVowels(s = "abciiidef", k = 3)) # 3
ic(maxVowels(s = "aeiou", k = 2)) # 2
ic(maxVowels(s = "leetcode", k = 3)) # 2
ic(maxVowels(s = "weallloveyou", k = 7)) # 4

