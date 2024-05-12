"""
Done 13.05.2024. Topics: String
1784. Check if Binary String Has at Most One Segment of Ones
https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/description/

Given a binary string s without leading zeros, return true
if s contains at most one contiguous segment of ones. Otherwise, return false.

Example 1:
Input: s = "1001"
Output: false
Explanation: The ones do not form a contiguous segment.

Example 2:
Input: s = "110"
Output: true

Hint 1
It's guaranteed to have at least one segment
Hint 2
The string size is small so you can count all segments of ones with no that have no adjacent ones.
"""

# Runtime 8 ms Beats 93.48% of users with Python
# Memory 11.70 MB# Beats 65.22% of users with Python

from collections import Counter
def checkOnesSegment(s):
    """
    :type s: str
    :rtype: bool
    """
    dd = dict(Counter(s))
    return '1' * dd['1'] in s
