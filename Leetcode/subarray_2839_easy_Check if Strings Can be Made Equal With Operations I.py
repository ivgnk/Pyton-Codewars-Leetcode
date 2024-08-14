"""
Done 14.08.2024. Topics: String
2839. Check if Strings Can be Made Equal With Operations I
https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i

You are given two strings s1 and s2, both of length 4, consisting of lowercase English letters.

You can apply the following operation on any of the two strings any number of times:

Choose any two indices i and j such that j - i = 2,
then swap the two characters at those indices in the string.
Return true if you can make the strings s1 and s2 equal, and false otherwise.

Example 1:
Input: s1 = "abcd", s2 = "cdab"
Output: true
Explanation: We can do the following operations on s1:
- Choose the indices i = 0, j = 2. The resulting string is s1 = "cbad".
- Choose the indices i = 1, j = 3. The resulting string is s1 = "cdab" = s2.

Example 2:
Input: s1 = "abcd", s2 = "dacb"
Output: false
Explanation: It is not possible to make the two strings equal.

Constraints:
s1.length == s2.length == 4
s1 and s2 consist only of lowercase English letters.

Hint 1
Since the strings are very small you can try a brute-force approach.
Hint 2
There are only 2 different swaps that are possible in a string.

Solution
✏️ Python easy greedy solution
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Since the array always has a length of 4, then just iterate through all the options

# Approach
<!-- Describe your approach to solving the problem. -->
Idea from
https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/description/comments/2493297

s1[0]<=>s1[2]==s2 ?
s1[1]<=>s1[3]==s2 ?
(s1[0]<=>s1[2] && s1[1]<=>s1[3])==s2?

Do not forget to copy the list, otherwise the error starts from about the 865th test

14.08.2024
Runtime 10 ms Beats 87.93%
Memory 11.58 MB Beats 86.21%
"""

# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/description/comments/2493297
# s1==s2 ?
# s1[0]<=>s1[2]==s2 ?
# s1[1]<=>s1[3]==s2 ?
# (s1[0]<=>s1[2] && s1[1]<=>s1[3])==s2?

# Runtime 23 ms Beats 15.52%
# Memory 11.64 MB Beats 48.28%
# Runtime 19 ms Beats 34.48%
# Memory 11.84 MB Beats 18.97%

from copy import deepcopy, copy
def canBeEqual2(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    if s1==s2: return True
    l1=list(s1); l2=list(s2)

    l3= deepcopy(l1)
    l3[0], l3[2] = l3[2], l3[0]
    if l3==l2: return True

    l3= deepcopy(l1)
    l3[1], l3[3] = l3[3], l3[1]
    if l3==l2: return True

    l3= deepcopy(l1)
    l3[0], l3[2] = l3[2], l3[0]
    l3[1], l3[3] = l3[3], l3[1]
    if l3==l2: return True

    return False

# Runtime 10 ms Beats 87.93%
# Memory 11.58 MB Beats 86.21%
def canBeEqual(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    if s1==s2: return True
    l1=list(s1); l2=list(s2)

    l3= copy(l1)
    l3[0], l3[2] = l3[2], l3[0]
    if l3==l2: return True

    l3= copy(l1)
    l3[1], l3[3] = l3[3], l3[1]
    if l3==l2: return True

    l3= copy(l1)
    l3[0], l3[2] = l3[2], l3[0]
    l3[1], l3[3] = l3[3], l3[1]
    if l3==l2: return True

    return False


print(canBeEqual(s1 ="bnxw", s2 = "bwxn"))



