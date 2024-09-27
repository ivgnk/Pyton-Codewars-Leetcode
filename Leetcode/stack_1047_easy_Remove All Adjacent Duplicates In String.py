"""
Done 27.09.2024. Topics: String, Stack
1047. Remove All Adjacent Duplicates In String
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/

You are given a string s consisting of lowercase English letters.
A duplicate removal consists of choosing two adjacent and equal letters and removing them.
We repeatedly make duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made.
It can be proven that the answer is unique.

Example 1:
Input: s = "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

Example 2:
Input: s = "azxxzy"
Output: "ay"

Hint 1
Use a stack to process everything greedily.
"""

# Runtime 46 ms Beats 92.78%
# Memory 12.72 MB Beats 51.38%
def removeDuplicates(s: str) -> str:
    st=[]
    for s1 in s:
        if st==[]: st.append(s1)
        elif s1!=st[-1]:
            st.append(s1)
        else: st.pop()
    return ''.join(st)

print(removeDuplicates("abbaca"))


# Time Limit Exceeded -- 104 / 106 testcases passed
def removeDuplicates2(s: str) -> str:
    i = 1;  lls = len(s)
    while lls > i:
        nn = i - 1
        if s[i] == s[nn]:
            s = s[:nn] + s[i + 1:]
            i = 1
            lls = len(s)
        else:
            i = i + 1
    return s

# Time Limit Exceeded  - 104 / 106 testcases passed
def removeDuplicates3(s: str) -> str:
    s = list(s)
    i = 1;  lls = len(s)
    while lls > i:
        nn = i - 1
        if s[i] == s[nn]:
            s.pop(i)
            s.pop(nn)
            i = 1
            lls = len(s)
        else:
            i = i + 1
    return ''.join(s)

# not work
from itertools import groupby
def removeDuplicates4(s: str) -> str:
    n=[list(g) for k, g in groupby(s)] # [['v'], ['t'], ['k'], ['g'], ['n']]
    chngd=True
    while chngd:
        for i in range(len(n)):
            if len(n[i])>2: return False



