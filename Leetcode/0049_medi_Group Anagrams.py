"""
Done 21.06.2024. Topics: Array, Hash Table, String, Sorting

49. Group Anagrams
https://leetcode.com/problems/group-anagrams/description/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""

# Runtime 2656 ms Beats 5.01%
# Memory 16.84 MB Beats 31.91%
def groupAnagrams2(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    ll=len(strs)
    if ll==1: return [strs]

    dd =[sorted(s1) for s1 in strs]
    used=[False]*ll
    res=[]
    for i in range(ll):
        curr=[]
        if not used[i]:
            base = dd[i]
            curr.append(strs[i])
            used[i]=True
            for j in range(i+1, ll):
                if not used[j]:
                    if base==dd[j]:
                        curr.append(strs[j])
                        used[j]=True
        if curr !=[]:
            res.append(curr)
    return res

# Runtime 61 ms Beats 95.51%
# Memory 16.36 MB Beats 36.12%
# on tne base of
# https://leetcode.com/problems/group-anagrams/description/comments/1574673
def groupAnagrams(strs):
    ll=len(strs)
    if ll==1: return [strs]
    as_dd =[''.join(sorted(s1)) for s1 in strs]
    dd=dict()
    for i,word in enumerate(as_dd):
        if word in dd:
            dd[word].append(strs[i])
        else:
            dd[word]=[strs[i]]
    return [v for k,v, in dd.items()]

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# print(list('ytyu'))