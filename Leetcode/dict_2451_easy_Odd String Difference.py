'''
Done 20.08.2024. Topics: Hash Table, String
2451. Odd String Difference
https://leetcode.com/problems/odd-string-difference

You are given an array of equal-length strings words.
Assume that the length of each string is n.

Each string words[i] can be converted into a difference integer array difference[i]
of length n - 1 where difference[i][j] = words[i][j+1] - words[i][j] where 0 <= j <= n - 2.
Note that the difference between two letters is the difference between their positions in the alphabet
i.e. the position of 'a' is 0, 'b' is 1, and 'z' is 25.

For example, for the string "acb", the difference integer array is [2 - 0, 1 - 2] = [2, -1].
All the strings in words have the same difference integer array, except one. You should find that string.

Return the string in words that has different difference integer array.

Example 1:
Input: words = ["adc","wzy","abc"]
Output: "abc"
Explanation:
- The difference integer array of "adc" is [3 - 0, 2 - 3] = [3, -1].
- The difference integer array of "wzy" is [25 - 22, 24 - 25]= [3, -1].
- The difference integer array of "abc" is [1 - 0, 2 - 1] = [1, 1].
The odd array out is [1, 1], so we return the corresponding string, "abc".

Example 2:
Input: words = ["aaa","bob","ccc","ddd"]
Output: "bob"
Explanation: All the integer arrays are [0, 0] except for "bob", which corresponds to [13, -13].

Constraints:
3 <= words.length <= 100
n == words[i].length
2 <= n <= 20
words[i] consists of lowercase English letters.

Hint 1
Find the difference integer array for each string.
Hint 2
Compare them to find the odd one out.
'''

# Runtime 21 ms Beats 29.82%
# Memory 11.78 MB Beats 38.60%
from copy import copy, deepcopy
def find_unique_sublist2(sublists):

    # Dictionary to count the frequency of each sublist
    sublist_count = defaultdict(int)

    # Count the frequency of each sublist
    for sublist in sublists:
        sublist_tuple = tuple(sublist)  # Convert list to tuple to use as dictionary key
        sublist_count[sublist_tuple] += 1

    # Find the sublist that appears only once
    for i,sublist in enumerate(sublists):
        sublist_tuple = tuple(sublist)
        if sublist_count[sublist_tuple] == 1:
            return i

def oddString2(words):
    """
    :type words: List[str]
    :rtype: str
    """
    llenw = len(words[0])
    diff = [0] * (llenw - 1)
    arrdiff = []
    for ss in words:
        for i in range(len(ss)-1):
            diff[i] = ord(ss[i + 1]) - ord(ss[i])
        arrdiff.append(copy(diff))

    return words[find_unique_sublist2(arrdiff)]

#############################################################
# Runtime 16 ms Beats 57.89%
# Memory 11.78 MB Beats 38.60%

from collections import defaultdict
def find_unique_sublist(sublists):
    sublist_count = defaultdict(int)
    sl= [tuple(sublist) for sublist in sublists ]

    for sl1 in sl:
        sublist_count[sl1] += 1

    for i,sl1 in enumerate(sl):
        if sublist_count[sl1] == 1:
            return i

def oddString(words):
    """
    :type words: List[str]
    :rtype: str
    """
    llenw = len(words[0])
    diff = [0] * (llenw - 1)
    arrdiff = []
    for ss in words:
        for i in range(len(ss)-1):
            diff[i] = ord(ss[i + 1]) - ord(ss[i])
        arrdiff.append(copy(diff))

    return words[find_unique_sublist(arrdiff)]

print(oddString(["adc","wzy","abc"]))

