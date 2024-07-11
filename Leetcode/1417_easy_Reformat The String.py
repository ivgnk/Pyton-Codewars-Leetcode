"""
Done 11.07.2024. Topics: String
1417. Reformat The String
https://leetcode.com/problems/reformat-the-string/description/

You are given an alphanumeric string s.
(Alphanumeric string is a string consisting of lowercase English letters and digits).
You have to find a permutation of the string where no letter is followed by another letter and
no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.

Example 1:
Input: s = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.

Example 2:
Input: s = "leetcode"
Output: ""
Explanation: "leetcode" has only characters so we cannot separate them by digits.

Example 3:
Input: s = "1229857369"
Output: ""
Explanation: "1229857369" has only digits so we cannot separate them by characters.

Hint 1
Count the number of letters and digits in the string.
if cntLetters - cntDigits has any of the values [-1, 0, 1] we have an answer, otherwise we don't have any answer.
Hint 2
Build the string anyway as you wish.
Keep in mind that you need to start with the type that have more characters if cntLetters ≠ cntDigits.
"""

# Runtime 22 ms Beats 97.50%
# Memory 11.90 MB Beats 35.00%

aa_num = '0123456789'
def reformat(s):
    """
    :type s: str
    :rtype: str
    """
    a_alp = []; a_num=[]
    for s1 in s:
        if s1 in aa_num: a_num.append(s1)
        else: a_alp.append(s1)

    la=len(a_alp); ln=len(a_num)
    if ln-la>1 or ln-la<-1:  return ""
    elif ln>la:
        res = []
        for i in range(ln):
            res.append(a_num[i])
            if i !=(ln-1): res.append(a_alp[i])
    elif ln==la:
        res = []
        for i in range(ln):
            res.append(a_num[i])
            res.append(a_alp[i])
    else:
        res = []
        for i in range(la):
            res.append(a_alp[i])
            if i != (la - 1): res.append(a_num[i])
    return ''.join(res)

print(reformat("a0b1c2"))
# print(reformat("covid2019"))
