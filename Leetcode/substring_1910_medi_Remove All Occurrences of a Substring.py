"""
Done 11.08.2024. Topics: String
1910. Remove All Occurrences of a Substring
https://leetcode.com/problems/remove-all-occurrences-of-a-substring/description/

Given two strings s and part, perform the following operation on s until all occurrences
of the substring part are removed:
Find the leftmost occurrence of the substring part and remove it from s.
Return s after removing all occurrences of part.
A substring is a contiguous sequence of characters in a string.

Example 1:
Input: s = "daabcbaabcbc", part = "abc"
Output: "dab"
Explanation: The following operations are done:
- s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
- s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
- s = "dababc", remove "abc" starting at index 3, so s = "dab".
Now s has no occurrences of "abc".

Example 2:
Input: s = "axxxxyyyyb", part = "xy"
Output: "ab"
Explanation: The following operations are done:
- s = "axxxxyyyyb", remove "xy" starting at index 4 so s = "axxxyyyb".
- s = "axxxyyyb", remove "xy" starting at index 3 so s = "axxyyb".
- s = "axxyyb", remove "xy" starting at index 2 so s = "axyb".
- s = "axyb", remove "xy" starting at index 1 so s = "ab".
Now s has no occurrences of "xy".

Constraints:
1 <= s.length <= 1000
1 <= part.length <= 1000
s and part consists of lowercase English letters.

Hint 1
Note that a new occurrence of pattern can appear if you remove an old one,
For example, s = "ababcc" and pattern = "abc".
Hint 2
You can maintain a stack of characters and if the last character of the pattern size
in the stack match the pattern remove them

Solution
✏️ Easy Python solution
Intuition
Almost everything you need is in the description, examples, and tips.

Approach
But there is a nuance: you can not follow the hint (and use the stack),
but try the usual Python function for replacing in the string.
Another nuance: you need to do one replacement in one pass,
otherwise there will be an error on one of the last tests.
in 11.08.2024 this solution:
Runtime 14 ms Beats 68.61%
Memory 11.85 MB Beats 16.79%
"""


def removeOccurrences(s, part):
    """
    :type s: str
    :type part: str
    :rtype: str
    """
    while part in s:
        s=s.replace(part,'',1)
    return s

# print(removeOccurrences(s = "daabcbaabcbc", part = "abc")) # "dab"
print(removeOccurrences(s ="aabababa", part = "aba"))
