"""
Done 10.12.2024. Topics: Hash Table, String, Binary Search, Sliding Window
2981. Find Longest Special Substring That Occurs Thrice I
https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/

You are given a string s that consists of lowercase English letters.
A string is called special if it is made up of only a single character.
For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.

Return the length of the longest special substring of s which occurs at least thrice,
or -1 if no special substring occurs at least thrice.

A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
Input: s = "aaaa"
Output: 2
Explanation: The longest special substring which occurs thrice is "aa": substrings "aaaa", "aaaa", and "aaaa".
It can be shown that the maximum length achievable is 2.

Example 2:
Input: s = "abcdef"
Output: -1
Explanation: There exists no special substring which occurs at least thrice. Hence return -1.

Example 3:
Input: s = "abcaba"
Output: 1
Explanation: The longest special substring which occurs thrice is "a": substrings "abcaba", "abcaba", and "abcaba".
It can be shown that the maximum length achievable is 1.

Constraints:
3 <= s.length <= 50
s consists of only lowercase English letters.

Hint 1
The constraints are small.
Hint 2
Brute force checking all substrings.
"""

# Runtime 277 ms Beats 14.29%
# Memory 12.02 MB Beats 5.88%
def maximumLength(s):
    """
    :type s: str
    :rtype: int
    """
    ll=len(s); dd=dict()
    for i in range(ll):
        for j in range(i+1,ll+1):
            s1=s[i:j]
            if len(set(s1))==1:
                dd[s1]=dd.setdefault(s1,0)+1
    srt_it = sorted([len(k) for k,v in dd.items() if v>2])
    # print(srt_it)
    if srt_it==[]: return -1
    else: return srt_it[-1]

# Runtime 7 ms Beats 92.86%
# Memory 12.05 MB Beats 5.88%
from collections import defaultdict
# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/solutions/6131426/brute-force-solution-o-nlogn-using-dict/
def maximumLength2(s):
    dict = defaultdict(list)
    count = 1
    for i in range(len(s)):
        if i>0 and s[i]==s[i-1]:
            count+= 1
        else:
            count = 1
        dict[s[i]].append(count)

    maxlen = -1
    for value in dict.values():
        if len(value)>=3:
            value.sort(reverse = True)
            maxlen = max(maxlen, value[2])
    return maxlen

print(maximumLength("aaaa"))
print(maximumLength("abcdef"))
print(maximumLength("abcaba"))
