"""
05.01.2025
3407. Substring Matching Pattern
https://leetcode.com/problems/substring-matching-pattern/description/

You are given a string s and a pattern string p, where p contains exactly one '*' character.
The '*' in p can be replaced with any sequence of zero or more characters.
Return true if p can be made a substring of s, and false otherwise.
A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
Input: s = "leetcode", p = "ee*e"
Output: true
Explanation:
By replacing the '*' with "tcod", the substring "eetcode" matches the pattern.

Example 2:
Input: s = "car", p = "c*v"
Output: false
Explanation:
There is no substring matching the pattern.

Example 3:
Input: s = "luck", p = "u*"
Output: true
Explanation:
The substrings "u", "uc", and "uck" match the pattern.

Constraints:
1 <= s.length <= 50
1 <= p.length <= 50
s contains only lowercase English letters.
p contains only lowercase English letters and exactly one '*'

Hint 1
Divide the pattern in two strings and search in the string.
"""
# Runtime 3 ms Beats 100.00%
# Memory 12.58 MB Beats 100.00%
# https://leetcode.com/problems/substring-matching-pattern/solutions/6230099/python-solution-by-lavabottada-sw9w/
def hasMatch(s: str, p: str) -> bool:
    parts = p.split('*')
    pref = parts[0]
    suff = parts[1]
    plen = len(pref)
    slen = len(suff)
    if not pref and not suff:
        return True

    if not pref:
        return suff in s

    if not suff:
        return pref in s
    for i in range(len(s) - plen - slen + 1):
        if s[i:i + plen] == pref:
            if suff in s[i + plen:]:
                return True
    return False
print(hasMatch(s="leetcode", p = "ee*e"))
print(hasMatch(s = "car", p = "c*v"))
