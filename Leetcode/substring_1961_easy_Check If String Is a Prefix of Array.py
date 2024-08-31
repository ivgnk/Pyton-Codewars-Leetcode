"""
Done 31.08.2024. Topics: Two Pointers, String
1961. Check If String Is a Prefix of Array
https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/description/

Given a string s and an array of strings words, determine whether s is a prefix string of words.

A string s is a prefix string of words if s can be made by concatenating
the first k strings in words for some positive k no larger than words.length.

Return true if s is a prefix string of words, or false otherwise.

Example 1:
Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
Output: true
Explanation:
s can be made by concatenating "i", "love", and "leetcode" together.

Example 2:
Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
Output: false
Explanation:
It is impossible to make s using a prefix of arr.

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 20
1 <= s.length <= 1000
words[i] and s consist of only lowercase English letters.

Hint 1
There are only words.length prefix strings.
Hint 2
Create all of them and see if s is one of them.

Solution
✏️ Easy Python solution with length control

# Intuition
Gradual increase in the length of the string.

# Approach
To get the fastest solution, it is necessary to control the length of the string in the build-up cycle.
"""

# Runtime 10 ms Beats 97.07%
# Memory 11.51 MB Beats 97.07%
def isPrefixString(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: bool
    """
    ss = ""; ll = len(s)
    for w in words:
        ss += w
        if len(ss) > ll: break
        if ss == s: return True
    return False


# Runtime 18 ms Beats 54.63%
# Memory 11.56 MB Beats 97.07%
def isPrefixString3(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: bool
    """
    ss=""
    for i in range(len(words)):
        ss+=words[i]
        if ss==s: return True
    return False

# Runtime 18 ms Beats 54.63%
# Memory 11.90 MB Beats 5.85%
def isPrefixString2(s, words):
    ss = ""
    for w in words:
        ss += w
        if ss == s: return True
    return False

# Runtime 12 ms Beats 88.29%
# Memory 11.54 MB Beats 97.07%
def isPrefixString0(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: bool
    """
    prefix = ""
    i = 0
    while len(prefix) < len(s) and i < len(words):
        prefix += words[i]
        i += 1
    return prefix == s
