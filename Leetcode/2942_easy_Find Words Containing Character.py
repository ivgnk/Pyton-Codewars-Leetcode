"""
2942. Find Words Containing Character
https://leetcode.com/problems/find-words-containing-character/description/

You are given a 0-indexed array of strings words and a character x.
Return an array of indices representing the words that contain the character x.
Note that the returned array may be in any order.

Example 1:
Input: words = ["leet","code"], x = "e"
Output: [0,1]
Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.

Example 2:
Input: words = ["abc","bcd","aaaa","cbc"], x = "a"
Output: [0,2]
Explanation: "a" occurs in "abc", and "aaaa". Hence, we return indices 0 and 2.
"""


# Runtime 30 ms Beats 88.21% of users with Python
# Memory 11.76 MB Beats 40.95% of users with Python

def findWordsContaining(words, x):
    """
    :type words: List[str]
    :type x: str
    :rtype: List[int]
    """
    return [i for i in range(len(words)) if words[i].find(x) >= 0]