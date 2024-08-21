"""
Done 21.08.2024. Topics: String
2609. Find the Longest Balanced Substring of a Binary String
https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/description/

You are given a binary string s consisting only of zeroes and ones.

A substring of s is considered balanced if all zeroes are before ones and the number of zeroes
is equal to the number of ones inside the substring.
Notice that the empty substring is considered a balanced substring.
Return the length of the longest balanced substring of s.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "01000111"
Output: 6
Explanation: The longest balanced substring is "000111", which has length 6.

Example 2:
Input: s = "00111"
Output: 4
Explanation: The longest balanced substring is "0011", which has length 4.

Example 3:
Input: s = "111"
Output: 0
Explanation: There is no balanced substring except the empty substring, so the answer is 0.

Constraints:
1 <= s.length <= 50
'0' <= s[i] <= '1'

Hint 1
Consider iterating over each subarray and checking if it’s balanced or not.
Hint 2
Among all balanced subarrays, the answer is the longest one of them.
"""

# Runtime 96 ms Beats 18.64%
# Memory 11.54 MB Beats 84.75%
def findTheLongestBalancedSubstring2(s):
    """
    :type s: str
    :rtype: int
    """
    ll=len(s); mmax=0
    if (not '1' in s) or (not '0' in s): return mmax
    for i in range(ll-1):
        for j in range(i+1,ll+1):
            s1=s[i:j]
            ll1=len(s1)
            if ll1%2==0:
                if s1.count('0') == ll1//2:
                    if not '1' in s1[:ll1//2]:
                        mmax =max(mmax,ll1)
    return mmax

# Runtime 68 ms Beats 20.34%
# Memory 11.53 MB Beats 84.75%
def findTheLongestBalancedSubstring3(s):
    """
    :type s: str
    :rtype: int
    """
    ll = len(s); mmax = 0
    if (not '1' in s) or (not '0' in s): return mmax
    for i in range(ll - 1):
        for j in range(i + 2, ll + 1, 2):
            s1 = s[i:j]
            ll1 = len(s1)
            if s1.count('0') == ll1 // 2:
                if not '1' in s1[:ll1 // 2]:
                    mmax = max(mmax, ll1)
    return mmax

# Runtime 26 ms Beats 45.76%
# Memory 11.60 MB Beats 84.75%
def findTheLongestBalancedSubstring4(s):
    """
    :type s: str
    :rtype: int
    """
    ll=len(s); mmax=0
    if (not '1' in s) or (not '0' in s): return mmax
    for i in range(ll-1):
        for j in range(i+2,ll+1,2):
            s1=s[i:j]
            ll1=len(s1)
            if not '1' in s1[:ll1//2]:
                if s1.count('0') == ll1//2:
                    mmax = max(mmax,ll1)
            else: break
    return mmax

# Runtime 26 ms Beats 45.76%
# Memory 11.52 MB Beats 84.75%
def findTheLongestBalancedSubstring4(s):
    """
    :type s: str
    :rtype: int
    """
    ll=len(s); mmax=0
    if (not '1' in s) or (not '0' in s): return mmax
    for i in range(ll-1):
        if s[i]=='1': continue
        for j in range(i+2,ll+1,2):
            s1=s[i:j]
            ll1=len(s1)
            if not '1' in s1[:ll1//2]:
                if s1.count('0') == ll1//2:
                    mmax = max(mmax,ll1)
            else: break
    return mmax

# Runtime 8 ms Beats 100.00%
# Memory 11.67 MB Beats 54.24%

# https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/solutions/5472632/counting-clean-simple-no-string-concatenation-python3/
def findTheLongestBalancedSubstring(s):
    result = 0
    c0, c1 = 0, 0  # counting consecutive zeros and ones in the window

    for num in s:
        if num == '0':  # either start a new window, or continue current one with all 0s
            if c1 > 0:  # ones cannot appear before zeros, reset counts, start a new window
                c0 = c1 = 0
            c0 += 1
        elif c1 < c0:  # at '1', only update result if number of 1s is less than number of 0s
            c1 += 1
            result = max(result, c1 * 2)  # result has to be balanced, 00011, c0=3, c1=2, result = c1 * 2 = 4

    return result

print(findTheLongestBalancedSubstring("01000111"))
print(findTheLongestBalancedSubstring("00111"))
print(findTheLongestBalancedSubstring("111"))