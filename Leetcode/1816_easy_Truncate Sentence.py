'''
1816. Truncate Sentence
https://leetcode.com/problems/truncate-sentence/description/

A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
Each of the words consists of only uppercase and lowercase English letters (no punctuation).

For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
You are given a sentence s and an integer k.
You want to truncate s such that it contains only the first k words. Return s after truncating it.

Example 1:

Input: s = "Hello how are you Contestant", k = 4
Output: "Hello how are you"
Explanation:
The words in s are ["Hello", "how" "are", "you", "Contestant"].
The first 4 words are ["Hello", "how", "are", "you"].
Hence, you should return "Hello how are you".
'''

# Runtime 3 ms Beats 99.69% of users with Python
# Memory 11.68 MB Beats 80.12% of users with Python

def truncateSentence(s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    s1 = s.split()
    s2 = s1[:k]
    return ' '.join(s2)