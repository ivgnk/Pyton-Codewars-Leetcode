'''
2255. Count Prefixes of a Given String
https://leetcode.com/problems/count-prefixes-of-a-given-string/description/

You are given a string array words and a string s,
where words[i] and s comprise only of lowercase English letters.
Return the number of strings in words that are a prefix of s.
A prefix of a string is a substring that occurs at the beginning of the string.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: words = ["a","b","c","ab","bc","abc"], s = "abc"
Output: 3
Explanation:
The strings in words which are a prefix of s = "abc" are:
"a", "ab", and "abc".
Thus the number of strings in words which are a prefix of s is 3.

Example 2:
Input: words = ["a","a"], s = "aa"
Output: 2
Explanation:
Both of the strings are a prefix of s.
Note that the same string can occur multiple times in words, and it should be counted each time.
'''

# Runtime 25 ms Beats 95.54% of users with Python
# Memory 11.80 MB Beats 98.73% of users with Python

def countPrefixes(words, s):
    """
    :type words: List[str]
    :type s: str
    :rtype: int
    """
    n = 0
    for s1 in words:
        if s.startswith(s1): n = n + 1
    return n



# Runtime 32 ms Beats 62.42% of users with Python
# Memory 11.94 MB Beats 63.06%# of users with Python
def countPrefixes2(words, s):
    n=[1 for s1 in words if s.startswith(s1)]
    return len(n)