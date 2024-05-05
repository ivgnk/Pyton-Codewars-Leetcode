"""
Done 05.05.2024
1684. Count the Number of Consistent Strings
https://leetcode.com/problems/count-the-number-of-consistent-strings/description/

You are given a string allowed consisting of distinct characters and an array of strings words.
A string is consistent if all characters in the string appear in the string allowed.
Return the number of consistent strings in the array words.

Example 1:
Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

Example 2:
Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.

Example 3:
Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
"""


def countConsistentStrings(allowed, words):
    """
    :type allowed: str
    :type words: List[str]
    :rtype: int
    """
    # Runtime 194 ms Beats 30.32% of users with Python
    # Memory 14.27 MB Beats 43.44% of users with Python
    # n = 0
    # for w in words:
    #     if all(s in allowed for s in w):
    #         n = n + 1
    # return n

    # Runtime 192 ms Beats 33.12% of users with Python
    # Memory 14.37 MB Beats 20.86% of users with Python
    # return sum(1 for w in words if all(s in allowed for s in w))

    # Runtime 197 ms Beats 27.74% of users with Python
    # Memory 14.12 MB Beats 72.69% of users with Python
    return sum(all(s in allowed for s in w) for w in words)


