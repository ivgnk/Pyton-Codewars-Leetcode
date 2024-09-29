"""
Done 29.09.2024. Topics: String
917. Reverse Only Letters
Given a string s, reverse the string according to the following rules:
All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

Example 1:
Input: s = "ab-cd"
Output: "dc-ba"

Example 2:
Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:
Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Constraints:
1 <= s.length <= 100
s consists of characters with ASCII values in the range [33, 122].
s does not contain '\"' or '\\'.

Solution
✏️ Easy Python solution with some preparing
Intuition
Prepare
1) string with all english letters
2) reversed string with all english letters in the string
"""
# Runtime 9 ms Beats 86.37%
# Memory 11.74 MB Beats 22.04%

engl='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
import string
def reverseOnlyLetters(s):
    """
    :type s: str
    :rtype: str
    """
    lst=[s1 for s1 in s if s1 in engl]
    lst=list(reversed(lst))
    res=[]; n=0
    for s1 in s:
        if s1 in engl:
            res.append(lst[n])
            n+=1
        else:
            res.append(s1)
    return ''.join(res)

print(reverseOnlyLetters("a-bC-dEf-ghIj"))