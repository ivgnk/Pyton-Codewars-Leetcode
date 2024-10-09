"""
Done 09.10.2024. Topics: String, Stack, Greedy
921. Minimum Add to Make Parentheses Valid
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description

A parentheses string is valid if and only if:
It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))"
or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

Example 1:
Input: s = "())"
Output: 1

Example 2:
Input: s = "((("
Output: 3

Constraints:
1 <= s.length <= 1000
s[i] is either '(' or ')'.


tip 1
3 cases
1> : " ()"
2>: "())"
3>: "))"

simple use stack and push whenever you see "("
but when ")" comes you have 2 options
1> either case is this "()" meaning peek of stack has "(" .. simply pop beacuse you found a good pair
2>else case is either empty stack or you don't find "(" then just add ")" as a redundant parenthesis because no good pair will be made from this.

In the end what ever is left in stack has to be solved and hence becomes the answer
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/comments/1570502
"""

# Runtime 11 ms Beats 84.33%
# Memory 11.75 MB Beats 14.29%
# Time Complexity O(N)
# Space Complexity O(N)
def minAddToMakeValid(s):
    """
    :type s: str
    :rtype: int
    """
    lst=[]
    for s1 in s:
        if s1=='(':
            lst.append(s1)
        else:
            if lst==[]: lst.append(s1)
            elif lst[-1]=='(': lst.pop()
            else: lst.append(s1)
    return len(lst)

print(minAddToMakeValid("())"))
print(minAddToMakeValid("((("))
print(minAddToMakeValid("()"))
