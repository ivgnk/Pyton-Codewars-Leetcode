"""
Done 12.09.2024. Topics: String
1957. Delete Characters to Make Fancy String
https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/

A fancy string is a string where no three consecutive characters are equal.
Given a string s, delete the minimum possible number of characters from s to make it fancy.
Return the final string after the deletion. It can be shown that the answer will always be unique.

Example 1:
Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".

Example 2:
Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".

Example 3:
Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".

Constraints:
1 <= s.length <= 105
s consists only of lowercase English letters.

Hint 1
What's the optimal way to delete characters if three or more consecutive characters are equal?
Hint 2
If three or more consecutive characters are equal, keep two of them and delete the rest.

Solution
✏️ Easy Python solution

# Intuition
Convert to list for speed

# Approach
Iterating through the characters from the end
"""

# Runtime 4108 ms Beats 41.18%
# Memory 14.54 MB Beats 70.59%

def makeFancyString2(s):
    """
    :type s: str
    :rtype: str
    """
    lst=list(s)
    i=len(lst)-1
    while i>=2:
        if lst[i]==lst[i-1]==lst[i-2]:
            del lst[i]
        i-=1
    return ''.join(lst)

# https://leetcode.com/problems/delete-characters-to-make-fancy-string/submissions/1387780964/
# Runtime 531 ms Beats 75.00%
# Memory 17.14 MB Beats 41.18%
def makeFancyString(s):
    """
    :type s: str
    :rtype: str
    """
    l = [s[:2]]
    for i in range(2, len(s)):
        if not (s[i] == s[i - 1] == s[i - 2]):
            l.append(s[i])
    return "".join(l)


print(makeFancyString("leeetcode"))
print(makeFancyString("aaabaaaa"))
print(makeFancyString("aab"))
