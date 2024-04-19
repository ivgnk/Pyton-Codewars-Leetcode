"""
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

from icecream import ic
def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    if s==''.join(wordDict): return True
    wordDict = sorted(wordDict)
    Tr=True; ll=len(wordDict)
    tr=[False]*ll
    while Tr:
        for i in range(ll):
            tr[i]=wordDict[i] in s
            if tr[i]: s=s.replace(wordDict[i],'')
        Tr=any(tr)
        ic(s)
    s.strip()
    ic(s)
    return len(s)==0

print(wordBreak( s = "ccbb", wordDict = ["bc","cb"]))