"""
Done 05.05.2024
1832. Check if the Sentence Is Pangram
https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/

A pangram is a sentence where every letter of the English alphabet appears at least once.
Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
"""

# Runtime 25 ms Beats 5.31% of users with Python
# Memory 11.71 MB Beats 27.26% of users with Python
# Runtime 17 ms Beats 38.09% of users with Python
# Memory 11.66 MB Beats 65.56% of users with Python
# Runtime 12 ms Beats 75.23% of users with Python
# Memory 11.72 MB Beats 27.26%# of users with Python

from collections import Counter
def checkIfPangram(sentence):
    """
    :type sentence: str
    :rtype: bool
    """
    dd=dict(Counter(sentence))
    return len(dd)>=26

