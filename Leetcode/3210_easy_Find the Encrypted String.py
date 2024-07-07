"""
Done 07.07.2024. Topics: String
3210. Find the Encrypted String
https://leetcode.com/problems/find-the-encrypted-string/description/

You are given a string s and an integer k. Encrypt the string using the following algorithm:
For each character c in s, replace c with the kth character after c in the string (in a cyclic manner).
Return the encrypted string.

Example 1:
Input: s = "dart", k = 3
Output: "tdar"
Explanation:
For i = 0, the 3rd character after 'd' is 't'.
For i = 1, the 3rd character after 'a' is 'd'.
For i = 2, the 3rd character after 'r' is 'a'.
For i = 3, the 3rd character after 't' is 'r'.

Example 2:
Input: s = "aaa", k = 1
Output: "aaa"
Explanation:
As all the characters are the same, the encrypted string will also be the same.

Constraints:
1 <= s.length <= 100
1 <= k <= 104
s consists only of lowercase English letters.

Hint 1
Make a new string such that for each character in s,
character i will correspond to (i + k) % n character in the original string.
"""


# Runtime 44 ms Beats 100.00%
# Memory 16.48 MB Beats 100.00%
def getEncryptedString(s: str, k: int) -> str:
    ll = len(s)
    ns=[s[(i + k) % ll] for i in range(ll)]
    return ''.join(ns)

print(getEncryptedString(s = "dart", k = 3))