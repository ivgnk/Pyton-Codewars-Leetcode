"""
Done 20.05.2024. Topics: Array, Hash Table, String, Counting
2085. Count Common Words With One Occurrence
Given two string arrays words1 and words2,
return the number of strings that appear exactly once in each of the two arrays.

Example 1:
Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
Output: 2
Explanation:
- "leetcode" appears exactly once in each of the two arrays. We count this string.
- "amazing" appears exactly once in each of the two arrays. We count this string.
- "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
- "as" appears once in words1, but does not appear in words2. We do not count this string.
Thus, there are 2 strings that appear exactly once in each of the two arrays.

Example 2:
Input: words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
Output: 0
Explanation: There are no strings that appear in each of the two arrays.

Example 3:
Input: words1 = ["a","ab"], words2 = ["a","a","a","ab"]
Output: 1
Explanation: The only string that appears exactly once in each of the two arrays is "ab".
"""

# Runtime 79 ms Beats 66.32% of users with Python
# Memory 12.28 MB Beats 23.68% of users with Python
# Runtime 77 ms Beats 66.32% of users with Python
# Memory 12.22 MB Beats 23.68% of users with Python
from collections import Counter
def countWords2(words1, words2):
    """
    :type words1: List[str]
    :type words2: List[str]
    :rtype: int
    """
    l1 = dict(Counter(words1))
    l2 = dict(Counter(words2))
    # print(l1,l2)

    return sum([1
                for s1 in words1
                    if s1 in words2
                        if l1[s1]==l2[s1] and l1[s1]==1])


# Runtime 245 ms Beats 5.27% of users with Python
# Memory 12.10 MB Beats 81.05% of users with Python

def countWords3(words1, words2):
    """
    :type words1: List[str]
    :type words2: List[str]
    :rtype: int
    """
    l1 = [words1.count(s1) for s1 in words1]
    l2 = [words2.count(s2) for s2 in words2]
    print(l1)
    print(l2)
    return sum([1
                for i,s1 in enumerate(words1)
                    if s1 in words2
                        if l1[i]==1
                            if l1[i]==l2[words2.index(s1)]])




# https://leetcode.com/problems/count-common-words-with-one-occurrence/solutions/4569162/very-simple-one-python-python3/
# Runtime 157 ms Beats 34.74% of users with Python
# Memory 12.14 MB Beats 51.05% of users with Python
def countWords(words1, words2):
     """
     :type words1: List[str]
     :type words2: List[str]
     :rtype: int
     """
     count=0
     for i in words1:
        if words1.count(i)==1 and words2.count(i)==1:
            count=count+1
     return count

print(countWords(words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]))
