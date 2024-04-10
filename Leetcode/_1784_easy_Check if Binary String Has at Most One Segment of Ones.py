"""
1784. Check if Binary String Has at Most One Segment of Ones
https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/description/

Given a binary string s without leading zeros, return true
if s contains at most one contiguous segment of ones.
Otherwise, return false.

Example 1:
Input: s = "1001"
Output: false
Explanation: The ones do not form a contiguous segment.

Example 2:
Input: s = "110"
Output: true
"""

# Wrong Answer -- 134 / 191 testcases passed
# s = "1100111" Output true    Expected false
# ??????????????

def checkOnesSegment(s):
    """
    :type s: str
    :rtype: bool
    """
    if s == '1': return True
    sother = set(s[1:]);
    if s[0] == '1' and sother == {'0'}: return True
    return s.find('11') >= 0
print(checkOnesSegment('10'))