"""
08.07.2024. Topics: String, Backtracking, Bit Manipulation
784. Letter Case Permutation

Given a string s,
you can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create. Return the output in any order.

Example 1:
Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:
Input: s = "3z4"
Output: ["3z4","3Z4"]

Constraints:
1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits.

as Tip https://leetcode.com/problems/letter-case-permutation/description/comments/2370219
You can invert the character by ch ^= ' ' without knowing if it is upper or lower.
"""

# Runtime 36 ms Beats 64.00%
# Memory 12.40 MB Beats 75.00%
# Runtime 31 ms Beats 87.00%
# Memory 12.56 MB Beats 68.00%

def letterCasePermutation(s):
    ll = len(s)
    res=[]
    for i in range(ll):
        if i==0:
            if s[i].isalpha():
                res.append(s[i].lower())
                res.append(s[i].upper())
            else:
                res.append(s[i])
        else:
            res1=[]
            for j in range(len(res)):
                if s[i].isalpha():
                    res1.append(res[j]+s[i].lower())
                    res1.append(res[j]+s[i].upper())
                else:
                    res1.append(res[j]+s[i])
            res=res1
    return res

print(letterCasePermutation("3z4"))
print(letterCasePermutation("a1b2"))
