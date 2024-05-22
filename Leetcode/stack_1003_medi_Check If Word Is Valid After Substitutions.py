"""
Done 22.05.2024. Topics: String, Stack
1003. Check If Word Is Valid After Substitutions
https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/description/

Given a string s, determine if it is valid.

A string s is valid if, starting with an empty string t = "",
you can transform t into s after performing the following operation any number of times:

Insert string "abc" into any position in t. More formally,
t becomes tleft + "abc" + tright, where t == tleft + tright.
Note that tleft and tright may be empty.
Return true if s is a valid string, otherwise, return false.

Example 1:
Input: s = "aabcbc"
Output: true
Explanation:
"" -> "abc" -> "aabcbc"
Thus, "aabcbc" is valid.

Example 2:
Input: s = "abcabcababcc"
Output: true
Explanation:
"" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
Thus, "abcabcababcc" is valid.

Example 3:
Input: s = "abccba"
Output: false
Explanation: It is impossible to get "abccba" using the operation.
"""

# Runtime 148 ms Beats 5.95% of users with Python3
# Memory 16.83 MB Beats 30.84% of users with Python3

def isValid2(s: str) -> bool:
    ll = len(s)
    if ll%3 !=0: return False
    for i in range(ll//3):
        if s.find('abc')>-1:
            s=s.replace('abc', '', 1)
        else: return False
    return s==''


# https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/solutions/3221953/simple-3-liner-solution-in-python/
# Runtime 42 ms Beats 77.53% of users with Python3
# Memory 16.81 MB Beats 30.84% of users with Python3
def isValid(self, s: str) -> bool:
        while len(s) > 3 and 'abc' in s:
            s = ''.join(s.split('abc'))
        return s == '' or s == 'abc'

print(isValid("aabcbc"))
