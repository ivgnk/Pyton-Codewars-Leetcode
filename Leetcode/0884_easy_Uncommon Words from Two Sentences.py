'''
Done 20.05.2024. Topics: Hash Table, String
884. Uncommon Words from Two Sentences

A sentence is a string of single-space separated words where each word consists only of lowercase letters.
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

Example 1:
Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]

Example 2:
Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]
'''

# The task is incorrectly formulated
# Conflicting tests
# Input s1 = "s z z z s" s2 = "s z ejt"
# Expected ["ejt"]
#  and
# Input: s1 = "apple apple", s2 = "banana"
# Expected  ["banana"]



# Runtime 16 ms Beats 49.80% of users with Python
# Memory 11.74 MB Beats 45.71% of users with Python
# Runtime 14 ms Beats 62.86% of users with Python
# Memory 11.70 MB Beats 45.71% of users with Python

from icecream import ic
from collections import Counter
def uncommonFromSentences(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: List[str]
    """
    lst1=s1.split(); d1=dict(Counter(lst1)); s1n=[]
    print(lst1)
    lst2=s2.split(); d2=dict(Counter(lst2)); s2n=[]
    print(lst2)

    for k,v in d1.items():
        if v==1 and k not in lst2: s1n.append(k)
    ic(s1n)

    for k,v in d2.items():
        if v==1 and k not in lst1: s2n.append(k)
    ic(s2n)

    return s1n+s2n

ic('result=',uncommonFromSentences(s1 = "d b zu d t", s2 = "udb zu ap"))
# print(uncommonFromSentences( s1 = "apple apple", s2 = "banana"))
# print('result=',uncommonFromSentences( s1 ="s z z z s", s2 ="s z ejt"))