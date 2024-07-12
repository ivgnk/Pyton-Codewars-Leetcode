"""
12.07.2024. Topics: String, Stack

1717. Maximum Score From Removing Substrings
https://leetcode.com/problems/maximum-score-from-removing-substrings

You are given a string s and two integers x and y. You can perform two types of operations any number of times.
Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

Example 1:
Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.

Example 2:
Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20

Constraints:
1 <= s.length <= 105
1 <= x, y <= 104
s consists of lowercase English letters.

Hint 1
Note that it is always more optimal to take one type of substring before another
Hint 2
You can use a stack to handle erasures
"""

# Time Limit Exceeded - 59 / 76 testcases passed
# len(s) = 84070
from icecream import ic
def maximumGain2(s, x, y):
    """
    :type s: str
    :type x: int
    :type y: int
    :rtype: int
    """
    if x>=y:
        s1='ab'; s2='ba'
    else:
        x,y=y,x
        s1='ba'; s2='ab'
    n=0;  tr1=True; tr2=True
    while tr1:
        if s1 in s:
            s=s.replace(s1,'',1)
            n=n+x
        else: tr1=False
    while tr2:
        if s2 in s:
            s=s.replace(s2,'',1)
            n=n+y
        else: tr2=False
    return n

# Time Limit Exceeded - 63 / 76 testcases passed
def maximumGain(s, x, y):
    """
    :type s: str
    :type x: int
    :type y: int
    :rtype: int
    """
    if x>=y:
        s1='ab'; s2='ba'
    else:
        x,y=y,x
        s1='ba'; s2='ab'
    n=0
    while s1 in s:
        nx = s.count(s1)
        s=s.replace(s1,'')
        n=n+x*nx

    while s2 in s:
        ny = s.count(s2)
        s=s.replace(s2,'')
        n=n+y*ny
    return n



ic(maximumGain(s = "cdbcbbaaabab", x = 4, y = 5))
ic(maximumGain(s = "aabbaaxybbaabb", x = 5, y = 4))



