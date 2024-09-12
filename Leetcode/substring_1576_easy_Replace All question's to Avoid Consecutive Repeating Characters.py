"""
Done 12.09.2024. Topics: String
1576. Replace All ?'s to Avoid Consecutive Repeating Characters
https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/description/

Given a string s containing only lowercase English letters and the '?' character,
convert all the '?' characters into lowercase letters such that the final string does not contain any consecutive repeating characters.
You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made.
If there is more than one solution, return any of them.
It can be shown that an answer is always possible with the given constraints.

Example 1:
Input: s = "?zs"
Output: "azs"
Explanation: There are 25 solutions for this problem.
From "azs" to "yzs", all are valid.
Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".

Example 2:
Input: s = "ubv?w"
Output: "ubvaw"
Explanation: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings
will consist of consecutive repeating characters in "ubvvw" and "ubvww".

Constraints:
1 <= s.length <= 100
s consist of lowercase English letters and '?'.

Hint 1
Processing string from left to right, whenever you get a ‘?’,
check left character and right character, and select a character not equal to either of them
Hint 2
Do take care to compare with replaced occurrence of ‘?’ when checking the left character.
"""
# Runtime 30 ms Beats 91.95%
# Memory 16.60 MB Beats 8.50%
# Time Complexity O(N)
# Space Complexity O(N)

from icecream import ic
set_low={'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
def modifyString(s):
    """
    :type s: str
    :rtype: str
    """
    ll=len(s)
    if ll==1 and s=='?': return 'a'
    ss=[s1 for s1 in s]
    for i in range(ll):
        if ss[i]=='?':
            if i==0:
                new_let = set_low-set(ss[i+1])
            elif i==ll-1:
                new_let = set_low - set(ss[i-1])
            else:
                if s[i + 1] == '?':
                    new_let = set_low - set(ss[i-1])
                    # ic(s[i-i],new_let,'----')
                else: new_let = set_low-set(ss[i-1])-set(ss[i+1])
            ss[i]=new_let.pop()
    return ''.join(ss)

ic(modifyString("?ix????hn"))

