"""
Done 29.05.2024. Topics: String, Stack
1544. Make The String Great
https://leetcode.com/problems/make-the-string-great/description/

Given a string s of lower and upper case English letters.
A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:
0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them.
You can keep doing this until the string becomes good.
Return the string after making it good. The answer is guaranteed to be unique under the given constraints.
Notice that an empty string is also good.

Example 1:
Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".

Example 2:
Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""

Example 3:
Input: s = "s"
Output: "s"
"""
# Runtime 14 ms Beats 82.75% of users with Python
# Memory 11.63 MB Beats 66.15% of users with Python

a_hgh='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def makeGood(s):
    """
    :type s: str
    :rtype: str
    """
    ll=len(s)
    if ll<=1: return s
    if s.islower() or s.isupper(): return s
    s = list(s)
    flag=True
    while flag:
        i= ll-1
        while i>=1:
            if abs(ord(s[i])-ord(s[i-1])) == 32:
                s.pop(i)
                s.pop(i-1)
                i=i-2
            else: i=i-1
        nll=len(s)
        if nll==0 or ll==nll: flag=False
        else: ll=nll
    return ''.join(s)


# print(makeGood("leEeetcode"))
print(makeGood("abBAcC"))
# print(makeGood("s"))
