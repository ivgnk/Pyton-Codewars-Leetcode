"""
Done 22.10.2024. Topics: Hash Table, String
2068. Check Whether Two Strings are Almost Equivalent
https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/description

Two strings word1 and word2 are considered almost equivalent if the differences between the
frequencies of each letter from 'a' to 'z' between word1 and word2 is at most 3.

Given two strings word1 and word2, each of length n,
return true if word1 and word2 are almost equivalent, or false otherwise.
The frequency of a letter x is the number of times it occurs in the string.

Two strings word1 and word2 are considered almost equivalent if
the differences between the frequencies of each letter from 'a' to 'z'
between word1 and word2 is at most 3.

Given two strings word1 and word2, each of length n, return true if word1 and word2 are
almost equivalent, or false otherwise.

The frequency of a letter x is the number of times it occurs in the string.

Example 1:
Input: word1 = "aaaa", word2 = "bccb"
Output: false
Explanation: There are 4 'a's in "aaaa" but 0 'a's in "bccb".
The difference is 4, which is more than the allowed 3.

Example 2:
Input: word1 = "abcdeef", word2 = "abaaacc"
Output: true
Explanation: The differences between the frequencies of each letter in word1 and word2 are at most 3:
- 'a' appears 1 time in word1 and 4 times in word2. The difference is 3.
- 'b' appears 1 time in word1 and 1 time in word2. The difference is 0.
- 'c' appears 1 time in word1 and 2 times in word2. The difference is 1.
- 'd' appears 1 time in word1 and 0 times in word2. The difference is 1.
- 'e' appears 2 times in word1 and 0 times in word2. The difference is 2.
- 'f' appears 1 time in word1 and 0 times in word2. The difference is 1.

Example 3:
Input: word1 = "cccddabba", word2 = "babababab"
Output: true
Explanation: The differences between the frequencies of each letter in word1 and word2 are at most 3:
- 'a' appears 2 times in word1 and 4 times in word2. The difference is 2.
- 'b' appears 2 times in word1 and 5 times in word2. The difference is 3.
- 'c' appears 3 times in word1 and 0 times in word2. The difference is 3.
- 'd' appears 2 times in word1 and 0 times in word2. The difference is 2.


Constraints:
n == word1.length == word2.length
1 <= n <= 100
word1 and word2 consist only of lowercase English letters.

My Solution
✏️ Easy and fast (0 ms) Python solution /with dictionary and set/ for Problem 2068
https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/solutions/5951716/easy-and-fast-0-ms-python-solution-with-dictionary-and-set-for-problem-2068/
Intuition
Use dictionary (with get) and set
Use "from collections import Counter"
Approach
Letter-by-letter comparison
"""

from collections import Counter
# Runtime 0 ms Beats 100.00%
# Memory 11.78 MB Beats 19.30%
# Time Complexity O(N)
# Space Complexity O(N)

def checkAlmostEquivalent(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: bool
    """
    ss=set(word1+word2)
    d1=dict(Counter(word1))
    d2=dict(Counter(word2))
    for ss1 in ss:
        n1=d1.get(ss1,0)
        n2=d2.get(ss1,0)
        if abs(n1-n2)>3: return False
    return True

print(checkAlmostEquivalent(word1 = "aaaa", word2 = "bccb"))
print(checkAlmostEquivalent(word1 = "abcdeef", word2 = "abaaacc"))
print(checkAlmostEquivalent( word1 = "cccddabba", word2 = "babababab"))
# print(set("aaaa"+"bccb"))