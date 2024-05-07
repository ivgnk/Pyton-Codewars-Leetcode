"""
Done 07.05.2024. Topics: String, Stack
1021. Remove Outermost Parentheses
https://leetcode.com/problems/remove-outermost-parentheses/description/

A valid parentheses string is either empty "", "(" + A + ")", or A + B,
where A and B are valid parentheses strings, and + represents string concatenation.
For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty,
and there does not exist a way to split it into s = A + B,
with A and B nonempty valid parentheses strings.
Given a valid parentheses string s, consider its primitive decomposition:
s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

Example 1:

Input: s = "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:
Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation:
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:

Input: s = "()()"
Output: ""
Explanation:
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
"""

# Runtime 17 ms Beats 85.59% of users with Python
# Memory 11.99 MB Beats 55.91% of users with Python

def removeOuterParentheses(s):
    """
    :type s: str
    :rtype: str
    """
    nl=0; res=''; curri=-1
    for i,s1 in enumerate(s):
        if s1=='(':
            nl=nl+1
            if curri<0: curri=i
        elif s1==')':
            nl=nl-1
        if nl==0 and i != 0:
            res=res+s[curri+1:i]
            curri=-1
    return res

print(removeOuterParentheses("(()())(())"))