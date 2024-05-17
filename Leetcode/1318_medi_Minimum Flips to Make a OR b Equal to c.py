"""
Done 17.05.2024. Topics: Bit Manipulation
1318. Minimum Flips to Make a OR b Equal to c
https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/description/

Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

Example 1:
Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)

Example 2:
Input: a = 4, b = 2, c = 7
Output: 1

Example 3:
Input: a = 1, b = 2, c = 3
Output: 0
"""

# Runtime 3 ms Beats 99.47% of users with Python
# Memory 11.43 MB Beats 95.77% of users with Python

from icecream import ic
def minFlips(a, b, c):
    """
    :type a: int
    :type b: int
    :type c: int
    :rtype: int
    """
    sa=bin(a)[2:]; la=len(sa)
    sb=bin(b)[2:]; lb=len(sb)
    sc=bin(c)[2:]; lc=len(sc)
    ll=max(la,lb,lc)
    sa = '0' * (ll - la) + sa
    sb = '0' * (ll - lb) + sb
    sc = '0' * (ll - lc) + sc

    print(sa, sb, sc)
    ssum = 0
    for i in range(ll):
        if sa[i] == sb[i]:
            if sb[i] != sc[i]:
                if sc[i] == '0':
                    ssum = ssum + 2
                else:
                    ssum = ssum + 1
        else:
            if sc[i] == '0': ssum = ssum + 1
    return ssum


print(minFlips( a = 8, b = 3, c = 5))