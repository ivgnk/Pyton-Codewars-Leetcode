"""
Done 11.07.2024. Topics: String, Stack
1190. Reverse Substrings Between Each Pair of Parentheses
https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

You are given a string s that consists of lower case English letters and brackets.
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any brackets.

Example 1:
Input: s = "(abcd)"
Output: "dcba"

Example 2:
Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.

Example 3:
Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.

Constraints:
1 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It is guaranteed that all parentheses are balanced.

Hint 1
Find all brackets in the string.
Hint 2
Does the order of the reverse matter ?
Hint 3
The order does not matter.
"""

# on the base of https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/comments/1828809
# Runtime 11 ms Beats 95.12%
# Time Complexity O(N**2)
# Memory 11.96 MB Beats 12.20%
    # Space Complexity O(N)



def reverseParentheses(s):
    """
    :type s: str
    :rtype: str
    """
    sst=[['']]; j=0
    for i,s1 in enumerate(s):
        # print(i,'bef', s1, sst)
        if s1 != '(' and s1 != ')':
            if j==0: sst[0].append(s1)
            else: sst[j].append(s1)
        elif s1 == '(':
            j=j+1
            sst.append([])
        elif s1 == ')':
            for k in range(len(sst[j])-1,-1,-1):
                sst[j-1].append(sst[j][k])
            sst.pop()
            j=j-1
        # print(i,'aft', s1, sst)
    return ''.join(sst[0])

print(reverseParentheses("(abcd)")) # "dcba"
print(reverseParentheses("(u(love)i)")) # iloveu
print(reverseParentheses("(ed(et(oc))el)")) # leetcode


