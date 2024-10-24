"""
Done 24.10.2024. Topics: Hash Table, String, Sorting
2273. Find Resultant Array After Removing Anagrams
https://leetcode.com/problems/find-resultant-array-after-removing-anagrams

You are given a 0-indexed string array words, where words[i] consists of lowercase English letters.
In one operation, select any index i such that 0 < i < words.length and words[i - 1] and words[i] are anagrams,
and delete words[i] from words.
Keep performing this operation as long as you can select an index that satisfies the conditions.

Return words after performing all operations.
It can be shown that selecting the indices for each operation in any arbitrary order will lead to the same result.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase using all the original
letters exactly once. For example, "dacb" is an anagram of "abdc".

Example 1:
Input: words = ["abba","baba","bbaa","cd","cd"]
Output: ["abba","cd"]
Explanation:
One of the ways we can obtain the resultant array is by using the following operations:
- Since words[2] = "bbaa" and words[1] = "baba" are anagrams, we choose index 2 and delete words[2].
  Now words = ["abba","baba","cd","cd"].
- Since words[1] = "baba" and words[0] = "abba" are anagrams, we choose index 1 and delete words[1].
  Now words = ["abba","cd","cd"].
- Since words[2] = "cd" and words[1] = "cd" are anagrams, we choose index 2 and delete words[2].
  Now words = ["abba","cd"].
We can no longer perform any operations, so ["abba","cd"] is the final answer.

Example 2:
Input: words = ["a","b","c","d","e"]
Output: ["a","b","c","d","e"]
Explanation:
No two adjacent strings in words are anagrams of each other, so no operations are performed.

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.

Hint 1
Instead of removing each repeating anagram,
try to find all the strings in words which will not be present in the final answer.
Hint 2
For every index i, find the largest index j < i such that words[j] will be present in the final answer.
Hint 3
Check if words[i] and words[j] are anagrams.
If they are, then it can be confirmed that words[i] will not be present in the final answer.

My solution
✏️ Fast (5 ms) and easy Python solution for Problem 2273
https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/solutions/5961674/fast-5-ms-and-easy-python-solution-for-problem-2273/
# Intuition
For compare words do not use dictionary, but use letters sorting
"""

def removeAnagrams2(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    ll = len(words)
    lst = [''.join(sorted(list(w))) for w in words]
    lstn = [len(w) for w in words]
    if all(i == 1 for i in lstn):
        if not all([words[i - 1] == words[i] for i in range(1, ll)]):
            return words
    print('other')
    dd = dict();
    res = []
    for i, lst2 in enumerate(lst):
        if lst2 in dd:
            if words[i] in res:
                res.append(words[i])
        else:
            dd[lst2] = 1
            res.append(words[i])
    return res

# Runtime 5 ms Beats 100.00%
# Memory 11.46 MB Beats 96.48%
def removeAnagrams(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    ll = len(words)
    lst = [''.join(sorted(w)) for w in words]
    res=[words[0]]
    for i in range(1,ll):
        if lst[i]!=lst[i-1]:
            res.append(words[i])
    return res


print(removeAnagrams(["abba","baba","bbaa","cd","cd"]))
print(removeAnagrams(words = ["abba", "baba", "bbaa", "cd", "cd"]))