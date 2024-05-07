"""
Done 08.05.2024. Topics: Array, String, String Matching
2185. Counting Words With a Given Prefix
https://leetcode.com/problems/counting-words-with-a-given-prefix/description/

You are given an array of strings words and a string pref.
Return the number of strings in words that contain pref as a prefix.
A prefix of a string s is any leading contiguous substring of s.

Example 1:
Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".

Example 2:
Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0
Explanation: There are no strings that contain "code" as a prefix.
"""

# Runtime 15 ms Beats 90.11% of users with Python
# Memory 12.05 MB Beats 7.60% of users with Python

def prefixCount(words, pref):
    """
    :type words: List[str]
    :type pref: str
    :rtype: int
    """
    return sum(1 for w in words if w.find(pref)==0)
