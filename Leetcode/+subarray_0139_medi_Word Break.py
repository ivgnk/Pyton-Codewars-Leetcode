"""
13.09.2024. Topics: String, Dynamic Programming
139. Word Break
https://leetcode.com/problems/word-break/description/

Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""

# https://leetcode.com/problems/word-break/solutions/5742606/n-3-dynamic-programming-solution/
# Runtime 21 ms Beats 57.33%
# Memory 11.79 MB Beats 79.46%
# Runtime 19 ms Beats 70.67%
# Memory 11.72 MB Beats 79.46%

def wordBreak(s, wordDict):
    words = set(wordDict)
    dp = [False for _ in range(len(s) + 1)]
    dp[0] = True

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if s[i:j] in words and dp[i]:
                dp[j] = True
    return dp[-1]


from icecream import ic
def wordBreak2(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    lw = len(wordDict)
    lwall = [len(word) for word in wordDict]
    ls = len(s)
    ress = ' ' * ls
    for word in wordDict:
        lw1 = len(word)
        n = ls // lw1
        if ls % lw1 == 0 and word * n == s:
            return True

    if ''.join(wordDict) == s: return True
    Tr = [True] * len(wordDict)
    while any(Tr):
        for i, word in enumerate(wordDict):
            Tr[i] = word in s
            if Tr[i]:
                s = s.replace(word, ' ' * lwall[i], 1)
    if s == ress: return True

    wordDict = sorted(wordDict)
    if ''.join(wordDict) == s: return True
    print('last',wordDict)
    Tr = [True] * len(wordDict)
    while any(Tr):
        for i, word in enumerate(wordDict):
            Tr[i] = word in s
            if Tr[i]:
                s = s.replace(word, ' ' * lwall[i], 1)
    return s == ress


def wordBreak3(self, s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    Tr=True; ll=len(wordDict)
    tr=[False]*ll
    while Tr:
        for i in range(ll):
            tr[i]=wordDict[i] in s
            if tr[i]: s=s.replace(wordDict[i],'')
        Tr=any(tr)
    s.strip()
    return len(s)==0

ic(wordBreak(s = "cars", wordDict = ["car","ca","rs"]))
