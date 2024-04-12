"""
3042. Count Prefix and Suffix Pairs I
https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description/

Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:
isPrefixAndSuffix(str1, str2) returns true
if str1 is both a prefix and a suffix of str2, and false otherwise.
For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix,
but isPrefixAndSuffix("abc", "abcd") is false.
Return an integer denoting the number of index pairs (i, j) such that i < j,
and isPrefixAndSuffix(words[i], words[j]) is true.
"""
# Runtime 39 ms Beats 61.67% of users with Python
# Memory 11.91 MB Beats 7.35% of users with Python

def countPrefixSuffixPairs(words):
    ll = len(words)
    if ll == 2 and words[0] == words[1]: return 1
    lli = [len(w1) for w1 in words]
    n = 0
    for i in range(ll):
        for j in range(i + 1, ll):
            if lli[i] <= lli[j]:
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    n = n + 1
    return n

