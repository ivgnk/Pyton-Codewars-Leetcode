'''
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/description/

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    prf =""
    llen = len(strs)
    if (llen==1): return strs[0]
    if (not any(strs)): return strs[0]
    llen_all = [len(s) for s in strs]
    s1=strs[0]
    for key,s in enumerate(s1):
        b = True
        for i in range(1,llen):
            if key>llen_all[i]-1: return prf
            b1 = (s == strs[i][key])
            if (not b1):
                return prf
        prf = prf + s
    return prf

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["","",""]))
print(longestCommonPrefix(["ab","a"]))