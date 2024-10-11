"""
Done 11.10.2024. Topics: Hash Table, String
1897. Redistribute Characters to Make All Strings Equal
https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

You are given an array of strings words (0-indexed).
In one operation, pick two distinct indices i and j, where words[i] is a non-empty string,
and move any character from words[i] to any position in words[j].

Return true if you can make every string in words equal using any number of operations,
and false otherwise.

Example 1:
Input: words = ["abc","aabc","bc"]
Output: true
Explanation: Move the first 'a' in words[1] to the front of words[2],
to make words[1] = "abc" and words[2] = "abc".
All the strings are now equal to "abc", so return true.

Example 2:
Input: words = ["ab","a"]
Output: false
Explanation: It is impossible to make all the strings equal using the operation.

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.

Hint 1
Characters are independent—only the frequency of characters matters.
Hint 2
It is possible to distribute characters if all characters can be divided equally among all strings.

My solution
✏️ Super lazy Python solution, based on hints
https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/solutions/5899091/super-lazy-python-solution-based-on-hints/

Intuition
Count the numbers of letters

Approach
1) Make dictionary with letters
2) Find unique numbers in dictionary
3) All unique numbers must be divided by the number of words without remainder for True answer
"""

# Wrong Answer - 134 / 179 testcases passed
# dd: {'a': 15, 'b': 15, 'c': 45}, mi: 15, ma: 45
from icecream import ic
def makeEqual2(words):
    """
    :type words: List[str]
    :rtype: bool
    """
    ll = len(words)
    if ll == 1: return True

    dd=dict()
    for w in words:
        for s in w:
            if s in dd:
                dd[s]+=1
            else:
                dd[s]=1
    mi=1000000
    ma=-1
    for v in dd.values():
        mi=min(mi,v)
        ma=max(ma,v)
    ic(dd,mi,ma)
    return mi==ma and ma%ll==0

# Runtime 56 ms Beats 74.46%
# 16.77 MB Beats 44.54%
# Time Complexity O(N∗M)
# Space Complexity (N)
def makeEqual(words):
    """
    :type words: List[str]
    :rtype: bool
    """
    ll = len(words)
    if ll == 1: return True
    dd=dict()
    for w in words:
        for s in w:
            if s in dd:
                dd[s]+=1
            else:
                dd[s]=1
    set_v={v for v in dd.values()}
    return all([s%ll==0 for s in set_v])

# ic(makeEqual(["abc","aabc","bc"]))
# ic(makeEqual(["caaaaa","aaaaaaaaa","a","bbb","bbbbbbbbb","bbb","cc","cccccccccccc","ccccccc","ccccccc","cc","cccc","c","cccccccc","c"]))
# ic(makeEqual(["ab","a"]))
# ic(makeEqual(["aaaaaaaaaaaaaaaaa","aaaaa","aaaaaa","aaaaaaaaa","a","aaa","aaaa","bbbbbbbbbbbbbbbbbbbbbbb","bb","b","bb","bb","ccccccccccccccccccccccccccccccccccccccc","c","ccccc"]))
ic(makeEqual(["aa","abaab"]))
# set_v = {45, 15, 16}
# ic(gcd(*set_v), min(set_v))