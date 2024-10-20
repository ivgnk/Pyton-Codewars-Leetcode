"""
Done 20.10.2024. Topics: String
243. Shortest Word Distance
https://leetcode.com/problems/shortest-word-distanc
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2,
return the shortest distance between these two words in the list.

Example 1:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3

Example 2:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1

Constraints:
2 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2
"""
import re
def shortestDistance(wordsDict, word1, word2):
    w1=[i for i, v in enumerate(wordsDict) if v == word1]
    w2=[i for i, v in enumerate(wordsDict) if v == word2]
    mmin = 1000000
    for i in w1:
        for j in w2:
            mmin=min(mmin,abs(i-j))
    return mmin

# print(shortestDistance(wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"))
# print(shortestDistance(wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"))

# https://leetcode.ca/2016-07-30-243-Shortest-Word-Distance/
class Solution:
    def shortestDistance(self, wordsDict, word1, word2: str) -> int:
        i = j = -1
        ans = float('inf')
        for k, w in enumerate(wordsDict):
            if w == word1:
                i = k
            if w == word2:
                j = k
            if i != -1 and j != -1:
                ans = min(ans, abs(i - j))
        return ans
t=Solution()
print(t.shortestDistance(wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"))
print(t.shortestDistance(wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"))
