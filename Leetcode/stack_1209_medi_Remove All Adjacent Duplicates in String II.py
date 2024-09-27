"""
Done 27.09.2024. Topics: String, Stack
1209. Remove All Adjacent Duplicates in String II
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

You are given a string s and an integer k,
a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them,
causing the left and the right side of the deleted substring to concatenate together.
We repeatedly make k duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made.
It is guaranteed that the answer is unique.

Example 1:
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Example 2:
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation:
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

Example 3:
Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"

Constraints:
1 <= s.length <= 105
2 <= k <= 104

Hint 1
Use a stack to store the characters, when there are k same characters, delete them.
Hint 2
To make it more efficient, use a pair to store the value and the count of each character.
"""

# Runtime 130 ms Beats 14.40%
# Memory 23.99 MB Beats 7.39%
from icecream import ic
def removeDuplicates2(s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    st=[]; k1=k-1
    chngd=True
    while chngd:
        chngd = False
        for i,s1 in enumerate(s):
            if st==[]:
                n=1
                st.append((s1,n))
            elif s1!=st[-1][0]:
                n=1
                st.append((s1,n))
            else: # s1==st[-1]
                if st[-1][1]==k1:
                    for i in range(k1):
                        st.pop()
                    chngd =True
                else:
                    n += 1
                    st.append((s1, n))
        s=''.join([s1[0] for s1 in st])
        st = []
    return s

# Runtime 64 ms Beats 89.11%
# Memory 17.62 MB Beats 49.81%
def removeDuplicates(s, k):
    stck = []
    for c in s:
        if stck and stck[-1][0] == c:
            stck[-1][1] += 1
            if stck[-1][1] == k:
                stck.pop()
        else:
            stck.append([c, 1])
    return "".join(c * cnt for c, cnt in stck)


ic(removeDuplicates(s = "abcd", k = 2))
ic(removeDuplicates(s = "deeedbbcccbdaa", k = 3))
ic(removeDuplicates(s = "pbbcggttciiippooaais", k = 2))