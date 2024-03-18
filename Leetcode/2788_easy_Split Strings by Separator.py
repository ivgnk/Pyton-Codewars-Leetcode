'''
2788. Split Strings by Separator
https://leetcode.com/problems/split-strings-by-separator/description/


Given an array of strings words and a character separator, split each string in words by separator.
Return an array of strings containing the new strings formed after the splits, excluding empty strings.

Notes
separator is used to determine where the split should occur, but it is not included as part of the resulting strings.
A split may result in more than two strings.
The resulting strings must maintain the same order as they were initially given.

Example 1:
Input: words = ["one.two.three","four.five","six"], separator = "."
Output: ["one","two","three","four","five","six"]
Explanation: In this example we split as follows:
"one.two.three" splits into "one", "two", "three"
"four.five" splits into "four", "five"
"six" splits into "six"
Hence, the resulting array is ["one","two","three","four","five","six"].
'''

def splitWordsBySeparator(words, separator):
    """
    :type words: List[str]
    :type separator: str
    :rtype: List[str]
    """
    res = []
    for ss in words:
        sspl = ss.split(separator)
        for ss1 in sspl:
            if (ss1 != ""):
                res.append(ss1)
    return res