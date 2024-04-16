"""
Given a string paragraph and a string array of the banned words banned,
return the most frequent word that is not banned.
It is guaranteed there is at least one word that is not banned, and that the answer is unique.
The words in paragraph are case-insensitive and the answer should be returned in lowercase.

Example 1:
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.

Example 2:
Input: paragraph = "a.", banned = []
Output: "a"
"""

# Runtime 16 ms Beats 78.47% of users with Python
# Memory 11.92 MB Beats 21.81% of users with Python

from collections import Counter
def mostCommonWord(paragraph, banned) -> str:
    paragraph = paragraph.lower()
    lst = ['.', ',', '!', '?', ';', '\'']
    for s1 in lst:
        paragraph = paragraph.replace(s1, ' ')
    s = paragraph.split()
    dd = dict(Counter(s))
    ml = sorted(dd.items(), key=lambda x: x[1], reverse=True)
    for i in range(len(dd)):
        if ml[i][0] not in banned:
            return ml[i][0]

print(mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))