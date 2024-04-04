'''
1796. Second Largest Digit in a String
https://leetcode.com/problems/second-largest-digit-in-a-string/description/

Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.
An alphanumeric string is a string consisting of lowercase English letters and digits.

Example 1:
Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.

Example 2:
Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit.
'''

# Runtime 26 ms Beats 48.06% of users with Python
# Memory 11.76 MB Beats 44.96% of users with Python

def secondHighest(s):
    """
    :type s: str
    :rtype: int
    """
    x = [int(s1) for s1 in s if s1.isdigit()]
    if x == []: return -1
    yset = set(x)
    yset2 = sorted(yset, key=int, reverse=True)
    if len(yset2) == 1:
        return -1
    else:
        return yset2[1]

print(secondHighest("dfa12321afd"))