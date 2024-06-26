"""
Done 27.06.2024. Topics: String
1408. String Matching in an Array
https://leetcode.com/problems/string-matching-in-an-array/description/

Given an array of string words, return all strings in words that is a substring of another word.
You can return the answer in any order.
A substring is a contiguous sequence of characters within a string

Example 1:
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

Example 2:
Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".

Example 3:
Input: words = ["blue","green","bu"]
Output: []
Explanation: No string of words is substring of another string.

Hint 1
Bruteforce to find if one string is substring of another or use KMP algorithm.
"""


# Runtime 27 ms Beats 17.92%
# Memory 11.61 MB Beats 57.23%
# Runtime 21 ms Beats 47.98%
# Memory 11.62 MB Beats 57.23%
# Runtime 19 ms Beats 63.58%
# Memory 11.62 MB Beats 57.23%
# Runtime 18 ms Beats 71.10%
# Memory 11.51 MB Beats 87.28%
def stringMatching(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    rll = range(len(words))
    res = list(set([words[j] for i in rll for j in rll  if i !=j and words[j] in words[i]]))
    return res

print(stringMatching(["mass","as","hero","superhero"]))

