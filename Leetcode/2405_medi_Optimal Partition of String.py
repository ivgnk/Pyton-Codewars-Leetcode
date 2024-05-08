"""
Done 08.05.2024. Topics: Hash Table, String, Greedy
2405. Optimal Partition of String
https://leetcode.com/problems/optimal-partition-of-string/description/

Given a string s, partition the string into one or more substrings such that the characters in each substring are unique.
That is, no letter appears in a single substring more than once.
Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.

Example 1:
Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.

Example 2:
Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").

Hint 1
Try to come up with a greedy approach.
Hint 2
From left to right, extend every substring in the partition as much as possible.
"""

# Runtime 74 ms Beats 86.24% of users with Python
# Memory 14.62 MB Beats 29.99% of users with Python

def partitionString(s):
    """
    :type s: str
    :rtype: int
    """
    res=[]; s2=''
    for s1 in s:
        if s2=='': s2=s1
        elif s1 in s2:
            res.append(s2)
            s2=s1
        else: s2=s2+s1
    if s2 != '': res.append(s2)
    return len(res)

print(partitionString("abacaba"))


