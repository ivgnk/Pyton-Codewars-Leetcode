"""
Algo: https://en.wikipedia.org/wiki/Levenshtein_distance
Расстояние Левенштейна для чайников
https://habr.com/ru/articles/676858/
https://pypi.org/project/python-Levenshtein/

08.11.2024. Topics: String, Dynamic Programming
72. Edit Distance
https://leetcode.com/problems/edit-distance/description/

Given two strings word1 and word2,
return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:
Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Constraints:
0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
"""

# Runtime 72 ms Beats 77.37%
# Memory 11.68 MB Beats 96.88%
def minDistance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    n, m = len(word1), len(word2)
    if n > m:
        word1, word2 = word2, word1
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if word1[j - 1] != word2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]


def levenstein(str_1, str_2):
    n, m = len(str_1), len(str_2)
    if n > m:
        str_1, str_2 = str_2, str_1
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]

# print(levenstein("БИБА","БОБА"))
# print(levenstein('АВСТРИЯ', 'АВСТРАЛИЯ'))
# print(levenstein('КОТИК', 'СКОТИНА'))
print(minDistance(word1 = "horse", word2 = "ros"))
print(minDistance(word1 = "intention", word2 = "execution"))