'''
Done 27.09.2024. Topics: Hash Table, String
859. Buddy Strings
https://leetcode.com/problems/buddy-strings/description/

Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.
Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].
For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

Example 1:
Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

Example 2:
Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.

Example 3:
Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.
'''


from collections import Counter

# s = "abab" goal = "baba"
def buddyStrings2(s, t):
    """
    :type s: str
    :type goal: str
    :rtype: bool
    """
    ds = dict(Counter(s))
    dt = dict(Counter(t))
    if ds!=dt: return False
    else:
        return any([v>1 for k,v in ds.items()]) or (s[0]==t[1] and len(s)==2)

# Runtime 28 ms Beats 12.27%
# Memory 12.76 MB Beats 31.97%
# https://leetcode.com/problems/buddy-strings/description/comments/1953975
# if s[i] != goals[i] at more than 2 different places, return false.

# Solution
# ✏️ Lazy Python solution based on hint in discussion and 4 edge cases
# Intuition
# Main hint if s[i] != goals[i] at more than 2 different places, return false.
# https://leetcode.com/problems/buddy-strings/description/comments/1953975
#
# Approach
# 1 edge case - equal length of strings
# 2 edge case - for string with length==2
# 3 edge case - equal letters in strings
# 4 edge case - equal strings
# Done 27.09.2024
# Runtime 28 ms Beats 12.27%
# Memory 12.76 MB Beats 31.97%



def buddyStrings(s, t):
    lens = len(s)
    # 1 edge case
    if lens != len(t): return False
    # 2 edge case
    if lens == 2:
        return (s[0] == t[1] and s[1] == t[0]) or (s[0] == t[0] == s[1] == t[1])

    ds = dict(Counter(s))
    dt = dict(Counter(t))
    # 3 edge case
    if ds != dt: return False

    ssum = sum([s[i] != t[i] for i in range(lens)])
    if ssum == 2: return True
    # 4 edge case
    elif ssum == 0 and max([v for k, v, in ds.items()]) > 1:  return True
    else: return False

print(buddyStrings("ab", "babbb"))
