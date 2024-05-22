"""
Done 22.05.2024. Topics: String, Stack
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/description/

Given a string s containing just the characters
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Hint 1
Use a stack of characters.
Hint 2
When you encounter an opening bracket, push it to the top of the stack.
Hint 3
When you encounter a closing bracket, check if the top of the stack was the opening for it.
If yes, pop it from the stack.
Otherwise, return false.
"""

# Wrong Answer -- 90 / 98 testcases passed
def isValid2(self, s):
    """
    :type s: str
    :rtype: bool
    """
    mkr = 0;  mkv = 0;   mfg = 0
    # smaxkr = 0;  smaxkv = 0; smaxfg = 0
    for i in range(len(s)):
        match s[i]:
            case '(':
                mkr = mkr + 1
                # smaxkr = max(smaxkr, mkr)
            case ')':
                mkr = mkr - 1
                # smaxkr = max(smaxkr, mkr)
            case '[':
                mkv = mkv + 1
                # smaxkv = max(smaxkv, mkv)
            case ']':
                mkv = mkv - 1
                # smaxkv = max(smaxkv, mkv)
            case '{':
                mfg = mfg + 1
                # smaxkv = max(smaxfg, mfg)
            case '}':
                mfg = mfg - 1
                # smaxfg = max(smaxfg, mfg)
    return mfg==0 and mkv==0 and mkr==0


# Runtime 37 ms Beats 46.32% of users with Python3
# Memory 16.56 MB Beats 74.54% of users with Python3
# Runtime 34 ms Beats 67.14% of users with Python3
# Memory 16.73 MB Beats 5.91% of users with Python3

def isValid(s):
    if len(s)==1: return False
    if s[0]==')' or s[0]==']' or s[0]=='}': return False

    s2=[]
    for s1 in s:
        # print(s1,s2)
        if s1=='(' or s1=='{' or s1=='[':
            s2.insert(0,s1)
        elif s2==[]:return False
        elif s1==')' or s1=='}' or s1==']':
            if s1==')' and s2[0] != '(': return False
            elif s1==']' and s2[0] != '[': return False
            elif s1=='}' and s2[0] != '{': return False
            s2.pop(0)
    return s2==[]

print(isValid('(){}}{'))