"""
Done 16.02.2025
3456. Find Special Substring of Length K
https://leetcode.com/problems/find-special-substring-of-length-k

You are given a string s and an integer k.
Determine if there exists a substring of length exactly k in s that satisfies the following conditions:
- The substring consists of only one distinct character (e.g., "aaa" or "bbb").
- If there is a character immediately before the substring, it must be different from the character in the substring.
- If there is a character immediately after the substring, it must also be different from the character in the substring.
Return true if such a substring exists. Otherwise, return false.

Example 1:
Input: s = "aaabaaa", k = 3
Output: true
Explanation:
The substring s[4..6] == "aaa" satisfies the conditions.
It has a length of 3.
All characters are the same.
The character before "aaa" is 'b', which is different from 'a'.
There is no character after "aaa".

Example 2:
Input: s = "abc", k = 2
Output: false
Explanation:
There is no substring of length 2 that consists of one distinct character and satisfies the conditions.

Constraints:
1 <= k <= s.length <= 100
s consists of lowercase English letters only.

Hint 1
Return true if there is a sequence of consecutive characters of length k

My solutuion
Easy Python solution for Problem 3456
https://leetcode.com/problems/find-special-substring-of-length-k/solutions/6429649/easy-python-solution-for-problem-3456-by-1wja/

Intuition
To do according to the task description
"""

# Runtime 32 ms Beats 100.00%
# Memory 12.42 MB Beats 100.00%
# Time Complexity O(N)
# Space Complexity O(1)

from collections import Counter
def hasSpecialSubstring(s, k):
    """
    :type s: str
    :type k: int
    :rtype: bool
    """
    mc=Counter(s); lmc=len(mc)
    ll=len(s)
    if lmc==1:
        if k==ll: return True
        else: return False
    for i in range(ll-k+1):
        s1=s[i:i+k]
        if len(Counter(s1))==1:
            if i==0:
                if ll==k: return True
                elif s[i+k]!=s1[0]: return True
            elif i==ll-k:
                if s[i-1]!=s1[0]: return True
            else:
                if s[i-1]!=s1[0] and s[i+k]!=s1[0]: return True
    return False

# print(hasSpecialSubstring(s = "aaabaaa", k = 3))
# print(hasSpecialSubstring(s = "abc", k = 2))
# print(hasSpecialSubstring(s = "ccc", k = 2))
# print(hasSpecialSubstring(s = "bfggb", k = 2))
print(hasSpecialSubstring(s = "fi", k = 1))

