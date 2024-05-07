"""
Done 08.05.2024. Topics: Hash Table, String, Counting
1941. Check if All Characters Have Equal Number of Occurrences
https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

Given a string s, return true if s is a good string, or false otherwise.
A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

Example 1:
Input: s = "abacbc"
Output: true
Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

Example 2:
Input: s = "aaabb"
Output: false
Explanation: The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.
"""

# Runtime 14 ms Beats 80.00% of users with Python
# Memory 11.67 MB Beats 78.08% of users with Python

from collections import Counter
def areOccurrencesEqual(s):
    """
    :type s: str
    :rtype: bool
    """
    dd=dict(Counter(s))
    return all([dd[s[0]]==v for k,v in dd.items()])

print(areOccurrencesEqual("abacbc"))
print(areOccurrencesEqual("aaabb"))