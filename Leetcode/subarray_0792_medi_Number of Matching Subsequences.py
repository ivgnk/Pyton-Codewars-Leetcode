"""
Done 25.05.2024. Topics: String
792. Number of Matching Subsequences
https://leetcode.com/problems/number-of-matching-subsequences/description/

A subsequence of a string is a new string generated from the original string with
some characters (can be none) deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".

Example 1:
Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

Example 2:
Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
"""

# Runtime 1015 ms Beats 41.82% of users with Python
# Memory 14.92 MB Beats 90.91% of users with Python

# https://leetcode.com/problems/number-of-matching-subsequences/solutions/1289476/easy-approach-well-explained-95-faster/
# https://docs-python.ru/tutorial/operatsii-tekstovymi-strokami-str-python/metod-str-find/
def numMatchingSubseq(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: int
    """
    def is_sub(word):
        index = -1
        for ch in word:
            index = s.find(ch, index + 1)
            if index == -1:
                return False
        return True

    c = 0
    for word in words:
        if is_sub(word):
            c += 1
    return c



# Wrong Answer -- 13 / 53 testcases passed
import re
def numMatchingSubseq2(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: int
    """
    ssum=0
    for jj,w in enumerate(words):
        ll = len(w)
        if ll==1:
            if w in s: ssum=ssum+1
        else:
            regs=''.join([w[i]+'.?' if i<ll-1 else w[i] for i in range(ll)])
            print(regs)
            m = re.search(regs, s)
            if m: ssum=ssum+1
        print(jj,w,ssum)
    return ssum


print(numMatchingSubseq(s = "abcde", words = ["a","bb","acd","ace"]))
print(numMatchingSubseq(s = "dsahjpjauf", words = ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]))