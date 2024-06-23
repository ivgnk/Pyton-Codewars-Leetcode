"""
Done 23.06.2024. Topics: String
3174. Clear Digits
https://leetcode.com/problems/clear-digits

You are given a string s.
Your task is to remove all digits by doing this operation repeatedly:
Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.

Example 1:
Input: s = "abc"
Output: "abc"
Explanation:
There is no digit in the string.

Example 2:
Input: s = "cb34"
Output: ""
Explanation:
First, we apply the operation on s[2], and s becomes "c4".
Then we apply the operation on s[1], and s becomes "".

Hint 1
Process string s from left to right, if s[i] is a digit, mark the nearest unmarked non-digit index to its left.
Hint 2
Delete all digits and all marked characters.
"""

# Runtime 7 ms Beats 99.00%
# Memory 11.56 MB Beats 77.37%
def clearDigits(s):
    """
    :type s: str
    :rtype: str
    """
    ll=len(s)
    res=[]; rll=range(ll)
    for i in rll:
        if s[i].isdigit():
            res.pop(-1)
        else: res.append(s[i])
    return ''.join(res)

print(clearDigits('abc'))
print(clearDigits("cb34"))