"""
Done 09.07.2024. Topics: Array, String, Greedy
2900. Longest Unequal Adjacent Groups Subsequence I
https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/description/

You are given a string array words and a binary array groups both of length n,
where words[i] is associated with groups[i].

Your task is to select the longest alternating subsequence from words.
A subsequence of words is alternating if for any two consecutive strings in the sequence,
their corresponding elements in the binary array groups differ.

Essentially, you are to choose strings such that adjacent elements
have non-matching corresponding bits in the groups array.

Formally, you need to find the longest subsequence of an array of indices [0, 1, ..., n - 1]
denoted as [i0, i1, ..., ik-1], such that groups[ij] != groups[ij+1]
for each 0 <= j < k - 1 and then find the words corresponding to these indices.

Return the selected subsequence. If there are multiple answers, return any of them.
Note: The elements in words are distinct.

Example 1:
Input: words = ["e","a","b"], groups = [0,0,1]
Output: ["e","b"]
Explanation: A subsequence that can be selected is ["e","b"] because groups[0] != groups[2].
Another subsequence that can be selected is ["a","b"] because groups[1] != groups[2].
It can be demonstrated that the length of the longest subsequence of indices that satisfies the condition is 2.

Example 2:
Input: words = ["a","b","c","d"], groups = [1,0,1,1]
Output: ["a","b","c"]

Explanation: A subsequence that can be selected is ["a","b","c"] because
groups[0] != groups[1] and groups[1] != groups[2].
Another subsequence that can be selected is ["a","b","d"] because groups[0] != groups[1] and groups[1] != groups[3].
It can be shown that the length of the longest subsequence of indices that satisfies the condition is 3.

Constraints:
1 <= n == words.length == groups.length <= 100
1 <= words[i].length <= 10
groups[i] is either 0 or 1.
words consists of distinct strings.
words[i] consists of lowercase English letters.

Hint 1
This problem can be solved greedily.
Hint 2
Begin by constructing the answer starting with the first number in groups.
Hint 3
For each index i in the range [1, n - 1], add i to the answer if groups[i] != groups[i - 1].
"""

# Runtime 52 ms Beats 5.30%
# Memory 11.83 MB Beats# 7.95%
from icecream import ic
def getLongestSubsequence2(words, groups):
    """
    :type words: List[str]
    :type groups: List[int]
    :rtype: List[str]
    """
    ll=len(groups)
    res=[]; mlen=0
    for i in range(ll):
        curr=groups[i]
        res1=[i]; mlen1=1; last=-1
        j=i+1
        while j<=ll-1:
            if groups[j] != curr:
                curr=groups[j]
                res1.append(j)
                mlen1=mlen1+1
            j=j+1
        if mlen1>mlen:
            res=[words[i] for i in res1]; mlen=mlen1
    return res

# Runtime 32 ms Beats 87.42%
# Memory 11.77 MB Beats 27.15%
# Runtime 35 ms Beats 68.21%
# Memory 11.80 MB Beats 27.15%
def getLongestSubsequence(words, groups):
    res=[0]; last=groups[0]
    for i,s  in enumerate(groups):
        if last != s:
            last=s; res.append(i)
    return [words[i] for i in res]

ic(getLongestSubsequence( words = ["a","b","c","d"], groups = [1,0,1,1]))




