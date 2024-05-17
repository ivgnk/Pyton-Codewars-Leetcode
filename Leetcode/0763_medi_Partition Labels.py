"""
Done 18.08.2024. Topics: Hash Table, Two Pointers, String, Greedy
763. Partition Labels
https://leetcode.com/problems/partition-labels/description/

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
Return a list of integers representing the size of these parts.

Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Example 2:
Input: s = "eccbbbbdec"
Output: [10]

Hint 1
Try to greedily choose the smallest partition that includes the first letter.
If you have something like "abaccbdeffed", then you might need to add b.
You can use an map like "last['b'] = 5" to help you expand the width of your partition.
"""

from icecream import ic

def tst_range():
    a = [5, 11]
    b = [11, 15]
    print(list(range(max(a[0], b[0]), min(a[1], b[1]) + 1, 1)))

# Runtime 11 ms Beats 98.52% of users with Python
# Memory 11.69 MB Beats 62.61% of users with Python
def partitionLabels(s):
    # https://leetcode.com/problems/partition-labels/solutions/2300061/python-o-n-time-o-1-space-easy-explained/
    last = {}
    for i in range(len(s)):
        last[s[i]] = i
    most = 0
    res = []
    c = 0
    for i in range(len(s)):
        c = c + 1
        if last[s[i]] > most:
            most = last[s[i]]
        if last[s[i]] == most and i == most:
            res.append(c)
            most = 0
            c = 0
    return res

# Runtime 53 ms Beats 5.93% of users with Python
# Memory 11.72 MB Beats 26.11% of users with Python
# Runtime 52 ms Beats 5.93% of users with Python
# Memory 11.82 MB Beats 8.01% of users with Python

def partitionLabels2(s):
    """
    :type s: str
    :rtype: List[int]
    """
    ll = len(s)
    ddict = dict(); r=range(ll)
    for i, s1 in enumerate(s):
        if s1 not in ddict:
            ddict[s1] = [j for j in r if s[j] == s1]
    lst = sorted([[v, k] for k, v in ddict.items()])
    # print(lst)
    # ---
    ls = lst[0][0]
    a = [ls[0], ls[-1]];    res1 = []  # res=[];
    li = 0;    llst = len(lst)
    for i in range(1, llst):
        ls = lst[i][0]
        b = [ls[0], ls[-1]]
        if list(range(max(a[0], b[0]), min(a[1], b[1]) + 1, 1)) != []:
            li = max(a[1], b[1])
            a = [a[0], li]
        else:
            c = s[a[0]:a[1] + 1]
            res1.append(len(c))  # res.append(c);
            a = b
    else:
        c = s[a[0]:]
        res1.append(len(c))  # res.append(c);
    return res1


ic(partitionLabels("ababcbacadefegdehijhklij")) # "ababcbaca", "defegde", "hijhklij"
# tst_range()