"""
1869. Longer Contiguous Segments of Ones than Zeros
https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/description/

Given a binary string s, return true if the longest contiguous segment of 1's is strictly longer
than the longest contiguous segment of 0's in s, or return false otherwise.
For example, in s = "110100010" the longest continuous segment of 1s has length 2,
and the longest continuous segment of 0s has length 3.
Note that if there are no 0's, then the longest continuous segment of 0's is considered to have a length 0.
The same applies if there is no 1's.

Example 1:
Input: s = "1101"
Output: true
Explanation:
The longest contiguous segment of 1s has length 2: "1101"
The longest contiguous segment of 0s has length 1: "1101"
The segment of 1s is longer, so return true.

Example 2:
Input: s = "111000"
Output: false
Explanation:
The longest contiguous segment of 1s has length 3: "111000"
The longest contiguous segment of 0s has length 3: "111000"
The segment of 1s is not longer, so return false.

Example 3:
Input: s = "110100010"
Output: false
Explanation:
The longest contiguous segment of 1s has length 2: "110100010"
The longest contiguous segment of 0s has length 3: "110100010"
The segment of 1s is not longer, so return false.
"""

# 10 ms Beats 92.65% of users with Python
# Memory 11.75 MB Beats 16.18% of users with Python

def checkZeroOnes(s):
    """
    :type s: str
    :rtype: bool
    """
    s1=s.split('0'); s1_=[len(ss) for ss in s1 if ss !='']
    s0 = s.split('1'); s0_=[len(ss) for ss in s0 if ss !='']
    m0=max(s0_) if s0_!=[] else 0
    m1=max(s1_) if s1_!=[] else 0
    return m1>m0

print(checkZeroOnes("1101"))