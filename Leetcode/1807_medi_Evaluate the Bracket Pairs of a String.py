"""
Done 01.09.2024. Topics: Hash Table, String
1807. Evaluate the Bracket Pairs of a String
https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/description/

You are given a string s that contains some bracket pairs, with each pair containing a non-empty key.

For example, in the string "(name)is(age)yearsold",
there are two bracket pairs that contain the keys "name" and "age".
You know the values of a wide range of keys. This is represented by a 2D string array knowledge
where each knowledge[i] = [keyi, valuei] indicates that key keyi has a value of valuei.

You are tasked to evaluate all of the bracket pairs. When you evaluate a bracket pair
that contains some key keyi, you will:

Replace keyi and the bracket pair with the key's corresponding valuei.
If you do not know the value of the key, you will replace keyi and the bracket pair with
a question mark "?" (without the quotation marks).
Each key will appear at most once in your knowledge.
There will not be any nested brackets in s.

Return the resulting string after evaluating all of the bracket pairs.

Example 1:
Input: s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]
Output: "bobistwoyearsold"
Explanation:
The key "name" has a value of "bob", so replace "(name)" with "bob".
The key "age" has a value of "two", so replace "(age)" with "two".

Example 2:
Input: s = "hi(name)", knowledge = [["a","b"]]
Output: "hi?"
Explanation: As you do not know the value of the key "name", replace "(name)" with "?".

Example 3:
Input: s = "(a)(a)(a)aaa", knowledge = [["a","yes"]]
Output: "yesyesyesaaa"
Explanation: The same key can appear multiple times.
The key "a" has a value of "yes", so replace all occurrences of "(a)" with "yes".
Notice that the "a"s not in a bracket pair are not evaluated.


Constraints:

1 <= s.length <= 10**5
0 <= knowledge.length <= 10**5
knowledge[i].length == 2
1 <= keyi.length, valuei.length <= 10
s consists of lowercase English letters and round brackets '(' and ')'.
Every open bracket '(' in s will have a corresponding close bracket ')'.
The key in each bracket pair of s will be non-empty.
There will not be any nested bracket pairs in s.
keyi and value i consist of lowercase English letters.
Each keyi  in knowledge is unique.

Hint 1
Process pairs from right to left to handle repeats
Hint 2
Keep track of the current enclosed string using another string

Solution
✏️ Easy Python solution with dictionary and symbol analysis
Intuition
Knowledge list transgorm to dictionary.
You can replace brackets with the correct keys using the replace function using a dictionary,
but then you need to bypass the case when the word is not in the dictionary.
You can come up with a regular expression or a character-by-character analysis of the remaining brackets.

Approach
But it is better to immediately do a character-by-character analysis of the string
"""

# Runtime 705 ms Beats 76.19%
# Memory 77.06 MB Beats 23.81%
def evaluate(s, knowledge):
    dd={k[0]:k[1] for k in knowledge }
    res=[]; NoBr=True; kkey=''
    for i,s1 in enumerate(s):
        if s1=='(':
            kkey=''
            NoBr = False
        elif NoBr:
            res.append(s1)
        elif s1==')':
            if kkey in dd:
                res.append(dd[kkey])
            else:
                res.append("?")
            NoBr = True
        elif not NoBr:
            kkey += s1
    return ''.join(res)


# bad test case 2 - no that key
def evaluate2(s, knowledge):
    """
    :type s: str
    :type knowledge: List[List[str]]
    :rtype: str
    """
    dd={k[0]:k[1] for k in knowledge }
    s = s.replace('(', ' ').replace(')', ' ').split()
    res=[]
    for s1 in s:
        if s1 in dd:
            res.append(dd[s1])
        else:
            res.append(s1)
    return ''.join(res)

# print(evaluate(s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]))

# Wrong Answer - 47 / 105 testcases passed
# Output: "?r"
# Expected: "?tzv?r"

import re
def evaluate3(s, knowledge):
    """
    :type s: str
    :type knowledge: List[List[str]]
    :rtype: str
    """
    for k in knowledge:
        s=s.replace('('+k[0]+')',k[1])
    s = re.sub(r'\(.+\)', '?', s)
    return s

# Runtime 9477 ms Beats 14.29%
# Memory 76.62 MB Beats 100.00%
def evaluate4(s, knowledge):
    """
    :type s: str
    :type knowledge: List[List[str]]
    :rtype: str
    """
    for k in knowledge:
        s=s.replace('('+k[0]+')',k[1])
    res=[]; NoBr=True
    for s1 in s:
        if s1=='(':
            NoBr = False
            res.append('?')
        elif NoBr:
            res.append(s1)
        elif s1==')':
            NoBr = True
    return ''.join(res)

from icecream import ic


ic(evaluate(s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]))
ic(evaluate(s = "hi(name)", knowledge = [["a","b"]]))

