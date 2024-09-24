"""
24.09.2024. Hash Table, String. Trie
3043. Find the Length of the Longest Common Prefix
https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/description

You are given two arrays with positive integers arr1 and arr2.

A prefix of a positive integer is an integer formed by one or more of its digits, starting from its leftmost digit.
For example, 123 is a prefix of the integer 12345, while 234 is not.

A common prefix of two integers a and b is an integer c, such that c is a prefix of both a and b.
For example, 5655359 and 56554 have a common prefix 565 while 1223 and 43456 do not have a common prefix.

You need to find the length of the longest common prefix between all pairs of integers (x, y)
such that x belongs to arr1 and y belongs to arr2.

Return the length of the longest common prefix among all pairs. If no common prefix exists among them, return 0.

Example 1:
Input: arr1 = [1,10,100], arr2 = [1000]
Output: 3
Explanation: There are 3 pairs (arr1[i], arr2[j]):
- The longest common prefix of (1, 1000) is 1.
- The longest common prefix of (10, 1000) is 10.
- The longest common prefix of (100, 1000) is 100.
The longest common prefix is 100 with a length of 3.

Example 2:
Input: arr1 = [1,2,3], arr2 = [4,4,4]
Output: 0
Explanation: There exists no common prefix for any pair (arr1[i], arr2[j]), hence we return 0.
Note that common prefixes between elements of the same array do not count.

Constraints:
1 <= arr1.length, arr2.length <= 5 * 104
1 <= arr1[i], arr2[i] <= 108
"""
from icecream import ic
# Time Limit Exceeded - 707 / 718 testcases passed
def longestCommonPrefix77(arr1, arr2):
    prf_set=set()
    for a_ in arr1: # по словам
        a=str(a_)
        prf=''
        for ch in a: # по буквам
            prf+=ch
            prf_set.add(prf)
    ml=0
    for a_ in arr2:
        a=str(a_)
        for k in prf_set:
            if a.startswith(k):
                ml=max(ml,len(k))
    return ml

# Runtime 908 ms Beats 61.74%
# Memory 28.50 MB Beats 76.92%
def longestCommonPrefix(arr1, arr2):
    prf = set()
    # Generate all prefixes from the first array
    for num in arr1:
        s = str(num)
        prefix = ""
        for ch in s:
            prefix += ch
            prf.add(prefix)
    ans = 0
    # Check prefixes from the second array
    for num in arr2:
        s = str(num)
        prefix = ""
        for ch in s:
            prefix += ch
            if prefix in prf:
                ans = max(ans, len(prefix))  # Update the longest common prefix length
    return ans

# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/solutions/5827125/easy-solution-python/
# Runtime 1008 ms Beats 31.97%
# Memory 28.21 MB Beats 89.66%
def longestCommonPrefix__(arr1, arr2):
    arr1Set, res = set(), 0
    for x in arr1:
        s = str(x)
        n = len(s)
        for i in range(1,n+1): arr1Set.add(s[:i])
    for x in arr2:
        s = str(x)
        n = len(s)
        for i in range(1,n+1):
            if s[:i] in arr1Set: res = max(res, i)
    return res

ic(longestCommonPrefix(arr1=[1, 10, 100], arr2=[1000]))  # 3
ic(longestCommonPrefix(arr1=[1, 2, 3], arr2=[4, 4, 4]))  # 0
ic(longestCommonPrefix(arr1=[10], arr2=[17, 11]))  # 1
ic(longestCommonPrefix(arr1=[1, 3], arr2=[32, 22]))  # 1



def longestCommonPrefix5(arr1, arr2):
    """
    :type arr1: List[int]
    :type arr2: List[int]
    :rtype: int
    """
    as1=set(arr1)
    a1=[str(i) for i in as1]

    prf_set=set()
    for a in a1: # по словам
        prf=''
        for ch in a: # по буквам
            prf+=ch
            prf_set.add(prf)
    prf_dd={s:len(s) for s in prf_set}
    mml=max([i for i in prf_dd.values()])
    ml=0
    for a_ in arr2:
        a=str(a_)
        for k,v in prf_dd.items():
            if a.startswith(k):
                ml=max(ml,v)
                if ml==mml:
                    return ml
    return ml



# Time Limit Exceeded - 710 / 718 testcases passed
def longestCommonPrefix4(arr1, arr2):
    """
    :type arr1: List[int]
    :type arr2: List[int]
    :rtype: int
    """
    as1=set(arr1)
    as2=set(arr2)
    a1=[str(i) for i in as1]
    a2=[str(i) for i in as2]

    prf_set=set()
    for a in a1: # по словам
        prf=''
        for ch in a: # по буквам
            prf+=ch
            prf_set.add(prf)
    prf_dd={s:len(s) for s in prf_set}
    mml=max([i for i in prf_dd.values()])
    ml=0
    for a in a2:
        for k,v in prf_dd.items():
            if a.startswith(k):
                ml=max(ml,v)
                if ml==mml:
                    return ml
    return ml

    # for a in as2: # по словам от самого длинного из 1


# Time Limit Exceeded - 711 / 718 testcases passed
def longestCommonPrefix3(arr1, arr2):
    """
    :type arr1: List[int]
    :type arr2: List[int]
    :rtype: int
    """
    as1=set(arr1)
    as2=set(arr2)
    a1=sorted([str(i) for i in as1], reverse=True, key=lambda s: len(s)); la1=len(a1)
    a2=[str(i) for i in as2]
    ml=0; mml=len(a1[0])
    for a1p in a1: # по словам от самого длинного из 1
        prf = ''; cl = 0
        for s in a1p: # по буквам слова
            prf1 = prf + s; cl+=1
            if any([d.startswith(prf1) for d in a2]):
                prf = prf1
                ml=max(ml,cl)
                if ml==mml: return ml
            else:
                break
    return ml


# Wrong Answer - 77 / 718 testcases passed
# arr1 = [10] arr2 = [17, 11]
def longestCommonPrefix2(arr1, arr2):
    """
    :type arr1: List[int]
    :type arr2: List[int]
    :rtype: int
    """
    as1=set(arr1)
    as2=set(arr2)
    a1=sorted([str(i) for i in as1], reverse=True, key=lambda s: len(s))
    a2=[str(i) for i in as2]
    for a1p in a1:
        if all([a1p in d for d in a2]):
            return len(a1p)
    return 0
# r = sorted(['a', 'ab', 'abc', 'ab1','y'], reverse=True, key=lambda s: len(s))
# print(r)

# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/solutions/5827097/python-trie/
class TrieNode:
    def __init__(self, val):
        self.val = val
        self.next = dict()

class Trie:
    def __init__(self):
        self.root = TrieNode(val='')

    def add_word(self, word):
        node = self.root
        for char in word:
            if char not in node.next.keys():
                node.next[char] = TrieNode(char)
            node = node.next[char]

    def match_word(self, word):
        ans = 0
        node = self.root
        for char in word:
            if char not in node.next.keys():
                return ans
            node = node.next[char]
            ans += 1
        return ans

class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        ans = 0
        custom_trie = Trie()
        for x in arr1:
            custom_trie.add_word(str(x))
        for x in arr2:
            ans = max(ans, custom_trie.match_word(str(x)))
        return ans