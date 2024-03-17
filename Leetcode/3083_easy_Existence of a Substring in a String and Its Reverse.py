'''
3083. Existence of a Substring in a String and Its Reverse
https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/description/

Given a string s, find any substring of length 2 which is also present in the reverse of s.
Return true if such a substring exists, and false otherwise.

Example 1:
Input: s = "leetcode"
Output: true
Explanation: Substring "ee" is of length 2 which is also present in reverse(s) == "edocteel".

Example 2:
Input: s = "abcba"
Output: true
Explanation: All of the substrings of length 2 "ab", "bc", "cb", "ba" are also present in reverse(s) == "abcba".

Example 3:
Input: s = "abcd"
Output: false
Explanation: There is no substring of length 2 in s, which is also present in the reverse of s.
'''


def isSubstringPresent(s):
    """
    :type s: str
    :rtype: bool
    """
    llen = len(s)
    revs = s[::-1]
    exist_ = False
    for i in range(0, llen - 1):
        sss = s[i] + s[i + 1]
        if sss in revs: exist_ = True; break
    return exist_

print(isSubstringPresent("leetcode")) # True
print(isSubstringPresent("abcba")) # True
print(isSubstringPresent("abcd")) # False