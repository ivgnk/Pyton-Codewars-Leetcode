"""
Done 13.08.2024. Topics: Array, Hash Table, String
953. Verifying an Alien Dictionary
https://leetcode.com/problems/verifying-an-alien-dictionary/description/

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet,
return true if and only if the given words are sorted lexicographically in this alien language.

Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.

Solution
✏️ Easy Python solution with lists
Intuition
For words, create an array of letter indexes according to the specified alphabet.

Approach
Use list comprehension.
Done 13.08.2024:
Runtime 38 ms Beats 73.62%
Memory 16.44 MB Beats 88.96%
"""

# Runtime 44 ms Beats 30.14%
# Memory 16.63 MB Beats 16.93%
# Runtime 38 ms Beats 73.62%
# Memory 16.44 MB Beats 88.96%
def isAlienSorted(words, order):
    """
    :type words: List[str]
    :type order: str
    :rtype: bool
    """
    s=[[order.index(let) for let in w] for w in words]
    for i in range(1,len(s)):
        if s[i-1]>s[i]: return False
    return True

# print(isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz")) # True
# print(isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz")) # False
# print(isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz")) # False
print(isAlienSorted(words = ["zirqhpfscx","zrmvtxgelh","vokopzrtc","nugfyso","rzdmvyf","vhvqzkfqis","dvbkppw","ttfwryy","dodpbbkp","akycwwcdog"],
order = "khjzlicrmunogwbpqdetasyfvx"))


def isAlienSorted(words, order) -> bool:
    if len(words) == 1:
        return True

    order_map = {}

    for index, val in enumerate(order):
        order_map[val] = index

    for i in range(len(words) - 1):
        for j in range(len(words[i])):
            if j >= len(words[i + 1]):
                return False

            if words[i][j] != words[i + 1][j]:
                if order_map[words[i][j]] > order_map[words[i + 1][j]]:
                    return False
                break

    return True
# print([3, 5, 7, 16, 1, 15, 23, 21, 6, 25]> [3, 7, 8, 24, 19, 25, 12, 18, 4, 1] )

