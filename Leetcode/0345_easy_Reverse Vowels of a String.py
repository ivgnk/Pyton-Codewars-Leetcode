"""
Done 07.05.2024. Topics: Two Pointers, String
345. Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"
"""

# Runtime 76 ms Beats 34.55% of users with Python
# Memory 16.48 MB Beats 18.33%
# of users with Python

vowels= ['A','E','I','O','U', 'a', 'e', 'i', 'o', 'u']
def reverseVowels2(s):
    """
    :type s: str
    :rtype: str
    """
    ss = list(s)
    ll = len(s)
    ind = [i for i in range(ll) if ss[i] in vowels]
    vow = [s1 for s1 in ss if s1 in vowels]
    vow = vow[::-1]
    n = 0
    for i in ind:
        ss[i] = vow[n]
        n = n + 1
    return ''.join(ss)

# Runtime 78 ms Beats 33.66% of users with Python
# Memory 16.57 MB Beats 17.05% of users with Python

def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    ss = list(s)
    ind = [i for i in range(len(s)) if ss[i] in vowels]
    vow = [s1 for s1 in ss if s1 in vowels][::-1]

    for i in range(len(ind)):
        ss[ind[i]] = vow[i]

    return ''.join(ss)